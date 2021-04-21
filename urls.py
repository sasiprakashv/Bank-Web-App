from django.contrib import admin
from django.urls import path
from features import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.fun,name="fun"),
    path('res',views.res,name="res"),
    path('res1',views.res1,name="res1"),
    path('customer1',views.customer1,name="customer1"),
    path('customer2',views.customer2,name="customer2"),
    path('customer3',views.customer3,name="customer3"),
    path('customer4',views.customer4,name="customer4"),
    path('customer5',views.customer5,name="customer5"),
    path('transaction',views.transaction,name="transaction"),
    path('receiver',views.receiver,name="receiver"),

    ]
