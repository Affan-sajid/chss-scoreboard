from django.http import JsonResponse
from django.shortcuts import render
from .models import Score

# import datetime
# from django.utils import timezone

# Create your views here.
def scoreboard(request):
    return render(request, 'index.html')


def get_scores(request):
    scores = Score.objects.latest('last_updated')
    data = {

        
        "Red"    : scores.Red,
        "Orange" : scores.Orange,
        "Yellow" : scores.Yellow,
        "Green"  : scores.Green,
        "Blue"   : scores.Blue,       
        
        'last_updated': scores.last_updated.strftime('%Y-%m-%d %H:%M:%S')
    }
    return JsonResponse(data)
