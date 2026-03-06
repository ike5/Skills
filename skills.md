# AI Coding Skills & Guidelines

This project uses AI-assisted development. Follow these architectural and coding principles strictly.


--------------------------------------------------
OBJECT-ORIENTED PROGRAMMING
--------------------------------------------------

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



--------------------------------------------------
PROJECT ARCHITECTURE
--------------------------------------------------

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



--------------------------------------------------
FILE SIZE LIMITS
--------------------------------------------------

To maintain readability and maintainability:

- Files should generally remain under **300 lines**.
- Classes should generally remain under **150 lines**.
- Functions should generally remain under **40 lines**.

If a file grows too large:

1. Extract classes
2. Extract services
3. Extract reusable utilities

--------------------------------------------------
FUNCTION DESIGN
--------------------------------------------------

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



--------------------------------------------------
NAMING CONVENTIONS
--------------------------------------------------

Names should reflect intent clearly.

Classes:
PascalCase
Example: UserManager, ChatSession

Functions and variables:
snake_case
Example: create_user, send_message

Constants:
UPPER_CASE



--------------------------------------------------
REFRACTORING TRIGGERS
--------------------------------------------------

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

--------------------------------------------------
ERROR HANDLING
--------------------------------------------------

- Fail loudly and clearly.
- Do not silently swallow exceptions.
- Provide useful error messages.
- Use structured error handling where possible.

--------------------------------------------------
READABILITY FIRST
--------------------------------------------------

Prioritize:

1. Readability
2. Simplicity
3. Maintainability
4. Performance (only when necessary)

Code should be understandable by a new developer within minutes.



--------------------------------------------------
AI DEVELOPMENT BEHAVIOR
--------------------------------------------------

When generating code:

- Prefer modifying existing structures rather than rewriting large sections.
- Preserve established architecture.
- Do not introduce new frameworks or patterns without justification.
- Follow existing naming and structural conventions.

If a feature requires large complexity:
Break it into smaller classes and services.