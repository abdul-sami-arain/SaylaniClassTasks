from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('part2/', include('part2.urls')),
    path('admin/', admin.site.urls),
]
