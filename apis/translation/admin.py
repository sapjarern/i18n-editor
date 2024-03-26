from django.contrib import admin

from apis.translation.models import Language, Project, TranslationKey, Translate


class TranslationKeyInline(admin.TabularInline):
    fields = ['key']
    model = TranslationKey
    extra = 0


class TranslateInline(admin.TabularInline):
    fields = ['language', 'translate']
    model = Translate
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fields = [('code', 'title'), ('description', 'language')]
    list_display = ['code', 'title', 'language_list']
    search_fields = ['code', 'title']
    show_full_result_count = True
    sortable_by = ['code', 'title']

    inlines = [TranslationKeyInline]

    @admin.display(description='languages')
    def language_list(self, obj: Project):
        return ', '.join([str(l) for l in obj.language.all()])


class TranslationKeyAdmin(admin.ModelAdmin):
    fields = ['key', 'project']
    list_display = ['key', 'project']
    list_filter = ['project']
    search_fields = ['key', 'project']
    show_full_result_count = True
    sortable_by = ['key', 'project__code']

    inlines = [TranslateInline]


class TranslateAdmin(admin.ModelAdmin):
    fields = ['translation_key', 'language', 'translate']
    list_display = ['translation_key', 'language', 'translate']
    list_filter = ['language']
    search_fields = ['translate']
    show_full_result_count = True
    sortable_by = ['translation_key__key', 'language__code']


# Register your models here.
admin.site.register(Language)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TranslationKey, TranslationKeyAdmin)
admin.site.register(Translate, TranslateAdmin)