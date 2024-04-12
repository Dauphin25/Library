from django.contrib import admin

from .models import Book, Author


@ admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'year', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category')
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    fields = ['title', 'author', 'category', 'year', 'price', 'cover']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['price']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['title']
    list_select_related = False
    save_as = False
    save_on_top = False
    preserve_filters = True
    inlines = []
    exclude = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    actions = []
    show_full_result_count = True
    show_all = False


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'birth_place', 'death_date', 'death_place', 'created_at', 'updated_at')
    list_filter = ('birth_date', 'birth_place')
    search_fields = ('name', 'birth_place')
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    fields = ['name', 'birth_date', 'birth_place', 'death_date', 'death_place', 'portrait']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['name']
    list_select_related = False
    save_as = False
    save_on_top = False
    preserve_filters = True
    inlines = []
    exclude = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    actions = []
    show_full_result_count = True
    show_all = False