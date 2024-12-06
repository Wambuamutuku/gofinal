from django.contrib import admin
from myapp.models import Member, ImageModel
from myapp.models import product
from myapp.models import Appointment,Contact,User

# Register your models here.
admin.site.register(Member)
admin.site.register(product)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(ImageModel)