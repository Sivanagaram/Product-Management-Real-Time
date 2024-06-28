from django.urls import path

from . import views

urlpatterns=[
    path('',views.showallproducts,name='showpro'),
    path('products/<int:pk>', views.details, name='products'),
    path('addproducts',views.addproducts,name='addpro'),
    path('updateproducts/<int:pk>',views.updateproducts,name='updatepro'),
    path('deleteproducts//<int:pk>/', views.deleteproducts, name='deleteProduct'),
    path('search/',views.searchbar,name='search'),
    
    
]

