from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_cors import cross_origin

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        return render_template('chat.html', first_name=first_name, last_name=last_name, email=email)
    return render_template('index.html')

# Webhook route for Dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')

    # Handle intents
    if intent == 'Football Team':
        fulfillment_text = 'Yes, the University of Cincinnati has a football team known as the Bearcats.'
    elif intent == 'Computer Science Major':
        fulfillment_text = 'Yes, we offer a comprehensive Computer Science major with various specializations.'
    elif intent == 'In-State Tuition':
        fulfillment_text = 'The in-state tuition is approximately $11,000 per year.'
    elif intent == 'On-Campus Housing':
        fulfillment_text = 'Yes, we provide on-campus housing options for students.'
    else:
        fulfillment_text = 'I am sorry, I did not understand your question. Could you please rephrase it?'

    response = {
        "fulfillmentText": fulfillment_text
    }

    return jsonify(response)


# Route for the conclusion page
@app.route('/conclusion', methods=['GET'])
def conclusion():
    user_first_name = request.args.get('first_name')
    user_last_name = request.args.get('last_name')
    user_email = request.args.get('email')

    creator_first_name = 'Rohan'
    creator_last_name = 'Pothuru'
    creator_email = 'pothurrs@mail.uc.edu'

    return render_template('conclusion.html',
                           user_first_name=user_first_name,
                           user_last_name=user_last_name,
                           user_email=user_email,
                           creator_first_name=creator_first_name,
                           creator_last_name=creator_last_name,
                           creator_email=creator_email)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)