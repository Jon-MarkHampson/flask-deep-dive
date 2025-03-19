import json
from flask import Flask, render_template, request
from datetime import datetime

USERS_PATH = "users.json"

app = Flask(__name__)

with open(USERS_PATH, 'r') as handle:
    users = json.load(handle)

time_str = datetime.now().strftime("%H:%M")


# @app.route('/')
# def home():
#     return "Hello, World! 🌍"


@app.route('/greet/<name>')
def greet(name):
    return render_template('index.html', title='Home', user=name, time=time_str)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # The variable 'post_id' is an integer.
    return f"Post {post_id}"

@app.route('/')
def index():
    # Retrieve the 'name' parameter; default to 'Alice' if not provided
    user_name = request.args.get('name', 'Alice')

    return render_template('index.html', user=user_name, time=time_str)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/all-users')
def all_users():
    return render_template('all-users.html', users=users)

@app.route('/update_email', methods=['POST'])
def update_profile():
    username = request.form['username']
    email = request.form['email']

    # Check if the user exists
    if username in users:
        users[username]["email"] = email

        # Write the updated users dictionary back to the JSON file
        with open(USERS_PATH, 'w') as handle:
            json.dump(users, handle, indent=4)

        return f"Updated profile of {username} with email {email}"
    else:
        return f"User {username} not found", 404

@app.route('/update_email_form')
def update_profile_form():
    return render_template('update_email_form.html')

@app.route('/update_country', methods=['POST'])
def update_country():
    username = request.form['username']
    country = request.form['country']

    # Check if the user exists
    if username in users:
        users[username]["country"] = country

        # Write the updated users dictionary back to the JSON file
        with open(USERS_PATH, 'w') as handle:
            json.dump(users, handle, indent=4)

    return f"Updating profile of {username} with country {country}"

@app.route('/update_country_form')
def update_country_form():
    return render_template('update_country_form.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5001, debug=False)
