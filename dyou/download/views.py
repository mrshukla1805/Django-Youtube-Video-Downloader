from django.shortcuts import render
from pytube import Youtube
# Create your views here.

def down(request):
    return render(request,'down.html')
    

def yt_down(request):
    link = request.GET.get('link', False)
    obj = Youtube(link)
    res=[]
    stream = obj.stream_all()
    for i in stream:
        res.append(i.resolution)
    print(res)
    return render(request, "yt_down.html")  