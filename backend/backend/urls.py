from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/billing', include('billing.urls')), 
    path("api/", include("patients.urls")),
    path('', include('clinic.urls')),
]