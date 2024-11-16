from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category, Book, Review, Cart, CartItem, Order, OrderItem, Enquiry

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Customize the admin panel fields if necessary
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_picture', 'date_of_birth', 'location', 'website', 'phone', 'user_type')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    list_filter = ('user_type', )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username', )

admin.site.register(CustomUser, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', )
    save_on_top = True
    # readonly_fields = ('description', )
    # exclude = ('description', )
    # fields = ('description', 'name')
    # fieldsets = (
    #     ('Category Information', {'fields': ('name',)}),
    #     ('Description', {'fields': ('description',), 'classes': ('collapse',)}),
    # )
    # actions = ['mark_published', 'archive_categories']

    # def mark_published(self, request, queryset):
    #     queryset.update(status='published')

    # def archive_categories(self, request, queryset):
    #     queryset.update(status='archived')

    # prepopulated_fields = {'description': ('name', )}
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)

admin.site.register(Book)


admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Order)



class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'book', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'book')
    list_filter = ('book', )
    list_per_page = 10

admin.site.register(Enquiry, EnquiryAdmin)
