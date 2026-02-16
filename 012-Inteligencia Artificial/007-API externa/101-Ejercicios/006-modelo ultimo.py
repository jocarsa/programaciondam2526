import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAIAPI")
)

response = client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Quiero que me hagas una web en HTML y CSS, será una web personal de portafolio. Solo quiero el código, no me des ningun tipo de explicacion"}
    ],
    temperature=0.3
)

archivo = open("miweb.html",'w')
archivo.write(response.choices[0].message.content)
archivo.close()
print("ok")
