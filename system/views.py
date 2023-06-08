from django.shortcuts import render
from .forms import MeetcontrolForm

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