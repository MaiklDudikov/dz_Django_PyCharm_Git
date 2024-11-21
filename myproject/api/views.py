from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import random


class PredictionView(APIView):
    def get(self, request):
        predictions = [
            "Сегодня твой день!",
            "Удача на твоей стороне.",
            "Ты встретишь старого друга.",
            "Будь осторожен с новыми знакомствами.",
            "Завтра принесет новые возможности.",
        ]
        prediction = random.choice(predictions)
        return Response({"prediction": prediction})


@api_view(['GET'])
def random_number(request):
    return Response({"number": random.randint(1, 100)})


@api_view(['GET'])
def random_number_in_range(request):
    min_num = int(request.query_params.get('min', 0))
    max_num = int(request.query_params.get('max', 15))
    return Response({"number": random.randint(min_num, max_num)})


@api_view(['GET'])
def random_number_set(request):
    count = int(request.query_params.get('count', 5))
    numbers = [random.randint(1, 100) for _ in range(count)]
    return Response({"numbers": numbers})


# Задание 3
poems = {
    "love": [
        {"title": "Любовь", "author": "Пушкин", "text": "Я вас любил..."},
        {"title": "Мгновенье", "author": "Тютчев", "text": "О как убийственно мы любим..."},
    ],
    "life": [
        {"title": "Жизнь", "author": "Лермонтов", "text": "Как часто, пёстрою толпою окружён..."},
        {"title": "Судьба", "author": "Блок", "text": "В те дни, когда мне были новы..."},
    ],
}


@api_view(['GET'])
def random_poem(request):
    category = random.choice(list(poems.keys()))
    poem = random.choice(poems[category])
    return Response(poem)


@api_view(['GET'])
def random_poem_by_author(request):
    author = request.query_params.get('author', 'Пушкин')
    author_poems = [poem for poems_list in poems.values() for poem in poems_list if poem["author"] == author]
    return Response(random.choice(author_poems) if author_poems else {"error": "Автор не найден"})


@api_view(['GET'])
def random_poem_by_theme(request):
    theme = request.query_params.get('theme', 'love')
    theme_poems = poems.get(theme, [])
    return Response(random.choice(theme_poems) if theme_poems else {"error": "Тематика не найдена"})


# Задание 4
@api_view(['GET'])
def list_poems_by_author(request):
    author = request.query_params.get('author', 'Пушкин')
    author_poems = [poem["title"] for poems_list in poems.values() for poem in poems_list if poem["author"] == author]
    return Response({"titles": author_poems})


@api_view(['GET'])
def list_authors(request):
    authors = list({poem["author"] for poems_list in poems.values() for poem in poems_list})
    return Response({"authors": authors})


@api_view(['GET'])
def list_themes(request):
    themes = list(poems.keys())
    return Response({"themes": themes})


@api_view(['GET'])
def list_poems_by_theme(request):
    theme = request.query_params.get('theme', 'love')
    theme_poems = [poem["title"] for poem in poems.get(theme, [])]
    return Response({"titles": theme_poems})
