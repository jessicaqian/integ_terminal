from django.shortcuts import render

# Create your views here.
def main(request):
    if request.method == 'POST':
        pass


    else:

        return render(request, 'system/main.html', {})

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

