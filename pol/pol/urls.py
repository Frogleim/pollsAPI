
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('pols.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/user', include('pols.urls'))


]
