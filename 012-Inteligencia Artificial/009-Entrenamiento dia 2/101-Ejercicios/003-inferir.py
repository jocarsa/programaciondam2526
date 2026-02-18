#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ------------------------------------------------------------
# Paths relative to THIS script
# ------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder produced by the merge script
# Example:
#   ./lora-cpu-lowram/Qwen_Qwen2.5-0.5B-Instruct-merged
MODEL_PATH = os.path.join(
    SCRIPT_DIR,
    "lora-cpu-lowram",
    "Qwen_Qwen2.5-0.5B-Instruct-merged"
)

# HF cache in writable local folder
HF_CACHE = os.path.join(SCRIPT_DIR, ".hf-cache")
os.environ["HF_HOME"] = HF_CACHE
os.makedirs(HF_CACHE, exist_ok=True)


def main():
    if len(sys.argv) < 2:
        print("No prompt provided", file=sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]

    use_cuda = torch.cuda.is_available()
    dtype = (
        torch.bfloat16 if use_cuda and torch.cuda.is_bf16_supported()
        else torch.float16 if use_cuda
        else torch.float32
    )

    # --------------------------------------------------------
    # Load tokenizer + model (OFFLINE, merged model)
    # --------------------------------------------------------
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        local_files_only=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        local_files_only=True,
        torch_dtype=dtype,
        device_map="auto" if use_cuda else {"": "cpu"},
    )

    # --------------------------------------------------------
    # Chat prompt
    # --------------------------------------------------------
    conv = [
        {
            "role": "system",
            "content": (
                "Responde a la pregunta que se realiza:"
                "Si no conoces la respuesta, indicalo."
            ),
        },
        {"role": "user", "content": prompt},
    ]

    # Use chat template if available
    try:
        chat_text = tokenizer.apply_chat_template(
            conv,
            tokenize=False,
            add_generation_prompt=True,
        )
    except Exception:
        chat_text = (
            f"SYSTEM: {conv[0]['content']}\n"
            f"USER: {prompt}\n"
            f"ASSISTANT:"
        )

    inputs = tokenizer(chat_text, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    input_len = inputs["input_ids"].shape[-1]

    # --------------------------------------------------------
    # Generate
    # --------------------------------------------------------
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    generated_ids = output_ids[0, input_len:]
    answer = tokenizer.decode(
        generated_ids,
        skip_special_tokens=True
    ).strip()

    print(answer)


if __name__ == "__main__":
    main()
