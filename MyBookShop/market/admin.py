from django.contrib import admin

from market.models.book import Book

from market.models.author import Author

from market.models.category import Category

from market.models.book_publisher import BookPublisher

from market.models.publisher import Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_categories', 'cover_type', 'year', 'price', 'created_at', 'updated_at')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    fields = ['title', 'author', 'category', 'cover_type', 'year', 'price', 'cover']
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

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categories'


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    fields = ['name', 'description']
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


@admin.register(BookPublisher)
class BookPublisherAdmin(admin.ModelAdmin):
    list_display = ('book', 'publisher', 'publication_date', 'edition', 'published_copies')
    list_filter = ('publication_date', 'edition')
    search_fields = ('book__title', 'publisher__name')
    date_hierarchy = 'publication_date'
    ordering = ['publication_date']
    fields = ['book', 'publisher', 'publication_date', 'edition', 'published_copies']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['book']
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


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_year', 'country', 'website', 'email')
    list_filter = ('founded_year', 'country')
    search_fields = ('name', 'country')
    ordering = ['name']
    fields = ['name', 'founded_year', 'country', 'website', 'email']
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