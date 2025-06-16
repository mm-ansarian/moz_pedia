from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
]


handler403 = 'web.views.permission_denied_view'
handler404 = 'web.views.not_found_view'
