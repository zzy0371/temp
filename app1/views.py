from django.shortcuts import render
from .models import MessageInfo
# Create your views here.
from django.http import HttpResponse
def index(req):
    if req.method == "GET":
        return render(req,"index.html")
    else:
        m = MessageInfo()
        m.info = req.POST.get("info")
        m.img = req.FILES.get("head")
        m.file = req.FILES.get("file")
        m.save()
        return HttpResponse("成功")