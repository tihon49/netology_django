from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, ArticleSection



class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        set_is_main = False
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                if set_is_main:
                    raise ValidationError('Основной раздел может быть только один!')
                set_is_main = True
        if not set_is_main:
            raise ValidationError('Укажите основной раздел!')
        return super().clean()



class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 1



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]



@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    ordering = ['name']