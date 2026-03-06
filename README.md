# Skills.md Builder

A Django application that allows users to build custom skills.md files by selecting skill components from different frameworks and categories.

## Features

- 💼 **Multiple Skill Categories** - Select from React, Django, General Programming, and more
- ⚡ **Brutalist UI** - Clean, minimal interface focused on functionality
- 🔐 **Social Authentication** - Login with Google, GitHub, or Apple (with Django fallback)
- 📝 **Custom Collections** - Create multiple skills.md files with different combinations
- 📋 **Copy to Clipboard** - One-click copy functionality for markdown content
- 📥 **Download .md Files** - Download skills collections as .md files
- 🔧 **Admin Panel** - Easy management of skill components and categories

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone or download the project
2. Navigate to the project directory
3. Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Load initial data:

```bash
python load_skills_properly.py
```

7. Create a superuser for admin access (optional):

```bash
python manage.py createsuperuser
```

8. Run the development server:

```bash
python manage.py runserver
```

9. Visit http://localhost:8000 to use the application

## Usage

### For Users

1. **Browse Categories**: View available skill categories on the home page
2. **Login**: Use social authentication or create a Django account
3. **Select Skills**: Choose skill components from any category
4. **Create Collection**: Save your selection as a named collection
5. **Download/Copy**: Export as .md file or copy to clipboard

### For Administrators

1. Access the admin panel at `/admin/`
2. Manage categories, skill components, and user collections
3. Add new frameworks or edit existing content

## Project Structure

```
Skills/
├── skills_manager/          # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   └── admin.py           # Admin interface
├── templates/              # HTML templates
│   └── skills_manager/     # App-specific templates
├── Skills/                 # Django project settings
├── manage.py              # Django management
└── load_skills_properly.py # Data initialization
```

## Customization

### Adding New Skill Categories

1. Use the Django admin panel at `/admin/skills_manager/category/add/`
2. Add categories manually or modify `load_skills_properly.py`

### Adding Skill Components

1. Access `/admin/skills_manager/skillcomponent/add/`
2. Each component requires:
   - Title (brief description)
   - Content (detailed markdown)
   - Category association
   - Order (display priority)

### Social Authentication Setup

To enable social authentication, add the following environment variables:

```bash
# In your environment or .env file
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
```

## API Endpoints

- `/` - Home page with category overview
- `/dashboard/` - User dashboard (login required)
- `/categories/<slug>/` - Browse skills by category
- `/skills/create/` - Create new skills collection
- `/skills/<id>/` - View/edit specific collection
- `/skills/<id>/download/` - Download collection as .md file

## Technical Details

- **Framework**: Django 6.x
- **Authentication**: django-allauth
- **Database**: SQLite (can be changed to PostgreSQL/MySQL)
- **Frontend**: Django templates with brutalist CSS
- **Markdown Generation**: Server-side markdown composition

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests if needed
5. Submit a pull request

## License

MIT License - feel free to use and modify as needed.