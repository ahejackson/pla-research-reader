from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/pokemon')
def pokemon():
    return { 'pokemon': [] }