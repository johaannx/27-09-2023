from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (replace with your authentication logic)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "johann", "password": "johann123"},
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            # Successful login, redirect to the dashboard or home page
            return redirect(url_for("dashboard"))

    # If login fails, return to the login page with an error message
    return render_template("index.html", error="Invalid username or password")


@app.route("/dashboard")
def dashboard():
    return "Welcome to your dashboard!"


if __name__ == "__main__":
    app.run(debug=True)
