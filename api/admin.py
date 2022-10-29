from django.contrib import admin
from .models import Assistants,UserLogs,Credits,Leave
# Register your models here.
admin.site.register(Assistants)
admin.site.register(UserLogs)
admin.site.register(Credits)
admin.site.register(Leave)