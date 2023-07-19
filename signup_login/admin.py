from django.contrib import admin
from .models import Signup,house,current_signup
# Register your models here.
admin.site.register(Signup)
admin.site.register(house)
admin.site.register(current_signup)