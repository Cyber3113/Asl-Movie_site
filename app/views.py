from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.forms import AuthenticationForm


def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    video_types = Video_type.objects.all()
    videos = Video.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        videos = videos.filter(video_name__icontains=search_query)

    type_id = request.GET.get('type', None)
    if type_id:
        videos = videos.filter(type_id=type_id)

    return render(request, 'index.html', {
        'video_types': video_types,
        'videos': videos
    })


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video_detail.html', {'video': video})

