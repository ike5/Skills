from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    """Represents a framework or task category (like React, Django, etc.)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SkillComponent(models.Model):
    """Represents an individual skill component that users can select"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='skill_components')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'title']
        unique_together = ['title', 'category']

    def __str__(self):
        return f"{self.category.name}: {self.title}"


class UserSkillsCollection(models.Model):
    """Represents a user's collection of selected skills"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills_collections')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    selected_components = models.ManyToManyField(SkillComponent, related_name='user_collections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'name']
        ordering = ['-created_at']

    def generate_markdown_content(self):
        """Generate the skills.md content from selected components"""
        # Group by category
        components_by_category = {}
        for component in self.selected_components.all():
            category_name = component.category.name
            if category_name not in components_by_category:
                components_by_category[category_name] = []
            components_by_category[category_name].append(component)

        # Build markdown content
        markdown_lines = []
        markdown_lines.append(f"# {self.name}\n")
        if self.description:
            markdown_lines.append(f"{self.description}\n")

        for category_name, components in components_by_category.items():
            markdown_lines.append(f"\n\n{'='*50}")
            markdown_lines.append(f"{category_name}")
            markdown_lines.append(f"{'='*50}\n")

            for component in components:
                markdown_lines.append(f"\n## {component.title}\n")
                markdown_lines.append(f"{component.content}\n")

        return '\n'.join(markdown_lines)

    def __str__(self):
        return f"{self.user.username}: {self.name}"
