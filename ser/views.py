from django.shortcuts import render,redirect
from signin.models import UserProfile                   #neww222
from signin.forms import ExtendedUserCreationForm, UserProfileForm #neww222
from .models import Service,Item,Quantity
from django.db.models import Q
# Create your views here.
from django.views.generic import ListView, DetailView, View
from .forms import ser_req
from .forms import buy
from .forms import item_form
from django.core.paginator import Paginator
from datetime import date,timedelta

#for email
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required
def req(request):
    aut=request.user.username
    current_user=request.user
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    if request.method == "POST":
        form = ser_req(request.POST,initial={'aut':aut,'flat_number':flat_number})
        if form.is_valid():
            form.save()
            return redirect('email')    
    else:
        form = ser_req(initial={'aut':aut,'flat_number':flat_number})
    context = {
        'form':form
    }
    return render(request, 'Ask_form.html', context)
    


@login_required
def shop(request):                                             
    items = Item.objects.all()
    aut=request.user.username
    current_user=request.user
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
  
    if request.method == "POST":
        form = buy(request.POST,initial={'author':aut,'flat_number':flat_number})     #neww for admin login
       
        if form.is_valid():
            
            form.save()
            
            messages.info(request, "Item ordered successfully.")
            return redirect('gmail')

    else:
       
        form = buy(initial={'author':aut,'flat_number':flat_number})

    context = {
        'form':form,
        'items':items,
        'current_user':current_user,  
    }
    
    return render(request, 'buy2.html', context)

@login_required
def serv_mail(request):    

    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    
    obj2=Service.objects.last()
    msg=obj2.body
    p=str(msg)

    mg=obj2.time
    s=str(mg)
    
    z="flat number :"+x+"\n"+"mobile number  :"+y+"\n"+"problem: "+p+"\n"+"Date: "+s

    subject = 'Service request posted'
    message=z
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail] 
    print(recipient_list)
    send_mail( subject, message, email_from, recipient_list )    
    return redirect('show')

@login_required
def shopmail(request):    
    
    current_user=request.user
    mail=request.user.email
    obj=UserProfile.objects.get(user=current_user)
    flat_number=obj.flat_number
    x=str(flat_number)
    
    mobile_number=obj.mobile_number
    y=str(mobile_number)
    
    # obj2=Post.objects.filter(aut=current_user).order_by('created')[:1]
    obj2=Quantity.objects.last()
    item=str(obj2.item)
    quantity=str(obj2.quantity)
    total=obj2.quantity*obj2.item.price
    price=str(total)
    
    z="FLAT NUMBER :"+x+"\n"+"MOBILE NUMBER :"+y+"\n"
    
    
    shoppinglist=(z+" Order Summary:"+"\n"+"Quantity : "+quantity +",  Item : "+item+", Price : "+price)
    
    context = {
        'details':shoppinglist
    }
    
    
   #email details---

    subject = 'You have orders'
    message=shoppinglist
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail] 
    
    if (obj2.quantity):
        send_mail( subject, message, email_from, recipient_list )    
    
   
    
    return redirect('/shop')

@login_required
def Myreqview(request):              #display service requests

   
    req=Service.objects.all().order_by('-created')
    aut=request.user.username
    info=[]
    for x in req:
        if x.aut==aut:
            y={'flnum':x.created,'aut':x.aut,'aut2':aut}
            info.append(y)
    
   
    paginator=Paginator(info,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        info = paginator.page(page)
    except(EmptyPage, InvalidPage):
        info=paginator.page(paginator.num_pages)

    context={
            'info':info,
            
        }   
    return render(request,'show.html',context)

class ServiceListView(ListView):
    model = Service
    template_name = 'show2.html'

    def get_queryset(self):

        category5= self.kwargs.get('category')
    
        return Service.objects.filter(created=category5)

        
@login_required
def MyView(request):                #display ordered items
    startdate = date.today()
    enddate = startdate + timedelta(days=7)
    # .filter(date__range=[startdate, enddate])
    query_results = Quantity.objects.all().order_by('-created')
    aut=request.user.username
    info=[]
   
    for x in query_results:
        if x.author==aut:
            y={'flnum':x.created,'aut':x.author,'aut2':aut}
            info.append(y)
        

   
    paginator=Paginator(info,5)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        info = paginator.page(page)
    except(EmptyPage, InvalidPage):
        info=paginator.page(paginator.num_pages)

    context={
            'info':info,
            
        }   
    return render(request, 'display.html',context)

class ShopListView(ListView):
    model = Quantity
    template_name = 'display2.html'
    

    def get_queryset(self):
   
        category6= self.kwargs.get('category')
    
        return Quantity.objects.filter(created=category6,author=self.request.user)



# def validate_user(request):
#     query_results = Quantity.objects.filter(author=request.user.username).order_by('-created')
#     context = {

#         "query_results":query_results
#     }
#     return render(request,'display2.html',context)

@login_required
def residents(request): 
    tenants=UserProfile.objects.all()
    info=[]
    for x in tenants:
        y={'flnum':x.flat_number}
        info.append(y)
    
    context={
            'info':info
        }    
    return render(request,'residents.html',context)



class CategoryListView(ListView):
    model = UserProfile
    template_name = 'residents_info.html'

    def get_queryset(self):

        category = self.kwargs.get('category')

        return UserProfile.objects.filter(flat_number=category)


@login_required
def add_item(request):                                             
   
    if request.user.groups.filter(name__in=['keeper']).exists():
        if request.method == "POST":
            form = item_form(request.POST)     #neww for admin login
            if form.is_valid():
                
                form.save()
                return redirect('index')

        else:
            form = item_form()
        context = {
            'form':form,
            
        }
        
        return render(request, 'add_item.html', context)
    else :
        return redirect('/login')

# def shop_index(request):
       

#     items = Item.objects.all()
    
#     context = {

#         'items':items
#     }

#     return render(request, 'test.html', context)