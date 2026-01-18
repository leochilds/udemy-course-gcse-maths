# GCSE Maths Udemy Course

This repository contains all content, scripts, and resources for creating a comprehensive GCSE Maths course for Udemy.

## About This Course

This course is designed for **adults who don't have a GCSE Maths qualification or didn't perform well when they first took it**. The content is delivered through pre-recorded video lessons created from PowerPoint presentations with voiceover narration.

### Course Format

Each lesson consists of:
- **Slide Content**: Concise, digestible key points and formulas
- **Narration**: Detailed word-for-word scripts for voiceover recording
- **Visual Learning Materials**: Graphs, diagrams, and animations (only when they add pedagogical value)

## Repository Structure

```
udemy-course-gcse-maths/
├── lessons/              # All lesson content organized by section
│   ├── section-01-[name]/
│   │   ├── lesson-01-[name].md
│   │   ├── lesson-02-[name].md
│   │   └── ...
│   ├── section-02-[name]/
│   └── ...
│
├── animations/           # Manim animation scripts
│   ├── README.md         # Animation guidelines and instructions
│   ├── section-01/
│   └── ...
│
├── templates/            # Template files for creating new content
│   └── lesson-template.md
│
├── docs/                 # Documentation and guidelines
│   ├── lesson-guidelines.md        # How to structure lessons
│   └── narration-style-guide.md    # Voice and tone standards
│
└── README.md            # This file
```

## Getting Started

### Creating a New Lesson

1. **Choose your section**: Determine which GCSE Maths topic section your lesson belongs to
2. **Copy the template**: Duplicate `templates/lesson-template.md`
3. **Name your file**: Use format `lesson-XX-descriptive-name.md`
4. **Place in section folder**: Save in `lessons/section-YY-[section-name]/`
5. **Fill in the content**: Follow the template structure for slides, narration, and visual materials

### Important Guidelines

Before creating content, please review:

- **[Lesson Guidelines](docs/lesson-guidelines.md)**: Standards for slide content, visual materials, and lesson structure
- **[Narration Style Guide](docs/narration-style-guide.md)**: Voice, tone, and scripting standards for voiceover narration

### Key Principles

✅ **Self-Contained Lessons**: Each lesson must work independently - no assumptions about watching other lessons
✅ **Natural Length**: Lessons should be as long or short as needed (1-20+ minutes) - never pad content
✅ **Clear and Accessible**: Target adult learners without assuming high academic background
✅ **Purpose-Driven Visuals**: Only include visual materials that enhance learning

## Lesson File Format

Each lesson is a Markdown file with this structure:

```markdown
# Lesson Title

**Section:** [Section Name]
**Lesson Number:** [X]
**Duration:** [Estimated minutes]

---

## Slide 1: [Title]

### Content
- Key points
- Formulas
- Concise information

### Narration
[Full word-for-word script for voiceover]

### Visual Materials
- **Type:** [None/Graph/Diagram/Animation]
- **Description:** [What it shows and why]
- **File:** [Reference to asset file]

---

[Additional slides follow the same pattern]
```

## Creating Animations

Animations are created using **Manim** (the same framework used by 3Blue1Brown). 

### When to Create Animations

Only create animations when motion/transformation adds clear learning value:
- ✅ Geometric transformations, graph plotting, equation morphing
- ❌ Static diagrams, decorative effects, simple text reveals

See **[animations/README.md](animations/README.md)** for:
- Installation instructions
- Creating and rendering animations
- Common Manim patterns for mathematics
- Best practices and guidelines

## Content Standards

### Slide Content
- Concise bullet points (3-5 per slide)
- Key formulas and equations
- Clear mathematical notation
- Easy to read and digest

### Narration
- Expands on slide content with detail
- Neutral, professional tone
- No time-based references (it's pre-recorded)
- No assumptions about prior lessons
- Target adult learners appropriately
- Clear explanations of "why" not just "how"

### Visual Materials
- Must serve a learning purpose
- No stock photos or decorative images
- Include: graphs, diagrams, geometric constructions, animations
- Always document type, description, and file reference

## Workflow

1. **Plan**: Determine lesson topic and key learning outcomes
2. **Structure**: Outline slides and main points
3. **Write Content**: Fill in slide content (concise) and narration (detailed)
4. **Identify Visuals**: Determine what diagrams/animations are needed
5. **Create Assets**: Build any required animations or diagrams
6. **Review**: Check against quality checklist in lesson guidelines
7. **Record**: Use narration script to record voiceover
8. **Build**: Create PowerPoint presentation from content
9. **Render**: Convert to video for Udemy

## Mathematical Notation

- Use standard mathematical notation throughout
- Be consistent with symbols across all lessons
- Variables: lowercase (x, y, n)
- Constants: uppercase or specific symbols (A, π)
- Clearly verbalize notation in narration scripts

## Version Control

This repository uses Git for version control:
- Commit completed lessons individually
- Use descriptive commit messages
- Create branches for major content additions or restructuring
- Each lesson file can be modified independently

## Contributing

When adding or modifying content:

1. Follow the established templates and guidelines
2. Ensure lessons are self-contained
3. Review the style guides before writing narration
4. Test that markdown renders correctly
5. Document any visual materials needed
6. Commit changes with clear messages

## Resources

### GCSE Maths Curriculum
- Familiarize yourself with official GCSE Maths specifications
- Cover Foundation and Higher tier topics as appropriate
- Ensure content aligns with exam board requirements

### Tools
- **Markdown Editor**: VS Code, Typora, or any preferred editor
- **Manim**: For mathematical animations
- **PowerPoint**: For slide creation
- **Screen Recording**: OBS, Camtasia, or similar for video creation

## Questions or Issues

If you need clarification on:
- Content structure or format
- Narration style
- Animation requirements
- Repository organization

Refer to the documentation in the `docs/` folder or review existing examples once lessons are created.

---

## Quick Reference

| Need to... | Go to... |
|------------|----------|
| Create a new lesson | `templates/lesson-template.md` |
| Learn about lesson structure | `docs/lesson-guidelines.md` |
| Understand narration style | `docs/narration-style-guide.md` |
| Create an animation | `animations/README.md` |
| Find lesson files | `lessons/section-XX-[name]/` |

---

**Course Target Audience**: Adults seeking GCSE Maths qualification
**Delivery Method**: Pre-recorded video lessons
**Content Format**: PowerPoint presentations with voiceover
**Repository Purpose**: Organize and version control all course content
