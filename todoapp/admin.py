from django.contrib import admin
from .models import task
# Register your models here.
class taskAdmin(admin.ModelAdmin):
    list_display=('tasks','is_completed','updated_at')
    search_fields=('tasks',)
admin.site.register(task,taskAdmin)