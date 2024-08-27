from flask import render_template, request, jsonify
import markdown
from app.main import main
from app.main.utils import gen_response, get_suggestions, load_suggestions_from_json, send_email, clean_response


predefined_suggestions = load_suggestions_from_json('suggestions.json')

@main.route('/suggest', methods=['POST'])
def suggest():
    input_text = request.form['input_text'].lower()
    suggestions = get_suggestions(input_text)
    return jsonify(suggestions)

@main.route('/save_and_send', methods=['GET', 'POST'])
def save_and_send():
    email = request.form['email']
    category = request.form['category']
    query = request.form['taskdescription']
    send_email(email, category, query)
    return render_template('chat.html')

@main.route("/get", methods=["GET", "POST"])
def chat():
    question = request.form.get("msg")
    response = gen_response(question)
    cleaned_response = clean_response(response)
    html_response = markdown.markdown(cleaned_response)
    return jsonify({'response': html_response})

@main.route("/")
def index():
    return render_template('chat.html')
