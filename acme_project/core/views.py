# core/views.py
from django.shortcuts import render

def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию;
    # выводить её в шаблон пользовательской страницы 404 мы не станем.
    return render(request, 'core/404.html', status=404)

def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)

def response_forbidden(request, exception):
    return render(request, 'core/403.html', status=403)

def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)
