## Задание
Создайте  HTML-шаблон (файл base.html).

Создайте страницы 1.html и 2.html, которые будут расширять шаблон и заполнять его контентом.

## Выполнение
У нас есть три страницы: index.html, contact.html и blog.html. Они отличаются только контентом,у них одинаковая навигационная панель
и футер. 
1. Создаем HTML -шаблон base.html.Копируем всю повторяющуюся часть (меню и футер) из index.html, contact.html и blog.html.
Вставляем в base.html.
2. Создаём блок внутри тега <title>. Здесь будет находиться название.
 <title>

    {% block title %}

    {% endblock %}

  </title>

Создаём блок для контента. Делаем это после меню, перед футером.
В блоки будет вставляться информация, которая не повторяется

{% block content %}
    
{% endblock %}

Из файлов index.html, contact.html и blog.html. удаляем все повторяющиеся части кода
* В начале index.html, contact.html и blog.html.пишем указание на использование шаблона:

{% extends 'base.html' %}

{% block title %}
    
{% endblock %}

в base. html 
указываем использование шаблона для контента:

{% block content %}

    # здесь уже написанный контент, который не повторяется

{% endblock %}


