from django.contrib import admin
from django.urls import path,include
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login
from .views.cart import Cart
from .views.sellerLogin import SellerLogin
from .views.sellerSignUp import SellerSignUp
from .views.sellerHomepage import SellerHomepage
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views import searchproduct
from .views import productdetails
from .views import productdetail
from .views import payment
from .views import profile
from .views.addProduct import AddProduct
from django.conf.urls.static import static
from kartocity import settings


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('sellerLogin', SellerLogin.as_view() , name='sellerLogin'),
    path('sellerSignUp', SellerSignUp.as_view() , name='sellerSignUp'),
    path('sellerHomepage', SellerHomepage.as_view() , name='sellerHomepage'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('checkout', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('searchproduct', searchproduct.search_products, name='search-products'),
    path('productdetails', productdetails.product_details, name='product-details'),
    path('productdetail', productdetail.product_details2, name='product-details2'),
    path('payment', payment.charge, name='pay-charge'),
    path('profile', profile.Profile, name='profile'),
    path('logout/',profile.logout,name='logout'),
    path('addProduct',AddProduct.as_view(),name='addProduct')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
