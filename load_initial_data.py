import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Skills.settings')
django.setup()

from skills_manager.models import Category, SkillComponent


def load_skills_data():
    # Create general programming category
    general_category, created = Category.objects.get_or_create(
        name='General Programming',
        defaults={
            'description': 'General software development principles and practices'
        }
    )

    # Load skills.md content
    try:
        with open('skills.md', 'r') as f:
            skills_content = f.read()

        # Split into sections
        sections = skills_content.split('-' * 50)

        for i, section in enumerate(sections):
            if not section.strip():
                continue

            # Extract title (first line after dashes)
            lines = section.strip().split('\n')
            if not lines:
                continue

            title = lines[0].strip()
            if not title:
                continue

            # Skip the header
            if title == 'AI Coding Skills & Guidelines':
                continue

            content = '\n'.join(lines).strip()

            # Create skill component
            skill, created = SkillComponent.objects.get_or_create(
                title=title,
                category=general_category,
                defaults={
                    'content': content,
                    'order': i
                }
            )

            if created:
                print(f"Created skill: {title}")
            else:
                print(f"Skill already exists: {title}")

    except FileNotFoundError:
        print("skills.md not found, creating sample skills...")

        # Create sample skills
        sample_skills = [
            {
                'title': 'Object-Oriented Programming',
                'content': '''IMPERATIVE:
Prefer object-oriented programming (OOP) when designing systems.

GUIDELINES:
- Organize related logic into classes instead of loose functions.
- Encapsulate behavior with the data it operates on.
- Keep classes focused on a single responsibility.
- Prefer composition over inheritance.
- Use inheritance only when the relationship is truly "is-a".
- Build small collaborating objects instead of large procedural scripts.'''
            },
            {
                'title': 'Project Architecture',
                'content': '''Architectural Bias: Modular and domain-driven design.

RULES:
- Separate concerns clearly.
- Business logic must not live in controllers or routes.
- Models represent domain entities.
- Services contain business logic and workflows.
- Controllers/views coordinate actions but remain thin.'''
            },
            {
                'title': 'Function Design',
                'content': '''Functions should be:
- Small
- Predictable
- Single-purpose
- Easy to read

Prefer:
    user_service.create_user()

Avoid:
    do_everything_and_save_user()'''
            }
        ]

        for i, skill_data in enumerate(sample_skills):
            skill, created = SkillComponent.objects.get_or_create(
                title=skill_data['title'],
                category=general_category,
                defaults={
                    'content': skill_data['content'],
                    'order': i
                }
            )
            if created:
                print(f"Created sample skill: {skill_data['title']}")

    # Create a React category
    react_category, created = Category.objects.get_or_create(
        name='React',
        defaults={
            'description': 'React.js framework skills and best practices'
        }
    )

    # Create React sample skills
    react_skills = [
        {
            'title': 'Component Design',
            'content': '''Guidelines for React component design:
- Keep components small and focused
- Use functional components with hooks
- Follow single responsibility principle
- Use TypeScript for type safety
- Avoid prop drilling, use context instead'''
        },
        {
            'title': 'State Management',
            'content': '''React state management approaches:
- Use useState for local component state
- Use useContext for global state that doesn't change often
- Use Redux for complex application state
- Consider Zustand or Jotai for simpler alternatives
- Avoid unnecessary state lifting'''
        },
        {
            'title': 'Performance Optimization',
            'content': '''Performance optimization techniques:
- Use React.memo() for expensive components
- Use useMemo() and useCallback() appropriately
- Code splitting with React.lazy()
- Avoid unnecessary re-renders
- Use proper dependency arrays'''
        }
    ]

    for i, skill_data in enumerate(react_skills):
        skill, created = SkillComponent.objects.get_or_create(
            title=skill_data['title'],
            category=react_category,
            defaults={
                'content': skill_data['content'],
                'order': i
            }
        )
        if created:
            print(f"Created React skill: {skill_data['title']}")


if __name__ == '__main__':
    load_skills_data()
    print("Initial data loaded successfully!")