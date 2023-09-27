from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (replace with your authentication logic)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "johann", "password": "johann123"},
]

# Initialize error message as None
error_message = None


@app.route("/")
def index():
    # Pass the error message to the template if it exists
    return render_template("index.html", error=error_message)


@app.route("/login", methods=["POST"])
def login():
    global error_message  # Use a global variable to store the error message
    username = request.form.get("username")
    password = request.form.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            # Successful login, reset error_message and redirect to the dashboard or home page
            error_message = None
            return redirect(url_for("dashboard"))

    # If login fails, set the error_message and return to the login page
    error_message = "Invalid username or password"
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
