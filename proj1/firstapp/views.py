from django.shortcuts import render

#create your views here.
def fun1(request):
    dct = {"name":[1,2,3,4,5],"emp":"ojas"}

    return render(request,"firstapp/first.html",context=dct)

def fun2(request):
    return render(request,"second.html")
