#urls for the webkiosk app

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webkiosk'
urlpatterns = [
    #localhost:8000/webkiosk
    path('', views.index, name='index'), #functions are in views.py, 3rd arg = name to the url

    #localhost:8000/webkiosk/login
    path('login', views.loginpage, name='log-in'),

    #localhost:8000/webkiosk/logout
    path('logout', views.logoutpage, name='log-out'),

    #localhost:8000/webkiosk/register
    path('register', views.register, name='register-user'),
    
    #localhost:8000/webkiosk/food
    path('food/', views.listfood, name='food-list'),

    #localhost:8000/webkiosk/food/new
    path('food/new/', views.createfood, name='food-create'), 

    #localhost:8000/webkiosk/food/<id>
    path('food/<int:pk>', views.detailfood, name='food-detail'),

    #localhost:8000/webkiosk/food/<int:pk>/delete
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

    #localhost:8000/webkiosk/food/<int:pk>/edit/
    path('food/<int:pk>/edit/',views.updatefood,name='food-update'),

    #localhost:8000/webkiosk/customers/
    #call view function name listcustomers, url pattern - customer list
    path('customers/', views.listcustomers, name='customer-list'),

    #localhost:8000/webkiosk/customers/new
    path('customers/new/', views.createcustomer, name='customer-create'),
    
    #localhost:8000/webkiosk/customers/<id>
    path('customers/<int:pk>', views.detailcustomer, name='customer-detail'),

    #localhost:8000/webkiosk/customers/<int:pk>/edit/
    path('customers/<int:pk>/edit/',views.updatecustomers,name='customer-update'),

    #localhost:8000/webkiosk/customers/<int:pk>/delete
    path('customers/<int:pk>/delete/', views.deletecustomers, name='customer-delete'),

    #localhost:8000/webkiosk/customers/<int:pk>/vieworders/
    path('customers/<int:pk>/vieworders/', views.customerorders, name='customer-orders'),

    #localhost:8000/webkiosk/orders/
    path('orders/', views.listorders, name='order-list'),

    #localhost:8000/webkiosk/orders/new/
    path('orders/new/',views.createorder, name='order-create'),

    #localhost:8000/webkiosk/orders/4
    path('orders/<int:pk>', views.detailorders, name='order-detail'),

    #localhost:8000/webkiosk/orders/4/edit
    path('orders/<int:pk>/edit/', views.updateorders, name='order-update'),

    #localhost:8000/webkiosk/orders/4/delete
    path('orders/<int:pk>/delete/', views.deleteorders, name='order-delete'),

 ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


