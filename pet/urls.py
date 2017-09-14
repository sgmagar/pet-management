from django.conf.urls import url

from pet.views import (
    HomePageView, LogoutView, RegisterView, LoginView, CreateDogView,
    EditDogView, DeleteDogView, CreateCatView, EditCatView, DeleteCatView)

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^create-dog/$', CreateDogView.as_view(), name='create_dog'),
    url(r'^edit-dog/(?P<pk>\d+)/$', EditDogView.as_view(), name='edit_dog'),
    url(r'^delete-dog/(?P<pk>\d+)/$', DeleteDogView.as_view(), name='delete_dog'),
    url(r'^create-cat/$', CreateCatView.as_view(), name='create_cat'),
    url(r'^edit-cat/(?P<pk>\d+)/$', EditCatView.as_view(), name='edit_cat'),
    url(r'^delete-cat/(?P<pk>\d+)/$', DeleteCatView.as_view(), name='delete_cat'),
]
