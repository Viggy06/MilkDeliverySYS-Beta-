from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),

    #admin urls
    path('upload/', views.upload, name='upload'),
    path("impexp/", views.impexp, name="impexp"),
    path('sb/', views.sb, name='sb'),
    path('assign_orders/', views.assign_orders,name='assign_orders'),
    path('dboy/', views.dboy, name='dboy'),

    path('ods', views.ods, name='ods'),

    path('cao', views.cao, name='cao'),
    path('exisitingdboy/', views.exisitingdboy, name='exisitingdboy'),
    path('DeleteAssignedOrders', views.DeleteAssignedOrders, name='DeleteAssignedOrders'),

    path('getpost/',views.getpost, name='getpost'),
    path('dboyride',views.dboyride, name='dboyride'),

    path('orderhistory',views.orderhistory, name='orderhistory'),
    path('orderhistoryf1',views.orderhistoryf1, name='orderhistoryf1'),
    path('orderhistoryf2',views.orderhistoryf2, name='orderhistoryf2'),
    path('orderhistoryf3',views.orderhistoryf3, name='orderhistoryf3'),
    path('orderhistoryf4',views.orderhistoryf4, name='orderhistoryf4'),
]