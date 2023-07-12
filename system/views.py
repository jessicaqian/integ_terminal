from django.shortcuts import render
from .forms import MeetcontrolForm
from django.http import JsonResponse
import requests
import json


# Create your views here.
def main(request):
    if request.method == 'POST':
        pass


    else:

        return render(request, 'system/main.html')

def meet(request):
    if request.method == 'POST':
        pass


    else:
        form = MeetcontrolForm()

        return render(request, 'system/meet.html', {'form': form})

def audioConfig(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/audioconfig.html', {})

def videoConfig(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/videoconfig.html', {})

def meetControl(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/meetcontrol.html', {})

def netconfig(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/netconfig.html', {})

def uiDisplay(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/UIdisplay.html', {})

def test(request):
    if request.method == 'POST':
        data = request.POST['IntegratedTerminal']
        val = json.loads(data)

        print(val['method'])
        print(val['data']['message'])
        return JsonResponse({'code': 200})
    else:

        try:
            url = 'http://10.25.16.9:8090'
            payload = {'method':'double auth','data':{'port':8090,'ip':'10.25.16.9','pin':'123456'}}
            res = requests.post(url,data=json.dumps(payload))
            print(res)
        except Exception as e:
            print(e)
        return JsonResponse({'code': 200})