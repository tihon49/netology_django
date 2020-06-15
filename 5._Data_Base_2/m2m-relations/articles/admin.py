from django.contrib import admin

from .models import Article, Thematic_section


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass



class Thematic_sectionInline(admin.TabularInline):
    model = Thematic_section.articles.through
    extra = 3


class Thematic_sectionAdmin(admin.ModelAdmin):
    inlines = [
        Thematic_sectionInline,
    ]


admin.site.register(Thematic_section, Thematic_sectionAdmin)