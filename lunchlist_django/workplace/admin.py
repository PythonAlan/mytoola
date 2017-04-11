from django.contrib import admin

# Register your models here.

from workplace.models import WorkPlace
class WorkPlaceAdmin(admin.ModelAdmin):
    list_display = ("project_name",
                    "project_link",
                    )

admin.site.register(WorkPlace,WorkPlaceAdmin)