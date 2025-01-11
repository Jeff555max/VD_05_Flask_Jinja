from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    context = {
        'question': 'Дубровники',
        'active_page': 'home'
    }
    return render_template("index.html", **context) #распаковываем словарь и пробрасываем наши переменные

@app.route('/blog/')
def blog():
    context = {
        'question': 'Хорватия и Черногория',
        'active_page': 'blog'
    }
    return render_template("blog.html", **context) #распаковываем словарь и пробрасываем наши переменные)

@app.route('/contacts/')
def contacts():
    context = {
        'question': 'Контакты',
        'active_page': 'contacts'
    }
    return render_template("contact.html", **context) #распаковываем словарь и пробрасываем наши переменные)

if __name__ == '__main__':
    app.run(debug=True)
