from django.contrib import admin
from courses.models import Category, Course, Lesson, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

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

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget)
    class Meta:
        model = Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_date', 'updated_date', 'active']

    form = LessonForm
    inlines = [LessonTagInline]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
