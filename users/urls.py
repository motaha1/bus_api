from django.urls import path

from users.views import *

urlpatterns = [
path(r'discount', checkout.as_view()),
path(r'add', add.as_view()),
path(r'info', pass_info.as_view()),
path(r'info1', pass_info_test.as_view()),
path(r'firebase', firebase_realtime.as_view()),
path(r'new_travel', new_travel.as_view()),
path(r'cap_info', cap_info.as_view()),
path(r'buss', buss.as_view()),
# path(r'test', test.as_view()),

















# pass_info



]