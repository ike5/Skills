import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Skills.settings')
django.setup()

from skills_manager.models import Category, SkillComponent


def clean_title(title):
    """Clean up section titles"""
    # Remove extra whitespace and symbols
    title = title.strip()
    # Remove leading/trailing punctuation
    title = title.strip('-')
    title = title.strip()
    # Remove markdown headers
    if title.startswith('#'):
        title = title.strip('#')
        title = title.strip()
    return title


def load_skills_data():
    # Delete existing skills for clean import
    SkillComponent.objects.all().delete()
    Category.objects.all().delete()

    # Create categories
    general_category = Category.objects.create(
        name='General Programming',
        description='General software development principles and practices'
    )

    react_category = Category.objects.create(
        name='React',
        description='React.js framework skills and best practices'
    )

    # Load skills.md content properly
    skills_content = '''# AI Coding Skills & Guidelines

This project uses AI-assisted development. Follow these architectural and coding principles strictly.

OBJECT-ORIENTED PROGRAMMING

IMPERATIVE:
Prefer object-oriented programming (OOP) when designing systems.

GUIDELINES:

- Organize related logic into classes instead of loose functions.
- Use clear domain objects that represent real concepts in the system.
- Encapsulate behavior with the data it operates on.
- Prefer composition over inheritance.
- Use inheritance only when there is a true "is-a" relationship.
- Keep classes focused on a single responsibility.

PATTERNS TO FAVOR:

- Domain models
- Service classes
- Manager or controller classes
- Value objects
- Reusable components

AVOID:

- Large procedural scripts
- Global state
- God objects
- Deep inheritance chains

WHEN UNSURE:
Default to creating a class.

PROJECT ARCHITECTURE

Architectural Bias: Modular and domain-driven structure.

RULES:

- Separate concerns clearly.
- Business logic should not live in controllers or routes.
- Data models should represent real domain concepts.
- Complex logic should live in services or domain classes.

RECOMMENDED STRUCTURE:

models/
Domain models and core entities

services/
Business logic and workflows

controllers/ or views/
Request handling and orchestration

utils/
Small reusable helper functions only

config/
Configuration and environment handling

tests/
Automated tests

Each file should have a clear single purpose.

FILE SIZE LIMITS

To maintain readability and maintainability:

- Files should generally remain under **300 lines**.
- Classes should generally remain under **150 lines**.
- Functions should generally remain under **40 lines**.

If a file grows too large:

1. Extract classes
2. Extract services
3. Extract reusable utilities

FUNCTION DESIGN

Functions should be:

- Small
- Predictable
- Single-purpose
- Side-effect aware

PREFER:

Good:
user_service.create_user()

Avoid:
do_everything_and_save_user()

NAMING CONVENTIONS

Names should reflect intent clearly.

Classes:
PascalCase
Example: UserManager, ChatSession

Functions and variables:
snake_case
Example: create_user, send_message

Constants:
UPPER_CASE

REFRACTORING TRIGGERS

Refactor when you see:

- A function longer than ~40 lines
- A class handling multiple responsibilities
- Duplicate logic in multiple places
- More than 3 nested conditionals
- Repeated parameter groups

Preferred refactoring techniques:

- Extract method
- Extract class
- Introduce service object
- Introduce value object

ERROR HANDLING

- Fail loudly and clearly.
- Do not silently swallow exceptions.
- Provide useful error messages.
- Use structured error handling where possible.

READABILITY FIRST

Prioritize:

1. Readability
2. Simplicity
3. Maintainability
4. Performance (only when necessary)

Code should be understandable by a new developer within minutes.

AI DEVELOPMENT BEHAVIOR

When generating code:

- Prefer modifying existing structures rather than rewriting large sections.
- Preserve established architecture.
- Do not introduce new frameworks or patterns without justification.
- Follow existing naming and structural conventions.

If a feature requires large complexity:
Break it into smaller classes and services.'''

    # Split into proper sections
    sections = []
    current_section = {'title': '', 'content': ''}

    for line in skills_content.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Check if this is a section header (uppercase with no indentation)
        if line.isupper() and not line.startswith(' ') and len(line) > 5:
            # Save previous section
            if current_section['title'] and current_section['content']:
                sections.append(current_section)

            # Start new section
            current_section = {'title': line, 'content': ''}
        else:
            # Add line to current section
            current_section['content'] += line + '\n'

    # Add the last section
    if current_section['title'] and current_section['content']:
        sections.append(current_section)

    # Create skill components
    for i, section in enumerate(sections):
        title = clean_title(section['title'])
        if title and len(title) > 3:  # Skip very short titles
            SkillComponent.objects.create(
                title=title,
                content=section['content'].strip(),
                category=general_category,
                order=i
            )
            print(f"Created skill: {title}")

    # Create React skills
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
        SkillComponent.objects.create(
            title=skill_data['title'],
            content=skill_data['content'],
            category=react_category,
            order=i
        )
        print(f"Created React skill: {skill_data['title']}")

    print("\nData loaded successfully!")
    print(f"Created {len(sections)} General Programming skills")
    print(f"Created {len(react_skills)} React skills")


if __name__ == '__main__':
    load_skills_data()