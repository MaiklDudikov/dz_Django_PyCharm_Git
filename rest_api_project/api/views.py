from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from rest_framework.decorators import api_view


class ServerTimeView(APIView):
    def get(self, request):
        now = datetime.datetime.now()
        data = {
            "current_time": now.strftime("%H:%M:%S"),
            "current_date": now.strftime("%Y-%m-%d"),
            "current_weekday": now.strftime("%A"),
        }
        return Response(data)


class GreetingView(APIView):
    def get(self, request):
        now = datetime.datetime.now()
        hour = now.hour

        if 5 <= hour < 12:
            greeting = "Доброе утро"
        elif 12 <= hour < 18:
            greeting = "Добрый день"
        elif 18 <= hour < 23:
            greeting = "Добрый вечер"
        else:
            greeting = "Доброй ночи"

        return Response({"greeting": greeting})


# http://127.0.0.1:8000/arithmetic/?num1=5&num2=10
@api_view(['GET'])
def arithmetic_operations(request):
    num1 = float(request.query_params.get('num1', 0))
    num2 = float(request.query_params.get('num2', 0))
    data = {
        "multiplication": num1 * num2,
        "addition": num1 + num2,
        "average": (num1 + num2) / 2,
        "minimum": min(num1, num2),
        "maximum": max(num1, num2),
    }
    return Response(data)


# http://127.0.0.1:8000/power/?base=2&exponent=3
@api_view(['GET'])
def power_operation(request):
    base = float(request.query_params.get('base', 1))
    exponent = float(request.query_params.get('exponent', 1))
    result = base ** exponent
    return Response({"base": base, "exponent": exponent, "result": result})
