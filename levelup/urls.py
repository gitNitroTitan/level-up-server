from django.contrib import admin
from django.urls import path
from levelupapi.views import register_user, check_user


urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
]
# Requests to http://localhost:8000/register will be routed to the register_user function
# Requests to http://localhost:8000/checkuser will be routed to the login_user function
