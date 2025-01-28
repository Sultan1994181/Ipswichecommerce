from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls')),
    path('orders/', include('apps.orders.urls')),
    path('users/', include('apps.users.urls')),
]
