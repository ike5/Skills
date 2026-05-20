import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Skills.settings')
django.setup()

from skills_manager.models import Category, SkillComponent


def load_skills_from_categories():
    """Load skills from categorized JSON files in the skills/categories directory"""

    categories_dir = 'skills/categories'

    # Clear existing data first
    SkillComponent.objects.all().delete()
    Category.objects.all().delete()

    # Process each category file
    for filename in os.listdir(categories_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(categories_dir, filename)

            try:
                with open(filepath, 'r') as f:
                    skills_data = json.load(f)

                print(f"Loading skills from {filename}...")

                # Get category name from first skill in file
                if skills_data.get('skills'):
                    category_name = skills_data['skills'][0].get('category', 'Uncategorized')
                    category_description = f'{category_name} principles and practices'

                    category, created = Category.objects.get_or_create(
                        name=category_name,
                        defaults={'description': category_description}
                    )

                    if created:
                        print(f"Created category: {category_name}")

                    # Process skills in this file
                    for skill_info in skills_data['skills']:
                        # Create formatted content
                        content_lines = [
                            skill_info['description'],
                            '',
                            'GUIDELINES:',
                            ''
                        ]
                        content_lines.extend([f'- {guideline}' for guideline in skill_info['guidelines']])
                        content = '\n'.join(content_lines)

                        # Create skill component
                        skill, created = SkillComponent.objects.get_or_create(
                            title=skill_info['title'],
                            category=category,
                            defaults={
                                'content': content,
                                'order': len(SkillComponent.objects.filter(category=category))
                            }
                        )

                        if created:
                            print(f"  Created skill: {skill_info['title']}")

                    print(f"Loaded {len(skills_data['skills'])} skills from {filename}")

            except Exception as e:
                print(f"Error loading {filename}: {str(e)}")

    print("\nCategorized skills loading completed!")


if __name__ == '__main__':
    load_skills_from_categories()
    total_skills = SkillComponent.objects.count()
    total_categories = Category.objects.count()
    print(f"Total skills loaded: {total_skills}")
    print(f"Total categories: {total_categories}")