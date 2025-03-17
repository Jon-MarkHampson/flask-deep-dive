from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route('/')
def index():
    time_str = datetime.now().strftime("%H:%M:%S")

    # Retrieve the 'name' parameter; default to 'Alice' if not provided
    user_name = request.args.get('name', 'Alice')

    return render_template('index.html', title='Home', user=user_name, time=time_str)


@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5001)