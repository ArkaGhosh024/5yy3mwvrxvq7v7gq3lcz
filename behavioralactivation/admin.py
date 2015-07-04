from django.contrib import admin
from .models import UserSchedule
from .models import User
# Register your models here.

admin.site.register(UserSchedule)
admin.site.register(User)