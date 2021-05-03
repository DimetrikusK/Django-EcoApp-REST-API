from django.contrib import admin
from .models import *

# admin.site.register(Course)
# admin.site.register(Ecocard)
admin.site.register(Ecosoviet)
admin.site.register(Profile)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'id', 'title', 'user')


@admin.register(Ecocard)
class EcocardAdmin(admin.ModelAdmin):
    list_display = ('cardname', 'id', 'coursenameid', 'title')

