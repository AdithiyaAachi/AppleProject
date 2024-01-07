from django.urls import path
from MyApp import views
from django.views.generic import RedirectView
urlpatterns=[
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('products_filter/<book_name>/',views.products_filter,name="products_filter"),
    path('singlepro_page/<int:proid>/',views.singlepro_page,name="singlepro_page"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('register_save/',views.register_save,name="register_save"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cart_delete/<int:pro_id>/',views.cart_delete,name="cart_delete"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage")

]