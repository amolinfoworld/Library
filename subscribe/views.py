from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import Subscribe
# Create your views here.
#s=Subscribe()


#from Library.settings import EMAIL_HOST_USER
from django.conf import settings

from . import forms
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):
    #print("in subscribe email method")
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to Library App'
        message1 = 'Thank You Using App...recent transactions as follow:'
        #rec=request.POST["email"].strip()
        #recepient = str(sub['email'].value())
        recepient=request.POST["email"].strip()
        final_recepient_list=None
        if ";" in recepient:
            final_recepient_list=recepient.split(";")
        else:
            final_recepient_list=[recepient]
        print(final_recepient_list)

        if final_recepient_list:
                send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
        #return HttpResponse("Thank  you...Checkout Your InBox/Spam")
        return render(request, 'success.html', {'recepient': final_recepient_list})
    return render(request, 'index.html',context={'form1':sub})
