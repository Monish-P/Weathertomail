from django.shortcuts import render,HttpResponse
import json
import urllib.request
from .models import User
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
    return render(request,'core/home.html')
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        user = User.objects.create(name=name,email=email,city=city)
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=1981e011069b0c3d9df7d41cee425929').read()
        list_of_data = json.loads(source)
        kelvin = list_of_data['main']['temp']
        temp =  str(kelvin) + 'k'
        subject = 'Hi '+name+', interested in our services'
        celcius = int(kelvin-273.15)
        if celcius in range(-10,6):
            emoji = '🥶'
        elif celcius in range(6,17):
            emoji = '🆒'
        elif celcius in range(18,30):
            emoji = '😊'
        elif celcius in range(31,51):
            emoji = '🔥'
        else:
            emoji = '🥵'
        message = 'The temperature in '+city+' is '+temp+' '+emoji
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        reciever_email = EmailMessage(
            subject,
            message,
            email_from,
            recipient_list
        )
        reciever_email.fail_silently = False
        reciever_email.send()
        return HttpResponse('The weather details have been sent, Check your mail! Thank you🤗')
