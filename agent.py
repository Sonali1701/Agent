# agent.py
from retriever import get_top_chunks
from llm import ask_llm
import math

def calculator(query):
    try:
        result = eval(query.split("calculate")[1])
        return f"The result is {result}"
    except Exception:
        return "Failed to calculate."

def define_word(query):
    word = query.split("define")[1].strip()
    return f"{word}: A placeholder definition (hook a real dictionary API here)."

def route_query(query):
    decision_log = []
    if "calculate" in query:
        decision_log.append("Routed to calculator tool")
        return calculator(query), decision_log
    elif "define" in query:
        decision_log.append("Routed to dictionary tool")
        return define_word(query), decision_log
    else:
        decision_log.append("Routed to RAG pipeline")
        chunks = get_top_chunks(query)
        context = "\n".join([doc.page_content for doc in chunks])
        answer = ask_llm(context, query)
        return answer, decision_log, context, chunks
