# Lesson Creation Guidelines

This document outlines the standards and best practices for creating lessons for the Udemy GCSE Maths Course.

---

## General Principles

### Self-Contained Lessons
- Each lesson must be completely self-contained
- Never reference other lessons by name or assume prior completion
- If a concept from another lesson is needed, briefly recap it
- Lessons can be taken in any order, so dependencies must be minimized

### Lesson Length
- **Quality over quantity**: Never pad content to reach a specific duration
- A lesson should be exactly as long as needed to teach the concept effectively
- Simple concepts: 1-3 minutes (2-4 slides) is perfectly acceptable
- Complex concepts: 15-20+ minutes if necessary
- Let the content dictate the length

---

## Slide Content Guidelines

### Keep It Concise
- Slides are for KEY POINTS only
- Use bullet points, not paragraphs
- Maximum 3-5 bullet points per slide
- Each point should be one line if possible

### Mathematical Content
- Include formulas, equations, and worked examples on slides
- Use clear notation that's consistent throughout the course
- For LaTeX/mathematical notation in markdown, use standard conventions
- Example: `a² + b² = c²` or use proper LaTeX if rendering is available

### Language and Readability
- Use simple, clear language
- Avoid jargon without explanation
- Break complex ideas into smaller chunks
- Use specific numbers and examples over abstract descriptions

### What Belongs on Slides
✅ Key formulas and equations
✅ Important definitions
✅ Step-by-step worked examples
✅ Summary bullet points
✅ Key takeaways

❌ Long explanations (save for narration)
❌ Full sentences when a phrase will do
❌ Multiple concepts per slide (split them up)
❌ Decorative or filler content

---

## Visual Materials Guidelines

### When to Include Visual Materials

**ALWAYS include for:**
- Graphs and coordinate geometry
- Geometric shapes, angles, and diagrams
- Data visualization (charts, tables)
- Step-by-step geometric constructions
- Visual proof demonstrations

**CONSIDER including for:**
- Complex formula derivations that benefit from visual breakdown
- Number line representations
- Fraction/percentage visualizations
- Pattern recognition exercises

**NEVER include:**
- Stock photos of people, classrooms, or unrelated objects
- Decorative graphics without learning value
- Images that repeat what text already clearly states

### Types of Visual Materials

1. **Static Images/Diagrams**
   - Hand-drawn style diagrams
   - Graphs plotted on coordinate systems
   - Geometric constructions
   - Labeled diagrams

2. **Animations (Manim)**
   - Use ONLY when motion/transformation adds learning value
   - Examples: rotating shapes, morphing equations, building graphs step-by-step
   - Avoid over-animation - simple is better
   - Consider production time vs. learning benefit

3. **Worked Examples**
   - Visual step-by-step solutions
   - Highlighting changes between steps
   - Color coding to show relationships

### Visual Material Documentation
Always specify:
- **Type**: What kind of visual aid
- **Description**: What it shows and why it's pedagogically valuable
- **File reference**: Where the asset will be stored

---

## Mathematical Notation Standards

### General Format
- Use clear, standard mathematical notation
- Be consistent with symbols throughout all lessons
- Define any non-standard notation when first introduced

### Common Conventions
- Variables: Use lowercase letters (x, y, n)
- Constants: Use uppercase or specific symbols (A for area, π for pi)
- Operations: Standard symbols (+, -, ×, ÷)
- Exponents: Use superscript notation (x²)
- Fractions: Use proper fraction notation where possible

### Worked Examples Format
```
Problem: [State the problem clearly]

Step 1: [First step with explanation]
Step 2: [Second step with explanation]
...
Answer: [Final answer clearly stated]
```

---

## Quality Checklist

Before finalizing a lesson, verify:

- [ ] Can this lesson be understood without watching other lessons?
- [ ] Is every slide clear and concise?
- [ ] Does the narration expand appropriately on slide content?
- [ ] Are all visual materials necessary and valuable for learning?
- [ ] Is the language appropriate for adult GCSE learners?
- [ ] Are all mathematical notations standard and consistent?
- [ ] Is the lesson exactly as long as it needs to be (no padding)?
- [ ] Would this be clear to someone who struggled with maths at school?

---

## Tips for Effective Lessons

1. **Start with the "why"**: Help learners understand why this concept matters
2. **Use concrete examples**: Real numbers and scenarios before abstract concepts
3. **Build gradually**: Start simple, add complexity incrementally
4. **Check understanding**: Include practice problems or examples to verify comprehension
5. **End with a summary**: Recap the key points at the end

---

## Lesson Naming Convention

When creating lesson files:
- Format: `lesson-XX-descriptive-name.md`
- Place in appropriate section folder: `lessons/section-YY-[section-name]/`
- Use descriptive names that indicate content: `lesson-01-introduction-to-algebra.md`
