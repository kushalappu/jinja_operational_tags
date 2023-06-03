from django.shortcuts import render

# Create your views here.
def home(request):
    d={'a':18}
    return render(request,'home.html',context=d)

def hii(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'hii.html',context=d)


def loop(request):
    d={'name':'akash sede'}
    return render(request,'loop.html',context=d)
