from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Sample user data (replace with your authentication logic)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "johann", "password": "johann123"},
]

# Initialize error message and username as None
error_message = None
username = None


@app.route("/")
def index():
    # Pass the error message to the template if it exists
    return render_template("index.html", error=error_message)


@app.route("/login", methods=["POST"])
def login():
    global error_message, username  # Use global variables for error message and username
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
    global username  # Use the global username variable
    sus_instance = 0  # Initialize sus_instance to 0

    # Read the CSV file
    try:
        df = pd.read_csv("comments_cleaned.csv")
        # Count the occurrences of "suicide" and "SUICIDE" in the "comment" column (case-insensitive)
        sus_instance += df["comment"].str.contains("suicide", case=False).sum()
        sus_instance += df["comment"].str.contains("kill", case=False).sum()
        sus_instance += df["comment"].str.contains("slaughter", case=False).sum()
        print(sus_instance)
    except Exception as e:
        # Handle any exceptions that may occur while reading the CSV file
        print(f"Error reading CSV file: {str(e)}")

    return render_template("dashboard.html", username=username, sus_instance=sus_instance)



if __name__ == "__main__":
    app.run(debug=True)
