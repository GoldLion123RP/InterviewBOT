from flask import Flask, render_template, jsonify, request, send_from_directory
import random
import os
from questions import questions_db  # Import from questions.py

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/topics', methods=['GET'])
def get_topics():
    topics = {
        "DSA": "Data Structures & Algorithms",
        "OOP": "Object-Oriented Programming",
        "DBMS": "Database Management Systems",
        "OS": "Operating Systems",
        "CN": "Computer Networks",
        "AI": "Artificial Intelligence"
    }
    return jsonify(topics)

@app.route('/api/questions', methods=['POST'])
def get_questions():
    data = request.json
    topic = data.get('topic')
    num_questions = data.get('num_questions', 5)
    
    if topic == 'ALL':
        all_questions = []
        for t, questions in questions_db.items():
            for q in questions:
                q_copy = q.copy()
                q_copy['topic'] = t
                all_questions.append(q_copy)
        random.shuffle(all_questions)
        selected = all_questions[:num_questions]
    else:
        questions = questions_db.get(topic, [])
        selected = random.sample(questions, min(num_questions, len(questions)))
        for q in selected:
            q['topic'] = topic
    
    return jsonify(selected)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
