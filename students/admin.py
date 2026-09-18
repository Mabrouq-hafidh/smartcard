from django.contrib import admin
from .models import Programme, Course, Student, SmartCard, CourseRegistration


# admin.site.register(Programme)
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")
    exclude = ("courses",)
    list_filter = ("courses",)
    list_per_page = 25
    list_editable = ("name",)


# admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "display_programmes")
    filter_horizontal = ("programmes",)

    def display_programmes(self, obj):
        return ", ".join(programme.name for programme in obj.programmes.all())

    display_programmes.short_description = "Programmes"

admin.site.register(Student)
admin.site.register(SmartCard)
admin.site.register(CourseRegistration)