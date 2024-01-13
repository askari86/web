from django.urls import path
from page.views import index_view
app_name="page"
urlpatterns=[
    path('',index_view,name='index')
]