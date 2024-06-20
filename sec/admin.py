from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Slide, Update, Whyu, Teacher, School_Info,Welcome


admin.site.register(Update)
admin.site.register(Whyu)
admin.site.register(School_Info)
admin.site.register(Welcome)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 't_id', 'role', 'image',)
    search_fields = ('full_name', 'role', 't_id')
    #prepopulated_fields = {'slug': ('title',)}

# admin.py


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ( 'caption',)
    #list_editable = ('order',)
    #ordering = ('order',)
