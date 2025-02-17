from django.shortcuts import render
from .models import AnimeVideo
def anime_list(request):
    videos = AnimeVideo.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
