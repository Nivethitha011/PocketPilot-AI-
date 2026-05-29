from flask import Flask, render_template, request, redirect, session
import threading
import webbrowser

app = Flask(__name__)
app.secret_key = "pocketmoney_secret"


# =========================
# AUTO OPEN BROWSER
# =========================
def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


# =========================
# LOADING PAGE
# =========================
@app.route("/")
def loading():
    return render_template("loading.html")


# =========================
# WELCOME PAGE
# =========================
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# =========================
# PARENT LOGIN
# Username = anything
# Password = 1234
# =========================
@app.route("/parent-login", methods=["GET", "POST"])
def parent_login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if password == "1234":
            session["user"] = username
            session["role"] = "parent"
            return redirect("/parent-dashboard")
        else:
            error = "Wrong Password"

    return render_template("parent_login.html", error=error)


# =========================
# CHILD LOGIN
# Username = anything
# Password = 6789
# =========================
@app.route("/child-login", methods=["GET", "POST"])
def child_login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if password == "6789":
            session["user"] = username
            session["role"] = "child"
            return redirect("/child-dashboard")
        else:
            error = "Wrong Password"

    return render_template("child_login.html", error=error)


# =========================
# PARENT DASHBOARD
# =========================
@app.route("/parent-dashboard")
def parent_dashboard():

    if "role" not in session:
        return redirect("/parent-login")

    data = {
        "allowance": 10000,
        "spent": 3500,
        "remaining": 6500,
        "transactions": [
            {"cat": "Food", "amt": 500},
            {"cat": "Books", "amt": 1200},
            {"cat": "Transport", "amt": 800},
            {"cat": "Entertainment", "amt": 1000}
        ],
        "badges": [
            "🏆 Gold Badge",
            "🔥 7 Day Streak",
            "💰 Smart Saver"
        ]
    }

    return render_template(
        "parent_dashboard.html",
        data=data
    )


# =========================
# CHILD DASHBOARD
# =========================
@app.route("/child-dashboard")
def child_dashboard():

    if "role" not in session:
        return redirect("/child-login")

    data = {
        "allowance": 10000,
        "spent": 3500,
        "remaining": 6500,
        "streaks": [
            "🔥 7 Day Streak"
        ],
        "badges": [
            "🏆 Gold Badge",
            "💰 Smart Saver"
        ]
    }

    return render_template(
        "child_dashboard.html",
        data=data
    )


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/welcome")


# =========================
# START APP
# =========================
if __name__ == "__main__":

    threading.Timer(1.5, open_browser).start()

    app.run(debug=True)