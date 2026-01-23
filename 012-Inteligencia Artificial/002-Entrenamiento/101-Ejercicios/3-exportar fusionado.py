#!/usr/bin/env python3
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Modelo base de Hugging Face
BASE_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

# Carpeta donde guardaste los adaptadores tras el entrenamiento
ADAPTER_PATH = "./qwen25-05b-jvc"

# Carpeta de salida con el modelo ya fusionado (base + LoRA)
OUT_PATH = "./qwen25-05b-jvc-merged"

def main():
    os.makedirs(OUT_PATH, exist_ok=True)

    print("Cargando modelo base de Qwen...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )

    print("Cargando adaptadores LoRA desde", ADAPTER_PATH)
    model = PeftModel.from_pretrained(
        base_model,
        ADAPTER_PATH,
    )

    print("Fusionando LoRA en el modelo base (merge_and_unload)...")
    model = model.merge_and_unload()

    print("Guardando modelo fusionado en", OUT_PATH)
    model.save_pretrained(OUT_PATH)

    print("Guardando tokenizer en", OUT_PATH)
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
    tokenizer.save_pretrained(OUT_PATH)

    print("✅ Modelo fusionado guardado correctamente.")

if __name__ == "__main__":
    main()

