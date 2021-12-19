from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'msg': 'こんにちは、世界！'

    }
    return render(request, 'main/index.html', context)
