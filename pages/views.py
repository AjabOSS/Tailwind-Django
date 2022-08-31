from django.shortcuts import render

def index(request):
    text = "Hello World"
    context  = {
        "c_text": text
    }
    return render(request, 'index.html', context)
