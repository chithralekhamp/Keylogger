from flask import Flask, render_template
import os

app = Flask(__name__)
LOG_PATH = "research_logs.txt"

@app.route('/')
def index():
    # Read the log file if it exists
    logs = ""
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            logs = f.read()
    
    return render_template('index.html', logs=logs)

if __name__ == "__main__":
    app.run(debug=True)