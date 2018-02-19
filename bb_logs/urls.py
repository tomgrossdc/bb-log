"""bb_log/bb_logs/url.py 
  This file specifies the bb_logs specific models etc.
  map http://localhost:8000/index.html   to views.index 
    edit the file bb_logs/views.py for an def index(request)

  Regular expression  ^$  says from beginning^ to end$ nothing then use index
  

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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	# Show bases by operation
	url(r'^bb_bases/$', views.bb_bases, name='bb_bases'),
	url(r'^bb_urls/$', views.bb_urls, name='bb_urls'),
]
