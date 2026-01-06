from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def ping_colab():
    colab_url = "https://colab.research.google.com/drive/1cmisyC4I9eNpHGGnPqzu3MNykCCuJKSk"
    try:
        requests.get(colab_url)
        return "✅ Colab pinged!"
    except Exception as e:
        return f"❌ Error: {e}"
