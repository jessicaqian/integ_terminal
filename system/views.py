from django.shortcuts import render
from .forms import MeetForm,MeetParameterForm,NetConfigForm,UIdisplayForm
from django.http import JsonResponse
import requests
import json
import datetime



# Create your views here.

status_dict = {
    'usb':'none',

}



def main(request):
    if request.method == 'POST':
        pass


    else:

        return render(request, 'system/main.html')

def meet(request):
    if request.method == 'POST':
        pass


    else:
        form = MeetForm()

        return render(request, 'system/meet.html', {'form': form})



def meetControl(request):
    if request.method == 'POST':
        pass

    else:
        form = MeetParameterForm()

        return render(request, 'system/meetcontrol.html', {'form': form})

def netconfig(request):
    if request.method == 'POST':
        pass

    else:
        form = NetConfigForm()

        return render(request, 'system/netconfig.html', {'form': form})

def uiDisplay(request):
    if request.method == 'POST':
        pass

    else:
        form = UIdisplayForm()

        return render(request, 'system/UIdisplay.html', {'form': form})

def time(request):
    if request.method == 'POST':
        pass

    else:
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%dT%H:%M:%S")
        print(time)

        return render(request, 'system/time.html', {'time':time})

def secure(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/secure.html', {})

def version(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/version.html', {})

def log(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/log.html', {})

def interfaceControl(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/interfaceControl.html', {})

def sysdiagnosis(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/sysdiagnosis.html', {})


def sysUpdate(request):
    if request.method == 'POST':
        pass

    else:

        return render(request, 'system/sysupdate.html', {})


def notify(request):
    if request.method == 'POST':
        # data = request.POST['IntegratedTerminal']
        data = request.body
        print(data)
        val = json.loads(data)

        # print(val['method'])
        # print(val['data']['message'])

        status_dict['usb'] = val['method']
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

def checkStatus(request):

    return JsonResponse({'msg': status_dict['usb']})

