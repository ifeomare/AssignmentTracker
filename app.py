from flask import Flask, render_template, request
from markupsafe import escape
# from flask import url_for

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        un=request.form.get('username')
        pw=request.form['password']
        print(un,pw)
    return render_template('login.html')

# @app.route("/create-account")
# def create_account():
#     return "This is the new account page"

# @app.route("/<username>/dashboard")
# def dashboard(username):
#     return "This is the dashboard"

# @app.route("/<username>/assignment-tracker")
# def assignment_tracker(username):
#     return "This is the Assignment Tracker page"

# @app.route("/<username>/calendar")
# def calendar(username):
#     return "This is this month's calendar"

# with app.test_request_context():
#     print(url_for('static', filename='login.css'))
#     print(url_for('login'))
#     print(url_for('create_account'))
#     print(url_for('dashboard', username='sinclair'))
#     print(url_for('assignment_tracker', username='sinclair'))
#     print(url_for('calendar', username='sinclair'))

# if __name__ == "__main__":
    # app.run(debug=True)