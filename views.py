from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .models import Food, Customer, Order
from .forms import FoodForm, CustomerForm, OrderForm, CreateUserForm

# Create your views here.

#STARTING PAGES
@login_required(login_url='webkiosk:log-in')
def index(request): 
    return render(request,'webkiosk/welcome.html')

def register(request):
    form = CreateUserForm

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account was succesfully created for ' + username)
            return redirect('webkiosk:customer-list')  

    context = {'form':form}
    return render(request, 'webkiosk/registration.html', context)

def loginpage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('webkiosk:food-list')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request, 'webkiosk/login_user.html', context)

def logoutpage(request):
    logout(request)
    return redirect('webkiosk:log-in')


#FOOD

@login_required(login_url='webkiosk:log-in')
def listfood(request):
    fl = Food.objects.all()
    context = {
        'foodlist': fl
    }
    return render(request, 'webkiosk/food_list.html', context) 

#add food page
#get to view the form, post to submit 
@login_required(login_url='webkiosk:log-in')
def createfood (request):
    if request.method == 'GET':
        ff = FoodForm() 
    elif request.method == 'POST':
        ff = FoodForm(request.POST)
        if ff.is_valid():
            ff.save()
            return redirect('webkiosk:food-list')

    context = { 'form': ff } 
    return render(request, 'webkiosk/food_form.html', context)

#details view function
@login_required(login_url='webkiosk:log-in')
def detailfood(request, pk):
    f = Food.objects.get(id=pk)
    context = { 'food':f }
    return render(request, 'webkiosk/food_detail.html', context)

#delete the food record, if get executes with delete button, post to the food list
@login_required(login_url='webkiosk:log-in')
def deletefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method=='GET':
        context = { 'food':f}
        return render(request, 'webkiosk/food_delete.html',context)
    elif request.method=='POST':
        f.delete()
        return redirect('webkiosk:food-list')

#update food record
@login_required(login_url='webkiosk:log-in')
def updatefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method=='GET':
        ff = FoodForm(instance=f)
    elif request.method == 'POST':
        ff = FoodForm(request.POST, instance=f)
        if ff.is_valid():
            ff.save()
            messages.success(request,'Food record successfully updated.')

    context = { 'form':ff } 
    return render(request, 'webkiosk/food_form.html',context)

#CUSTOMERS

#Customer same as model name
@login_required(login_url='webkiosk:log-in')
def listcustomers(request):
    cl = Customer.objects.all()
    context = {
        'customerlist': cl
    }
    return render(request, 'webkiosk/customer_list.html', context)

#create new customer
@login_required(login_url='webkiosk:log-in')
def createcustomer(request):
    if request.method =='GET':
        cf = CustomerForm()
    elif request.method =='POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect('webkiosk:customer-list')
    
    context = { 'form': cf } 
    return render(request, 'webkiosk/customer_form.html', context)

#view customer details
@login_required(login_url='webkiosk:log-in')
def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer':c}
    return render(request, 'webkiosk/customer_detail.html', context)

#delete customer
@login_required(login_url='webkiosk:log-in')
def deletecustomers(request,pk):
    c = Customer.objects.get(id=pk)
    if request.method=='GET':
        context = {'customer':c}
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method=='POST':
        c.delete()
        return redirect('webkiosk:customer-list')
        
#update customer details
@login_required(login_url='webkiosk:log-in')
def updatecustomers(request, pk):
    c = Customer.objects.get(id=pk)
    if request.method=='GET':
        cf = CustomerForm(instance=c)
    elif request.method=='POST':
        cf = CustomerForm(request.POST, instance=c)
        if cf.is_valid():
            cf.save()
            messages.success(request, 'Customer details successfully updated.')
    
    context = { 'form': cf }
    return render(request, 'webkiosk/customer_form.html', context)


# View all Orders of Customer
@login_required(login_url='webkiosk:log-in')
def customerorders(request, pk):
    ol = Order.objects.filter(customer_id=pk)
    context = {'orderlist': ol}
    return render(request, 'webkiosk/customer_orders.html', context)


#ORDERS
#Order List Page
@login_required(login_url='webkiosk:log-in')
def listorders(request):
    ol = Order.objects.all()
    context = {
        'orderlist': ol
    }
    return render(request, 'webkiosk/order_list.html',context)


#Add Order Page
@login_required(login_url='webkiosk:log-in')
def createorder(request):
        if request.method == 'GET':
            oo = OrderForm()
        elif request.method == 'POST':
            oo = OrderForm(request.POST)
            if oo.is_valid():
                oo.save()
                return redirect('webkiosk:order-list')

        context = {'form': oo}
        return render(request,'webkiosk/order_form.html', context)


#Details View Function
@login_required(login_url='webkiosk:log-in')
def detailorders(request, pk):
    o = Order.objects.get(id=pk)
    context = { 'order': o }
    return render(request, 'webkiosk/order_detail.html', context)


# Update Order Record
@login_required(login_url='webkiosk:log-in')
def updateorders(request, pk):
    o = Order.objects.get(id=pk)
    if request.method == 'GET':
        oo = OrderForm(instance=o)
    elif request.method == 'POST':
        oo = OrderForm(request.POST, instance=o) #instance=o enables us to update the correct order record
        if oo.is_valid():
            oo.save()
            messages.success(request, 'Food record successfully updated.')

    context = { 'form' : oo }    #connected to the form.as_ul in order_form.html
    return render(request, 'webkiosk/order_form.html', context) 

# Delete Order Records
@login_required(login_url='webkiosk:log-in')
def deleteorders(request, pk):
    o = Order.objects.get(id=pk)
    if request.method == 'GET':
        context = { 'order': o }
        return render(request, 'webkiosk/order_delete.html', context)
    elif request.method == 'POST':
        o.delete()
        return redirect('webkiosk:order-list')