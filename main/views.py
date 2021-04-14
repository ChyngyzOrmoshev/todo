from django.shortcuts import render, HttpResponse

def homepage (request):
    return HttpResponse('Это мая первая страница на Django')

def test(request):
    return render(request, 'test.html')

def go(request):
    return render(request, 'go.html')
