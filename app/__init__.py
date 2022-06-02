import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/travels')
def travels():
    return render_template('travels.html', title="Oh, the places I've Been!", url=os.getenv("URL"))

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Get in Touch!", url=os.getenv("URL"))