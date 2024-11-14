Title: Example Post
Date: 2024-11-14
Category: snippets
Tags: pelican, markdown, tutorial
Slug: example-post
Author: ChatGPT 4o
Summary: A quick overview of markdown formatting in Pelican.

# Example Markdown for Pelican Blog

Welcome to this example markdown file! If you're setting up a Pelican blog, it's helpful to understand how various formatting options will render in your new blog post. Here's a showcase of all the essential elements you can use with Pelican, including some Pelican-specific features.

## Headings

You can use different levels of headings to structure your content:

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
```

### Examples

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

---

## Text Formatting

Make your text stand out using basic Markdown formatting:

- **Bold text**: `**Bold**` → **Bold**
- *Italic text*: `*Italic*` → *Italic*
- ~~Strikethrough~~: `~~Strikethrough~~` → ~~Strikethrough~~
- `Inline code`: Use backticks (`) for inline code: `print("Hello, Pelican!")`

### Blockquotes

> You can create blockquotes to emphasize important points.

Use `>` followed by the text to create a blockquote, for example:

```markdown
> This is a blockquote.
```

## Lists

### Unordered List

- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2

### Ordered List

1. First item
2. Second item
   1. Sub-item 2.1
   2. Sub-item 2.2

## Links

Include links using:

```markdown
[OpenAI](https://www.openai.com)
```

[OpenAI](https://www.openai.com)

## Images

Add images to your posts using:

```markdown
![Alt text](https://example.com/image.jpg)
```

![Pelican Logo](https://upload.wikimedia.org/wikipedia/commons/8/8c/Pelican_logo.png)

## Code Blocks

You can add code blocks using triple backticks or indentation:

<pre>
```python
# Example Python code
for i in range(5):
    print("Hello, Pelican!")
```
</pre>

### Output

```python
# Example Python code
for i in range(5):
    print("Hello, Pelican!")
```

## Horizontal Rules

Create horizontal rules to separate sections:

```markdown
---
```

---

## Tables

Use tables to present data:

```markdown
| Header 1  | Header 2  |
| --------- | --------- |
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |
```

| Header 1  | Header 2  |
| --------- | --------- |
| Row 1 Col 1 | Row 1 Col 2 |
| Row 2 Col 1 | Row 2 Col 2 |

## Pelican-Specific Features

### Metadata

In Pelican, metadata is added to the top of the markdown file for each post:

```markdown
Title: Example Post
Date: 2024-11-14
Category: Markdown Tutorial
Tags: pelican, markdown, tutorial
Slug: example-post
Author: Your Name
Summary: A quick overview of markdown formatting in Pelican.
```

### Pelican Plugins

You can use various plugins to enhance your Pelican posts:

- **Tipue Search**: Add search functionality to your site.
- **Neighbors**: Easily link to previous/next articles within the template.
- **Summary**: Control the summary of your posts that are displayed on the main page by adding the `<!-- PELICAN_END_SUMMARY -->` tag.

### Inserting Summary Split

Control how much of your article shows up in a summary view by using the Pelican-specific tag:

```markdown
This is the beginning of the article, and it will appear in the summary.

<!-- PELICAN_END_SUMMARY -->

This part appears only in the full article.
```

## Embedding Media

### YouTube Videos

Embed a YouTube video in Pelican using an HTML snippet:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe>
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allowfullscreen></iframe>

## Footnotes

Add footnotes to provide additional information without cluttering the text:

```markdown
This is a statement with a footnote.[^1]

[^1]: This is the footnote text.
```

This is a statement with a footnote.[^1]

[^1]: This is the footnote text.

## Math Equations

Pelican also allows you to include LaTeX-style math expressions if you enable math rendering:

```markdown
$$
e^{i \pi} + 1 = 0
$$
```

$$
e^{i \pi} + 1 = 0
$$

## Conclusion

This example covers the main formatting features you can use in Pelican for writing blog posts. You can mix and match these elements to create rich and engaging content for your readers. Feel free to experiment with different markdown and Pelican-specific options to see what best fits your style!

Happy blogging with Pelican!

