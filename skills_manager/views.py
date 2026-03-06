from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.text import slugify
from django.contrib import messages
from .models import Category, SkillComponent, UserSkillsCollection


def home(request):
    """Home page showing available categories"""
    categories = Category.objects.filter(skill_components__is_active=True).distinct()
    context = {
        'categories': categories,
    }
    return render(request, 'skills_manager/home.html', context)


@login_required
def dashboard(request):
    """User dashboard showing their skills collections"""
    collections = UserSkillsCollection.objects.filter(user=request.user)
    context = {
        'collections': collections,
    }
    return render(request, 'skills_manager/dashboard.html', context)


@login_required
def category_detail(request, category_slug):
    """Show skill components for a specific category"""
    category = get_object_or_404(Category, slug=category_slug)
    components = category.skill_components.filter(is_active=True)

    # Get user's current collection if editing
    collection_id = request.GET.get('collection_id')
    selected_components = set()
    if collection_id:
        try:
            collection = UserSkillsCollection.objects.get(id=collection_id, user=request.user)
            selected_components = set(collection.selected_components.all())
        except UserSkillsCollection.DoesNotExist:
            pass

    context = {
        'category': category,
        'components': components,
        'selected_components': selected_components,
        'collection_id': collection_id,
    }
    return render(request, 'skills_manager/category_detail.html', context)


@login_required
def create_skills_collection(request):
    """Create a new skills collection"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        component_ids = request.POST.getlist('components')

        # Validate name
        if not name:
            return render(request, 'skills_manager/create_collection.html', {
                'error': 'Collection name is required'
            })

        # Check if collection with this name already exists
        if UserSkillsCollection.objects.filter(user=request.user, name=name).exists():
            return render(request, 'skills_manager/create_collection.html', {
                'error': 'A collection with this name already exists'
            })

        # Create collection
        collection = UserSkillsCollection.objects.create(
            user=request.user,
            name=name,
            description=description
        )

        # Add selected components
        if component_ids:
            components = SkillComponent.objects.filter(id__in=component_ids, is_active=True)
            collection.selected_components.set(components)

        messages.success(request, f'Collection "{name}" created successfully!')
        return redirect('skills_collection_detail', collection_id=collection.id)

    # GET request - show creation form
    categories = Category.objects.filter(skill_components__is_active=True).distinct()
    context = {
        'categories': categories,
    }
    return render(request, 'skills_manager/create_collection.html', context)


@login_required
def skills_collection_detail(request, collection_id):
    """Show details of a specific skills collection"""
    collection = get_object_or_404(UserSkillsCollection, id=collection_id, user=request.user)

    context = {
        'collection': collection,
        'markdown_content': collection.generate_markdown_content(),
    }
    return render(request, 'skills_manager/collection_detail.html', context)


@login_required
def download_skills_file(request, collection_id):
    """Download skills collection as .md file"""
    collection = get_object_or_404(UserSkillsCollection, id=collection_id, user=request.user)

    response = HttpResponse(collection.generate_markdown_content(), content_type='text/markdown')
    response['Content-Disposition'] = f'attachment; filename="{slugify(collection.name)}.md"'
    return response
