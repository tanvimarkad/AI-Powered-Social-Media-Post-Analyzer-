import google.generativeai as genai
import os

# Load key from apikey.txt
with open("apikey.txt", "r", encoding="utf-8") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)

print("\n✅ Listing available models:\n")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print("-", m.name)
