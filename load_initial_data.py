import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Skills.settings')
django.setup()

from skills_manager.models import Category, SkillComponent


def load_skills_data():
    # Clear existing data first
    SkillComponent.objects.all().delete()
    Category.objects.all().delete()

    # Load skills from JSON file
    try:
        with open('skills_data.json', 'r') as f:
            skills_data = json.load(f)

        # Process each skill in the JSON
        for skill_info in skills_data['skills']:
            # Get or create the category
            category_name = skill_info.get('category', 'General Programming')
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={
                    'description': f'{category_name} principles and practices'
                }
            )

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
                print(f"Created skill: {skill_info['title']}")
            else:
                print(f"Skill already exists: {skill_info['title']}")

    except FileNotFoundError:
        print("skills_data.json not found - skills must be loaded from JSON file")


if __name__ == '__main__':
    load_skills_data()
    print("Initial data loaded successfully!")