from django.contrib import admin
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add-to-cart/<int:id>/', views.add_to_cart),
    path('cart/', views.cart_view),
    path('place-order/', views.place_order),
    path('orders/', views.orders),
    path('dashboard/', views.dashboard),
    path('checkout/', views.checkout),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)