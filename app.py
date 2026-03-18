# Task 1:  To build a simple Flask application using basic HTML and css

# Requirements:
# * The application should have two routes: "/" ( home page ) and "/about" ( about page ).

# * Bth routes should display the content exactly as shown in the images shared.

# Project Structure:
# * Add the routes in "app.py".
# * Place the HTML files inside the "templates" folder.
# * Create "css" and "js" folders inside the "static" directory and keep the respective files there.

# Try to implement this small project and follow the structure mentioned above.


from datetime import datetime
from doctest import debug
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.utcnow().year}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        # Here you can process the feedback, e.g., save it to a database or file
        print(f"Received feedback: {feedback}")
        return redirect(url_for('home'))  # Redirect to home after processing feedback
    return render_template('add_feedback.html')


if __name__ == '__main__':
    # Run with: python app.py
    app.run(port=5000, debug=True)