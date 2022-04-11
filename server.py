import random

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'pineapple'

@app.route('/')
def identify():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    return render_template('index.html', hidden1='')

@app.route('/guess', methods=['post'])
def check_guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/again')
def again():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)