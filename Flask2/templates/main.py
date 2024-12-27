from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/blog.html')
def blog():
    return render_template('/blog.html')

@app.route('/contacts.html')
def contacts():
    return render_template('/contacts.html')

if __name__ == '__main__':
    app.run(debug=True)