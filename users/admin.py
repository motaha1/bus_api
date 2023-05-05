from django.contrib import admin


from users.models import *

# Register your models here.

admin.site.register(Passenger)
admin.site.register(Travel)
admin.site.register(Bus)
admin.site.register(Captine)



admin.site.site_header = "Smart Bus Adminpanel"
admin.site.site_title = "Smart Bus Adminpanel"