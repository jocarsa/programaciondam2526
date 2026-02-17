#!/usr/bin/env python3
import os
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

PROJECT_DIR = "/var/www/html/ia1"
MODEL_PATH = os.path.join(PROJECT_DIR, "qwen25-05b-jvc-merged")

# Cache de HF en sitio escribible (por si acaso)
os.environ["HF_HOME"] = "/tmp/hf-cache"
os.makedirs(os.environ["HF_HOME"], exist_ok=True)

def main():
    if len(sys.argv) < 2:
        print("No prompt provided", file=sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]

    # Cargar tokenizer y modelo desde el modelo fusionado, sin ir a internet
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        local_files_only=True,
        fix_mistral_regex=True  # evita el warning del regex
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        local_files_only=True,
        device_map="auto" if torch.cuda.is_available() else None,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    if not torch.cuda.is_available():
        model.to("cpu")

    conv = [
        {
            "role": "system",
            "content": (
                "Eres un asistente educativo en español de TAME Centro de Formación. "
                "Respondes dudas sobre los ciclos formativos (DAM, DAW, SMR, etc.), "
                "sus módulos, contenidos y orientación académica y profesional, de forma clara y concisa."
            )
        },
        {"role": "user", "content": prompt},
    ]

    chat_text = tokenizer.apply_chat_template(
        conv,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(chat_text, return_tensors="pt").to(model.device)
    input_len = inputs["input_ids"].shape[-1]

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.6,
            do_sample=True,
        )

    generated_ids = output_ids[0, input_len:]
    answer = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    print(answer)

if __name__ == "__main__":
    main()
