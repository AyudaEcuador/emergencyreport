from django.shortcuts import render, HttpResponse, render_to_response

# Create your views here.
def landing(request):
    return render(request, 'landing/home.html', {})


