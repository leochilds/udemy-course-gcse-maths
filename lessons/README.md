# Lessons Folder

This folder contains all lesson content for the GCSE Maths Udemy course, organized by section.

## Structure

Lessons are organized into sections (topics) with each lesson as a separate markdown file:

```
lessons/
├── section-01-[topic-name]/
│   ├── lesson-01-[name].md
│   ├── lesson-02-[name].md
│   └── ...
├── section-02-[topic-name]/
│   ├── lesson-01-[name].md
│   └── ...
└── ...
```

## Section Organization

Sections should follow the GCSE Maths curriculum structure. Example sections might include:

- **section-01-number**: Basic number operations, fractions, decimals, percentages
- **section-02-algebra**: Equations, expressions, graphs, sequences
- **section-03-geometry**: Shapes, angles, area, volume, Pythagoras
- **section-04-ratio-proportion**: Ratios, proportions, rates
- **section-05-statistics**: Data collection, averages, charts, probability
- **section-06-trigonometry**: Sine, cosine, tangent, applications

(Adapt to your specific curriculum structure)

## Naming Conventions

### Section Folders
Format: `section-XX-topic-name`
- `XX`: Two-digit section number (01, 02, 03...)
- `topic-name`: Descriptive name in lowercase with hyphens

Examples:
- `section-01-number`
- `section-02-algebra`
- `section-03-geometry`

### Lesson Files
Format: `lesson-XX-descriptive-name.md`
- `XX`: Two-digit lesson number within the section (01, 02, 03...)
- `descriptive-name`: Clear description of lesson content

Examples:
- `lesson-01-adding-fractions.md`
- `lesson-02-subtracting-fractions.md`
- `lesson-03-multiplying-fractions.md`

## Creating a New Lesson

1. **Determine section**: Identify which section your lesson belongs to
2. **Create section folder** (if it doesn't exist):
   ```bash
   mkdir lessons/section-XX-topic-name
   ```
3. **Copy template**:
   ```bash
   cp templates/lesson-template.md lessons/section-XX-topic-name/lesson-YY-name.md
   ```
4. **Edit the file**: Fill in all sections according to the guidelines
5. **Review**: Check against the quality checklist in `docs/lesson-guidelines.md`

## Lesson Independence

**CRITICAL**: Each lesson must be self-contained and work independently:
- Never reference specific other lessons
- Don't assume prior knowledge from other lessons
- If a concept from elsewhere is needed, briefly recap it
- Students should be able to take lessons in any order

## Lesson Content Requirements

Every lesson file must include:

### Metadata
- Lesson title
- Section name
- Lesson number
- Estimated duration (can be filled after creation)

### For Each Slide
- **Content**: Concise bullet points for the slide
- **Narration**: Complete word-for-word script
- **Visual Materials**: Specification of any diagrams, graphs, or animations

### Notes Section
- Additional references
- Production notes
- Any special considerations

## Quality Standards

Before considering a lesson complete, ensure:

✅ All slides have content, narration, and visual specifications
✅ Narration follows the style guide (see `docs/narration-style-guide.md`)
✅ Slide content is concise and digestible
✅ Visual materials serve a clear learning purpose
✅ Lesson is self-contained
✅ Mathematical notation is standard and consistent
✅ Language is appropriate for adult learners
✅ No time-based references in narration
✅ No assumptions about prior lessons

## Example Structure

See `section-01-example/lesson-01-example.md` for a complete example of proper formatting.

## Tips

1. **Start small**: Begin with simple lessons to get comfortable with the format
2. **Review guidelines**: Keep `docs/lesson-guidelines.md` and `docs/narration-style-guide.md` handy
3. **Be consistent**: Use the same formatting and style across all lessons
4. **Test your narration**: Read it aloud to ensure it flows naturally
5. **Think pedagogically**: Every element should serve the learning objective

## Moving or Reorganizing Lessons

Since lessons are self-contained:
- Lessons can be moved between sections easily
- Lesson numbers can be changed by renaming files
- Sections can be reordered without breaking references
- Use git to track changes when reorganizing

## Version Control

- Commit each completed lesson individually
- Use descriptive commit messages: "Add lesson on adding fractions"
- Review changes before committing
- Each lesson file is independent in version control
