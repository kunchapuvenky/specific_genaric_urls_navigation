from django.shortcuts import render

# Create your views here.
def lohi(request):
    return render(request,'lohi.html')