from django.conf.urls import url

from pet.views import HomePageView, LogoutView, RegisterView, LoginView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')

]
