from django.urls import path
from cvsite.views import *

app_name="cvsite"

urlpatterns = [
    path('',index_view, name='index'),
]
