from flask import render_template
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')  # Ensure this template exists in your templates folder

if __name__ == '__main__':
    app.run(debug=True)
