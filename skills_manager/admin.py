from django.contrib import admin
from .models import Category, SkillComponent, UserSkillsCollection


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'skill_components_count', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

    def skill_components_count(self, obj):
        return obj.skill_components.count()
    skill_components_count.short_description = 'Skill Components'


@admin.register(SkillComponent)
class SkillComponentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'content']
    ordering = ['category', 'order', 'title']


@admin.register(UserSkillsCollection)
class UserSkillsCollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'selected_components_count', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['name', 'description', 'user__username']

    def selected_components_count(self, obj):
        return obj.selected_components.count()
    selected_components_count.short_description = 'Components Selected'
