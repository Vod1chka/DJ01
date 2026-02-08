from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home.html')


def data_view(request):
    return render(request, 'pages/data.html')


def test_view(request):
    return render(request, 'pages/test.html')
