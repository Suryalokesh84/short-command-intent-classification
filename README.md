# 🧠 Short Command Intent Classification

## 🚀 Overview
This project classifies short user commands like "lights off" or "volume up" into intent categories such as:
- `smart_home`
- `media`
- `alarm`

We're using:
- ✅ Manually created word embeddings
- ✅ A simple ANN model built with TensorFlow/Keras

---

## 📁 Project Structure

| Folder        | Purpose                         |
|---------------|----------------------------------|
| `data/`       | CSV dataset of commands         |
| `embeddings/` | Manually defined word vectors   |
| `model/`      | ANN model and training script   |
| `utils/`      | Preprocessing logic             |
| `test/`       | Run predictions on new input    |

---

## 🧪 Sample Dataset

| Command     | Intent      |
|-------------|-------------|
| lights off  | smart_home  |
| play music  | media       |
| set alarm   | alarm       |

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/Suryalokesh84/short-command-intent-classification.git
cd short-command-intent-classification
pip install -r requirements.txt
