
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('api.urls')),
    
    # Local apps
    path("",include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    
    # User management
    path("accounts/",include("django.contrib.auth.urls")),
    
]
