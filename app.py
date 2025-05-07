# app.py
import os
from flask import Flask, render_template, request
from agent import route_query

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    answer, decision_log, context, chunks = "", [], "", []
    if request.method == 'POST':
        query = request.form['query']
        result = route_query(query)
        if len(result) == 2:
            answer, decision_log = result
        else:
            answer, decision_log, context, chunks = result
    return render_template('index.html', answer=answer, log=decision_log, context=context, chunks=chunks)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # use Render's PORT if set
    app.run(host="0.0.0.0", port=port)