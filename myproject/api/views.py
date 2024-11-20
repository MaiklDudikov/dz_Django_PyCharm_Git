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
