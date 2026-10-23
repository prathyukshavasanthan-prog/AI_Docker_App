from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    numbers = np.array([10, 20, 30, 40, 50])
    average = np.mean(numbers)

    return f"""
    <h1>AI Application Running Successfully!</h1>
    <h2>Docker Container is Working!</h2>
    <p>Average of {numbers.tolist()} = <b>{average}</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
