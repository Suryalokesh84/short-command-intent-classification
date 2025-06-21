def predict_intent(command):
    if any(w in command for w in ["light", "fan", "tv", "music", "ac"]):
        return "smart_home"
    elif "alarm" in command:
        return "alarm"
    return "unknown"
