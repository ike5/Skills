# AI Coding Skills & Guidelines

This repository uses AI-assisted development.

Follow these architectural and coding principles when generating or modifying code.

Primary goals:

1. Readability
2. Maintainability
3. Clear architecture
4. Small composable components

--------------------------------------------------
OBJECT-ORIENTED PROGRAMMING
--------------------------------------------------

IMPERATIVE:
Prefer object-oriented programming (OOP) when designing systems.

GUIDELINES:

- Organize related logic into classes instead of loose functions.
- Encapsulate behavior with the data it operates on.
- Keep classes focused on a single responsibility.
- Prefer composition over inheritance.
- Use inheritance only when the relationship is truly "is-a".
- Build small collaborating objects instead of large procedural scripts.

PATTERNS TO FAVOR:

- Domain models
- Service classes
- Manager/controller classes
- Value objects
- Small reusable components

INHERITANCE RULES:

- Inheritance depth should rarely exceed 2 levels.
- Prefer composition for combining behaviors.
- Avoid large or complex base classes.
- Avoid inheritance purely for code reuse.

WHEN UNSURE:
Default to creating a class.



--------------------------------------------------
PROJECT ARCHITECTURE
--------------------------------------------------

Architectural Bias: Modular and domain-driven design.

RULES:

- Separate concerns clearly.
- Business logic must not live in controllers or routes.
- Models represent domain entities.
- Services contain business logic and workflows.
- Controllers/views coordinate actions but remain thin.

RECOMMENDED STRUCTURE:

models/
Domain models and entities

services/
Business logic and workflows

controllers/ or views/
Request handling and orchestration

utils/
Small helper utilities only

config/
Configuration and environment handling

tests/
Automated tests



--------------------------------------------------
FILE SIZE LIMITS
--------------------------------------------------

Maintain small, understandable files.

- Files should remain under ~300 lines
- Classes should remain under ~150 lines
- Functions should remain under ~40 lines

If limits are exceeded:

1. Extract classes
2. Extract services
3. Extract helper modules

--------------------------------------------------
FUNCTION DESIGN
--------------------------------------------------

Functions should be:

- Small
- Predictable
- Single-purpose
- Easy to read

Prefer:

    user_service.create_user()

Avoid:

    do_everything_and_save_user()

--------------------------------------------------
NAMING CONVENTIONS
--------------------------------------------------

Names must clearly describe intent.

Classes:
PascalCase

Functions and variables:
snake_case

Constants:
UPPER_CASE



--------------------------------------------------
TEST DRIVEN DEVELOPMENT
--------------------------------------------------

Use pragmatic Test-Driven Development.

Write tests for important behavior before or alongside implementation.

Focus tests on:

- Core domain logic
- Business rules
- Critical workflows
- Edge cases
- Public interfaces of services and models

Tests should validate **behavior**, not internal implementation.

Prefer testing:

- Services
- Domain models
- Business logic

Avoid excessive testing of:

- Simple getters/setters
- Thin controllers
- Framework boilerplate
- Trivial data structures

Guidelines:

- Tests should be readable and descriptive.
- Each test should verify one behavior.
- Prefer fewer high-value tests over many trivial tests.
- Tests should protect important system behavior.

Example philosophy:

Test important logic, not everything.



--------------------------------------------------
REFACTORING TRIGGERS
--------------------------------------------------

Refactor when you see:

- Functions longer than ~40 lines
- Classes handling multiple responsibilities
- Duplicate logic
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
- Provide meaningful error messages.
- Use structured exception handling.

--------------------------------------------------
READABILITY FIRST
--------------------------------------------------

Prioritize in this order:

1. Readability
2. Simplicity
3. Maintainability
4. Performance (optimize only when necessary)

Code should be understandable by a new developer within minutes.



--------------------------------------------------
WHAT NOT TO DO
--------------------------------------------------

Do NOT:

- Create deep inheritance hierarchies
- Create "god classes"
- Put business logic in controllers/routes
- Write large procedural scripts instead of classes
- Introduce global mutable state
- Duplicate logic across files
- Create overly complex abstractions
- Write functions exceeding ~40 lines
- Use inheritance purely for code reuse
- Mix unrelated responsibilities in one class
- Over-test trivial code

--------------------------------------------------
AI DEVELOPMENT BEHAVIOR
--------------------------------------------------

When generating code:

- Follow the architecture defined in this file.
- Prefer modifying existing structures instead of rewriting large sections.
- Maintain consistent naming and structure.
- Do not introduce new frameworks without justification.
- Break complex features into smaller classes and services.

If complexity increases:
Create additional classes rather than larger functions.