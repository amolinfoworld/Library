from datetime import date

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


from Book.models import Book

# Create your views here.

def  home(request):   #function based view
    #print(request.method)     #------get function
    # print("In home function...")
    # return HttpResponse("<h1>Hi welcome to home page of project</h1>")
    #return JsonResponse({"key": "Value"})
    return render(request, "base.html")



def homepage(request):   #by default return none
    if request.method=="POST":
        data=request.POST
        if not data.get("id"):
    # 'nm': ['yearbook'], 'qty': ['23'], 'price': ['213'], 'ispub': ['Yes']}>
            if data["ispub"]=="Yes":
                Book.object.create(name=data["nm"],
                qnty=data["qnty"],
                price=data["price"],
                is_published=True,
                published_date=date.today())
            elif data["ispub"]=="No":
                Book.object.create(name=data["nm"],
                qnty=data["qnty"],
                price=data["price"],
                is_published=False)

            return redirect("home")
        
        else:
            bid=data.get("id")
            b_obj=Book.object.get(id=bid)
            b_obj.name=data["nm"]
            b_obj.qnty=data["qnty"]
            b_obj.price=data["price"]

            if data["ispub"]=="Yes":
                if b_obj.is_published:
                    pass
                else:
                    b_obj.is_published=True
                    b_obj.published_date=date.today()

            elif data["ispub"]=="No":
                if b_obj.is_published==True:
                    pass
                else:
                    b_obj.is_published=False
                    b_obj.published_date=None


            b_obj.save()
            return render(request, template_name="home.html")

        #print(request.POST)
    #return HttpResponse("<h1>Hi welcome to home page of project</h1>")
    else:
        return render(request, template_name="home.html")


def get_books(request):
    books=Book.object.all()
    return render(request,template_name="books.html",context={"all_books":books})    

def delete_book(request,id):
    #print(id,"deleted book")
    # subject1 = 'Welcome to Library App'
    # message1 = 'Thank You For Using App...recent transactions as follow'
    # final_recepient_list=["amol.londhe20@gmail.com","cloudtech321@gmail.com"]
    # send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    Book.object.get(id=id).delete()
    subject1 = 'Welcome to Library App'
    message1 = f'''
    Dear User Thank You For Using Library App...recent transactions as follow:
    Book Details with {id} Deleted succesfully from database'''
    final_recepient_list=["amol.londhe20@gmail.com","londheamol474@gmail.com"]
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    return redirect("show_book")

def update_book(request,id):
    #print(id,"deleted book")
    b_obj=Book.object.get(id=id)
    subject1 = 'Welcome to Library App'
    result=''
    result=result=f'''
    ----------------Updated Details of Book as follows-------------------------------
        Book Id-->{b_obj.id}
        Book Name-->{b_obj.name}
        Book Quantity-->{b_obj.qnty}
        Book Price-->{b_obj.price}  
        ---------------------------------------------------
        '''
    message1 = f'''
    Dear User Thank You For Using Library App...recent transactions as follow:
    Book Details with {id} updated succesfully'''+result
    final_recepient_list=["amol.londhe20@gmail.com","londheamol474@gmail.com"]
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    return render(request,"home.html",context={"single_book":b_obj})

def soft_delete(request,id):
    b_obj=Book.object.get(id=id)
    subject1 = 'Welcome to Library App'
    message1 = f'''
    Dear User Thank You For Using Library App...recent transactions as follow:
    Book Details with {id} soft deleted succesfully'''
    final_recepient_list=["amol.londhe20@gmail.com","londheamol474@gmail.com"]
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    b_obj.is_deleted="Y"
    b_obj.save()
    return redirect("show_book")

def rrr_books(request,id):
    b_obj=Book.object.get(id=id)
    b_obj.is_deleted="N"
    b_obj.save()
    return redirect("show_book")

def active_books(request):
    #all_active_books=Book.objects.filter(is_deleted="N")
    all_active_books=Book.active_books.all()
    result=''
    for i in all_active_books:
        result=result + f'''
        -----------------------------------------------
        Book Id-->{i.id}
        Book Name-->{i.name}
        Book Quantity-->{i.qnty}
        Book Price-->{i.price}  
        ---------------------------------------------------
        '''
    subject1 = 'Welcome to Library App'
    message1 = f'''
    Dear User Thank You For Using Library App...recent transactions as follow:
    Active Books as Follows
    '''+ result
    final_recepient_list=["amol.londhe20@gmail.com","londheamol474@gmail.com"]
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    return render(request,template_name="books.html",context={"all_books":all_active_books})

def in_active_books(request):
    #all_in_active_books=Book.objects.filter(is_deleted="Y")
    all_in_active_books=Book.in_active_books.all()
    result=''
    for i in all_in_active_books:
        result=result + f'''
        -----------------------------------------------
        Book Id-->{i.id}
        Book Name-->{i.name}
        Book Quantity-->{i.qnty}
        Book Price-->{i.price}  
        ---------------------------------------------------
        '''
    subject1 = 'Welcome to Library App'
    message1 = f'''
    Dear User Thank You For Using Library App...recent transactions as follow:
    All InActive Books as Follows
    '''+ result
    final_recepient_list=["amol.londhe20@gmail.com","onlyamol22@gmail.com"]
    send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_recepient_list)
    return render(request,template_name="books.html",context={"all_books":all_in_active_books,"book_status":"In_Active"})

