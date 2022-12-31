from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':12,'b':63,'c':54}
    return render(request,'operations.html',d)