from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    context = {
        'question': 'Дубровники',
        'active_page': 'home',
        'css_file': 'index.css'  # Указываем css для главной страницы
    }
    return render_template("index.html", **context)


@app.route('/blog/')
def blog():
    context = {
        'question': 'Хорватия и Черногория',
        'active_page': 'blog',
        'css_file': 'blog.css'  # Указываем css для блога
    }
    return render_template("blog.html", **context)


@app.route('/contacts/')
def contacts():
    context = {
        'question': 'Контакты',
        'active_page': 'contacts',
        'css_file': 'contact.css'  # Указываем css для страницы контактов
    }
    return render_template("contact.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
