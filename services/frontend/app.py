from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>FutureCars</h1>
    <p>Welcome to FutureCars — Premium Electric & Luxury Vehicles</p>

    <h2>Featured Cars</h2>
    <ul>
        <li>Tesla Model S</li>
        <li>BMW i7</li>
        <li>Mercedes 2055</li>
        <li>Porsche Taycan</li>
    </ul>

    <h2>About Us</h2>
    <p>FutureCars is a modern digital car marketplace powered by a cloud-native GitOps platform.</p>

    <h2>Contact</h2>
    <p>Email: info@futurecars.com</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)