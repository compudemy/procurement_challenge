from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')


def success_view(request):
    return render(request, 'frontend/success.html')  # Create a success template
