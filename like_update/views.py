from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Count
from django.views.decorators.csrf import csrf_exempt


def like_dislike_view(request):
    count = Count.objects.get(id=1)
    return render(request, 'like_dislike.html', {'count': count})


@csrf_exempt
def update_count(request):
    if request.method == 'POST':
        count = Count.objects.get(id=1)
        count.update_count(request.POST.get('like') == "true")
        return JsonResponse({'likes': count.likes, 'dislikes': count.dislikes})
