from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('pet.api.urls')),
    url(r'', include('pet.urls'))
]
