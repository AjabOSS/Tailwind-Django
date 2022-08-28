from django.shortcuts import render

def index(request):
    text = "hello"
    context  = {
        "c_text": text
    }
    return render(request, 'index.html', context)
