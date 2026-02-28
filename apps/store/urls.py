from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('contact/', views.contact_us, name='contact_us'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('invoice/', views.generate_invoice, name='generate_invoice'),
    path('signup/', views.signup, name='signup'),
    path('add-review/<int:product_id>/', views.add_review, name='add_review'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]