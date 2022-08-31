from django.http import JsonResponse
from .models import FoodCategory, FoodListSerializer


def api_view(request):
    qs = FoodCategory.objects.filter(food__is_publish=True).distinct()
    serialazer = FoodListSerializer(qs, many=True)

    food_list = {
        'foods': [data for data in serialazer.data if len(data['foods']) > 0]
    }

    return JsonResponse(food_list)
