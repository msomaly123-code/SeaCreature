from django.urls import path
from Blog import views

urlpatterns = [
    #use URL for creature
    path('creatures/', views.manage_creature),
    path('creature/<int:id>/', views.manage_creature),

    #use URL for BlogPost
    path('blogpost/', views.manage_blogpost),
    path('blogpost/<int:id>/', views.manage_blogpost),


    #use URL for Comment
    path('comment/', views.manage_comment),
    path('comment/<int:id>/', views.manage_comment),



]
