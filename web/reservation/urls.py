from django.conf.urls import url
from reservation import reservation_views

app_name = 'reservation'
urlpatterns = [
	url(r'^home/$', reservation_views.home, name='home'),
    url(r'^insert/$', reservation_views.create_post, name='create_post')
]