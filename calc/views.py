from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'name':'mitul',
    }
    return render(request, 'home.html',context)

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    try:
        res = float(val1) + float(val2)
    except:
        res = 'please enter ineteger or float value'
    return render(request,'result.html',{'res':res})