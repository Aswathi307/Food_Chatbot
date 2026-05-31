from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    prompt = f"""
    You are a food recipe assistant.

    Answer briefly and clearly.

    Question:
    {user_message}
    """

    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 100
        }
    }
)

    reply = response.json()["response"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)