from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag

class CourseInline(admin.StackedInline):
    model = Course

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_date', 'updated_date', 'active']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)
