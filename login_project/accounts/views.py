from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime, timedelta


def list_task(request):
    return render(request, 'accounts/list_task.html')


# Пример базы данных пользователей
users = {
    'admin': {'password': 'admin123', 'role': 'Администратор'},
    'user1': {'password': 'user123', 'role': 'Пользователь'}
}


def login_view(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = users.get(username)
        if user and user['password'] == password:
            message = f"Добро пожаловать, {username}! Ваш уровень доступа : {user['role']}."
        else:
            message = "Неправильный логин или пароль, или нет базы данных, нет супер-пользователя в admin Django"
    return render(request, 'accounts/login.html', {'message': message})


def calculate_view(request):
    result = None
    if request.method == 'POST':
        numbers = request.POST.get('numbers')
        if numbers:
            numbers = list(map(float, numbers.split()))
            operation = request.POST.get('operation')
            if operation == 'min':
                result = min(numbers)
            elif operation == 'max':
                result = max(numbers)
            elif operation == 'avg':
                result = sum(numbers) / len(numbers)
    return render(request, 'accounts/calculate.html', {'result': result})


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        subscribe = 'Да' if request.POST.get('subscribe') else 'Нет'
        return render(request, 'accounts/registration_result.html', {
            'name': name,
            'surname': surname,
            'age': age,
            'email': email,
            'gender': gender,
            'address': address,
            'subscribe': subscribe,
        })
    return render(request, 'accounts/register.html')


def programmer_day_view(request):
    date_result = ''
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        date = datetime(year, 1, 1) + timedelta(days=255)
        date_result = date.strftime('%d %B (%A)')
    return render(request, 'accounts/programmer_day.html', {'date_result': date_result})
