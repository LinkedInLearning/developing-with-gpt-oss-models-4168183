from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat/", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call OpenAI ChatCompletion
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=[{"role": "user", "content": user_message}]
        )
        assistant_reply = response.choices[0].message.content.strip()
        return jsonify({"reply": assistant_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)