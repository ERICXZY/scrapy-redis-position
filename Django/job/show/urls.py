from django.conf.urls import url
from . import views
urlpatterns = [
	#列表页
	url(r'^(?P<pIndex>[0-9]*)',views.index,name='index'),
	#搜索关键字
	#url(r'^keywords$')
]