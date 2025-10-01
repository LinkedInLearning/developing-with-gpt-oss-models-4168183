from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# Configure OpenAI SDK to use Ollama local endpoint


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat/", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    try:
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )
        assistant_msg = response.choices[0].message.content
        return jsonify({"reply": assistant_msg})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)