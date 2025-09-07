from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials
USER = {"email": "test@example.com", "password": "1234"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == USER["email"] and password == USER["password"]:
            # Just redirect to dashboard, no session
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials. Try again."

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    # No session check, always accessible
    return render_template("dashboard.html", username=USER["email"])

@app.route("/logout")
def logout():
    # Just redirect back to index
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
