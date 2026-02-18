#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Must match training config
PRIMARY_MODEL  = "microsoft/Phi-3-mini-4k-instruct"
FALLBACK_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"
OUTPUT_DIR     = "./lora-cpu-lowram"

# Choose which base model you want to merge for:
# - If your training actually used Qwen (fallback), keep this as FALLBACK_MODEL.
# - If training used Phi-3, set BASE_MODEL = PRIMARY_MODEL.
BASE_MODEL = FALLBACK_MODEL

# Adapter path as produced by the trainer script
ADAPTER_PATH = os.path.join(OUTPUT_DIR, BASE_MODEL.replace("/", "_"))

# Output merged folder
OUT_PATH = ADAPTER_PATH + "-merged"


def main():
    if not os.path.isdir(ADAPTER_PATH):
        raise FileNotFoundError(
            f"Adapter folder not found: {ADAPTER_PATH}\n"
            f"Check which model was used during training and set BASE_MODEL accordingly."
        )

    os.makedirs(OUT_PATH, exist_ok=True)

    use_cuda = torch.cuda.is_available()
    dtype = (torch.bfloat16 if use_cuda and torch.cuda.is_bf16_supported()
             else torch.float16 if use_cuda
             else torch.float32)

    print("BASE_MODEL   :", BASE_MODEL)
    print("ADAPTER_PATH :", ADAPTER_PATH)
    print("OUT_PATH     :", OUT_PATH)
    print("CUDA         :", use_cuda, "| dtype:", dtype)

    print("Loading base model...")
    base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=dtype,
        device_map="auto" if use_cuda else {"": "cpu"},
    )

    print("Loading tokenizer...")
    tok = AutoTokenizer.from_pretrained(BASE_MODEL, use_fast=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token

    print("Loading LoRA adapters...")
    model = PeftModel.from_pretrained(base, ADAPTER_PATH)

    print("Merging (merge_and_unload)...")
    merged = model.merge_and_unload()

    try:
        merged.config.use_cache = True
    except Exception:
        pass

    print("Saving merged model...")
    merged.save_pretrained(OUT_PATH, safe_serialization=True)

    print("Saving tokenizer...")
    tok.save_pretrained(OUT_PATH)

    print("✅ Merged model saved at:", OUT_PATH)


if __name__ == "__main__":
    main()
