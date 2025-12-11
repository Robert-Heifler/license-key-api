from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Your 100 pre-generated license keys
KEYS = [
    "WC7X3-12347",
    "WC7X3-89562",
    "WC7X3-45679",
    "WC7X3-23450",
    "WC7X3-67893",
    # Add 95 more keys here using the VBA generator
]

@app.route('/')
def home():
    return "License Key API - Running"

@app.route('/get-key')
def get_key():
    key = random.choice(KEYS)
    return jsonify({"key": key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
```

- Scroll down, click **"Commit new file"**

---

**4. Add the second file - requirements.txt:**
- Click **"Add file"** → **"Create new file"**
- Filename: `requirements.txt`
- Paste this:
```
Flask==3.0.0
flask-cors==4.0.0
gunicorn==21.2.0
