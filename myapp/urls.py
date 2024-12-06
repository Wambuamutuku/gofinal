

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index' ),
    path('service-details/',views.service,name='service-details' ),
    path('starter-page/',views.starter,name='starter-page' ),
    path('about/',views.about,name='about' ),
    path('doctors/',views.doctors,name='doctors' ),
    path('service/',views.service,name='service' ),
    path('appointment/',views.appointment,name='appointment' ),
    path('show/',views.show,name='show' ),
    path('delete/<int:id>',views.delete),
    path('contact/',views.contact, name='contact'),
    path('shcontact/',views.shcontact, name='shcontact'),
    path('delcontact/<int:id>', views.delcontact),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

    #Mpesa integration
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
