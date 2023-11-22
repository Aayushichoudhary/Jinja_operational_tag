from django.shortcuts import render

# Create your views here.

def ifoperation(request):
    d={'a':1000, 'b':200}
    return render(request,'if.html', context=d)

def ifelseoperation(request):
    dict={'a':1000, 'b':200}
    return render(request,'ifelse.html', context=dict)

def ifelifoperation(request):
    dict1={'a':100, 'b':200, 'c':300}
    return render(request,'ifelif.html', context=dict1)

def nestedifoperation(request):
    dict2={'a':1000, 'b':200, 'c':300}
    return render(request,'nestedif.html', context=dict2)