from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag

class CourseInline(admin.StackedInline):
    model = Course

class LessonInline(admin.StackedInline):
    model = Lesson

class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_date', 'updated_date', 'active']
    inlines = [LessonInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_date', 'updated_date', 'active']
    inlines = [LessonTagInline]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
