import google.generativeai as genai

genai.configure(api_key="AIzaSyBIY1yFW9fwRX59WIETbV-9Svpi4Z-wsDs")

print("✅ Connected! Available models:\n")
for model in genai.list_models():
    print(model.name)
