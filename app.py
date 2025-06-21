from flask import Flask, request, jsonify, render_template
from model.predict import predict_intent

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json.get("command", "").lower()
    intent = predict_intent(user_input)

    if "light" in user_input:
        obj = "light"
    elif "fan" in user_input:
        obj = "fan"
    elif "tv" in user_input:
        obj = "tv"
    elif "music" in user_input:
        obj = "music"
    elif "ac" in user_input:
        obj = "ac"
    elif "alarm" in user_input:
        obj = "alarm"
    else:
        obj = "unknown"

    action = "on" if "on" in user_input or "play" in user_input or "set" in user_input else "off"
    return jsonify({"intent": intent, "object": obj, "action": action})

if __name__ == "__main__":
    app.run(debug=True)
