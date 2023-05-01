from django.urls import path

from users.views import *

urlpatterns = [
path(r'discount', checkout.as_view()),
path(r'add', add.as_view()),
path(r'info', pass_info.as_view()),
path(r'info1', pass_info_test.as_view()),
path(r'firebase', firebase_realtime.as_view()),






# pass_info



]