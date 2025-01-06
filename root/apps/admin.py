from django.contrib import admin
from .models import Person,Job
from django.utils.html import format_html


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('fullname','job', 'img')

    def img(self, obj):
        return format_html(
            f'''<a href="{obj.image.url}" target="_blank">
                          <img src="{obj.image.url}" alt="image" width="150" height="100"
                               style="object-fit: cover;"/>
                      </a>'''
        )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name',)