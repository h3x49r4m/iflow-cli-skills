---
name: rst-writer
description: A skill for writing articles in reStructuredText (RST) format with 100% syntax accuracy.
license: Apache
---

# RST Writer

**Name**: rst-writer

**Description**: A skill for writing articles in reStructuredText (RST) format with 100% syntax accuracy.

**Trigger Conditions**:
This skill should be automatically invoked when:
- User requests to write an article in RST format
- User asks to create RST documentation
- User requests reStructuredText content generation
- Keywords: "rst", "restructuredtext", "write article", "create documentation", ".rst file"

**RST Syntax Requirements**:

### Section Headers
Headers use underlines and overlines (optional for top-level) with matching characters:

```
Title with Overline
===================

Section 1
---------

Subsection 1.1
~~~~~~~~~~~~~~

Sub-subsection 1.1.1
^^^^^^^^^^^^^^^^^^^^
```

**Rules**:
- Underline length must match text length exactly
- Overline is optional for top-level, required for all other levels
- Use distinct characters for each level: =, -, ~, ^, ", ', *, +, #

### Text Formatting
```
*italic*          - Single asterisks
**bold**          - Double asterisks
``monospace``     - Backticks
:emphasis:        - Role directive
:strong:          - Role directive
```

### Lists

**Bullet Lists**:
```
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```

**Enumerated Lists**:
```
1. First item
2. Second item
   a. Sub-item
   b. Another sub-item
3. Third item
```

**Definition Lists**:
```
Term 1
   Definition for term 1.

Term 2
   Definition for term 2.
```

### Code Blocks

**Literal Blocks** (with double colons):
```
This is a paragraph::

   This is a literal block
   Preserves whitespace
   All lines indented
```

**Code Blocks** (with directive):
```
.. code-block:: python

   def example():
       return "Hello, World!"
```

### Tables

**Simple Tables**:
```
=====  =====  ======
A      B      A and B
=====  =====  ======
False  False  False
True   False  False
True   True   True
=====  =====  ======
```

**Grid Tables**:
```
+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| cell 1     | cell 2     | cell 3    |
+------------+------------+-----------+
| cell 4     | cell 5     | cell 6    |
+------------+------------+-----------+
```

### Links and References

**External Links**:
```
`Link text <https://example.com>`_
```

**Internal References**:
```
.. _reference-label:

Section to reference
--------------------

See :ref:`reference-label`
```

**Hyperlink Targets**:
```
.. _my-anchor:

This is a section with an anchor.

Jump to :ref:`my-anchor`
```

### Directives

**Note/Warning/Tip**:
```
.. note::

   This is a note.

.. warning::

   This is a warning.

.. tip::

   This is a tip.
```

**Include Directive**:
```
.. include:: other_file.rst
```

**Image Directive**:
```
.. image:: path/to/image.png
   :alt: Alternative text
   :width: 200px
```

### Comments

```
.. This is a comment that won't appear in output
```

### Line Blocks

```
| Line 1
| Line 2
|   Indented line
| Line 3
```

### Field Lists

```
:Author: John Doe
:Date: 2026-02-09
:Version: 1.0
```

### Substitutions

```
.. |name| replace:: replacement text

Use |name| throughout the document.
```

### Footnotes

```
This is text with a footnote [#]_.

.. [#] This is the footnote text.
```

### Citations

```
This is a citation [CIT2001]_.

.. [CIT2001] Citation reference.
```

**Validation Checklist**:
- [ ] All section headers have matching underline/overline lengths
- [ ] Header hierarchy uses distinct characters consistently
- [ ] Code blocks use proper indentation (3 spaces minimum)
- [ ] Lists use consistent indentation
- [ ] Tables have proper column alignment
- [ ] Links use correct syntax (backticks for reference, angle brackets for URLs)
- [ ] Inline markup doesn't span multiple lines
- [ ] All directives end with double colon and proper indentation
- [ ] No unescaped special characters in text
- [ ] Blank lines before and after directives/code blocks

**Instructions**:

### When Invoked:
1. **Understand Requirements**: Identify the article topic, structure, and content requirements
2. **Plan Structure**: Create an outline with appropriate section hierarchy
3. **Generate Content**: Write the article following RST syntax rules
4. **Validate Syntax**: Verify 100% RST compliance using the validation checklist
5. **Output Result**: Provide the RST file content

### State Management:
- `current-article.md` - Track the article currently being written
- `next-steps.md` - Track remaining work
- `project-state.md` - Overall skill state

### Resume Commands:
- "continue writing" - Resume current article
- "what's next?" - Show next steps
- "validate rst" - Validate current RST content

### Quality Standards:
- 100% RST syntax accuracy
- Proper header hierarchy
- Correct indentation for all blocks
- Valid directive syntax
- Proper table formatting
- Correct link/reference syntax