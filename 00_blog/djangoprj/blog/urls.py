from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('',views.post_list,name='post_list'),
	path('',views.post_list_detail,name='post_list_detail'),
	path('',views.post_list_html,name='post_list_html'),
	#path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]
