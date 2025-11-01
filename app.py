from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = "data.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        # Get the six values from the form
        values = [request.form.get(f"value{i}", "").strip() for i in range(1, 7)]

        # Ensure all values are filled
        if all(values):
            # Create a timestamped line
            line = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | " + ", ".join(values) + "\n"
            
            # Save to text file on the server
            with open(DATA_FILE, "a", encoding="utf-8") as f:
                f.write(line)

            message = "✅ Values saved successfully!"
        else:
            message = "⚠️ Please fill in all 6 values."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    # Make sure the file exists
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

    app.run(debug=True, port=5000)
