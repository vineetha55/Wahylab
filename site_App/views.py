from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about_us(request):
    return render(request,"about-us.html")

def internships(request):
    return render(request,"internships.html")

def services(request):
    return render(request,"services.html")

def portfolio(request):
    return render(request,"portfolio.html")


def career(request):
    return render(request,"career.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")