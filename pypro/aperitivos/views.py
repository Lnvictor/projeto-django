from django.shortcuts import render

# Create your views here.


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 410376813},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 251497668}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

