from django.shortcuts import render

# Create your views here.



def start(request):
    return render(request, "index1.html")

def catalog(request):
    return render(request, "catalogue1.html")

def soft_toys(request):
	return render(request, "soft_toys.html")

def cart(request):
	return render(request, "cart1.html")

def toy(request):
	return render(request, "toy.html")