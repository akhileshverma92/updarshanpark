from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutpage(request):
    # return HttpResponse("about page")
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")

def monuments(request):
    return render(request,"monuments.html")

def gallery(request):
    return render(request,"gallery.html")
