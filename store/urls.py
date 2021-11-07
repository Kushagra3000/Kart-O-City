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
from .views import otp
from .views import otpsignup
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
    path('sellerlogout/',profile.sellerlogout,name='sellerlogout'),
    path('editprofile', profile.editprofile, name='editprofile'),
    path('manageprofile',profile.manageprofile,name='manageprofile'),
    path('addProduct',AddProduct.as_view(),name='addProduct'),
    path('otp/',otp.checkotp,name='otp'),
    path('checkotpsellersignup',otp.checkotpsellersignup,name='checkotpsellersignup'),
    path('otpsellerlogin',otp.checkotpsellerlogin,name='otpsellerlogin'),
    path('checkotpmanageprofile',otp.checkotpmanageprofile,name='checkotpmanageprofile'),
    path('otpsignup/',otpsignup.checkotp,name='otpsignup'),
    path('changepassword',profile.newpass,name='changepassword'),
    path('passwordchange',profile.changepass,name='passwordchange')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
