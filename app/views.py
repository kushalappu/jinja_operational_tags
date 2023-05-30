from django.shortcuts import render

# Create your views here.
def home(request):
    d={'a':18}
    return render(request,'home.html',context=d)
