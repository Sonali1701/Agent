# agent.py
from retriever import get_top_chunks
from llm import ask_llm
import math
import re


def calculator(query):
    """Handles basic math queries using safe evaluation."""
    try:
        expression = re.search(r"calculate (.+)", query, re.IGNORECASE)
        if expression:
            result = eval(expression.group(1), {"__builtins__": None}, math.__dict__)
            return f" The result of the calculation is: **{result}**"
        return " Couldn't extract a valid expression to calculate."
    except Exception as e:
        return f" Failed to calculate due to error: {str(e)}"


def define_word(query):
    """Handles word definition requests."""
    word_match = re.search(r"define (\w+)", query, re.IGNORECASE)
    if word_match:
        word = word_match.group(1)
        # Placeholder for future integration with a dictionary API
        return f" **{word}**: *[Definition placeholder]* (https://api.dictionaryapi.dev/api/v2/entries/en/<word>)"
    return " Couldn't extract the word to define."


def route_query(query):
    """Routes the query to the appropriate tool or RAG pipeline."""
    decision_log = []

    if "calculate" in query.lower():
        decision_log.append("🛠 Routed to: Calculator tool")
        answer = calculator(query)
        return {"answer": answer, "decision_log": decision_log}

    elif "define" in query.lower():
        decision_log.append(" Routed to: Dictionary tool")
        answer = define_word(query)
        return {"answer": answer, "decision_log": decision_log}

    else:
        decision_log.append(" Routed to: RAG pipeline")
        chunks = get_top_chunks(query)
        context = "\n".join([doc.page_content for doc in chunks])
        answer = ask_llm(context, query)
        return {
            "answer": answer,
            "decision_log": decision_log,
            "context": context,
            "chunks": chunks
        }
