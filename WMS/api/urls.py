"""WMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', DetailsView.as_view(), name='details'),
    url(r'^$', CreateView.as_view(), name='create'),
    # This new line includes the DRF routes that provides a default login template
    # to authenticate a user. You can call the route anything you want.
    # you will see a login button on the top right of the screen when you access any of the above urls
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/', obtain_auth_token),
]


urlpatterns = format_suffix_patterns(urlpatterns)

# The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs.
# It appends the format to be used to every URL in the pattern.
