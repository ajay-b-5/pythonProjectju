from django.shortcuts import render

def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')

def dash(request):
    return render(request,'dash.html')

def views_data(request):
    return render (request,'views_data')
