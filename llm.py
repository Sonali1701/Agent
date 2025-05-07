# llm.py
from groq import Groq

client = Groq(api_key="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")

def ask_llm(context, query):
    prompt = f"Answer the question based on the following context:\n{context}\n\nQ: {query}\nA:"
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()
