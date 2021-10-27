from flask import Flask,render_template

app=Flask(__name__,template_folder='../vista',static_folder='../static')

@app.route('/')
def inicio():
    return render_template('comunes/index.html')

