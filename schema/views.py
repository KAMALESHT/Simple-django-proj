from django.shortcuts import render

from schema.models import disptable

def showtable(request):
    if request.method=="POST":

        res = disptable.objects.all()[:int(request.POST.get("showrecords"))]
        return render(request,"index.html",{"show":res})
    else:
        res = disptable.objects.all()
        return render(request,"index.html",{"show":res})