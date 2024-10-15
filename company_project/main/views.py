from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def news(request, extra=None):
    return render(request, 'main/news.html')


def management(request, extra=None):
    return render(request, 'main/management.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def branches(request, branch=None):
    if branch == 'London':
        return render(request, 'main/branches_london.html')
    elif branch == 'Paris':
        return render(request, 'main/branches_paris.html')
    else:
        return render(request, 'main/branches.html')
