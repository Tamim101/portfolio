from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import blog, about, portfilio
from portfolio_pink.settings import EMAIL_HOST_USER


def home(request):
    object = about.objects.all()
    return render(request,'index.html',{'object':object})


def details(request):
    obj = portfilio.objects.all()
    return  render(request,'portfolio-details.html',{'obj':obj})




class send_email(APIView):
    def post(self , request):
        name = request.POST['name']
        email = request.POST['email']
        note = request.POST['note']
        print('note')
        if name and email and note:
            print(note , name , email)
            print('email')
            email = send_mail('from : {}'.format(email) , 'Hey, it\'s {} '.format(name) + note ,
                              EMAIL_HOST_USER , ['tamimkhan7133@.com' , ] , fail_silently=False)

            return Response({'success': True , 'message': 'Thanks for contacting us, will get back to you soon.' , 'email': email})

        else:
            return Response({'success': False , 'message': 'Please fill all the information.'})

