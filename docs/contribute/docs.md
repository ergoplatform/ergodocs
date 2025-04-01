# Contributing to the Documentation

We appreciate your interest in contributing to our documentation. Your assistance is invaluable, and we aim to make the contribution process as straightforward as possible.

## Prerequisites for Contribution

Before you start contributing, ensure you have the following set up on your system:

- A GitHub account for version control and collaboration.
- Python (3.7 or higher) if you plan to build the documentation locally.

## How to Contribute

There are two ways you can contribute to these docs:

### Minor Changes

For minor changes, simply log into GitHub, click the *edit* arrow at the top-right of this page. After saving, you'll have the option to open a pull request.

### Major Changes

For major changes, you'll need to set up your development environment locally. Follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ergoplatform/ergodocs.git
```

2. Install dependencies:

```bash
cd mkdocs-project
pip install -r requirements.txt
```

3. Build the project:

```bash
mkdocs build
```

4. Start the development server:

```bash
mkdocs serve
```

5. Open the documentation in your browser:

```
http://127.0.0.1:8000/
```

Make your changes locally and submit a pull request when you're done.

## Guidelines

### Writing Style

- Write in clear, concise, and grammatically correct English.
- Use appropriate formatting, such as bold or italics, to emphasize key points.
- Keep paragraphs and sections short and focused on a single topic.

### Code Style

- Follow the code style conventions used throughout the project.
- Include comments and explanations to make the code easy to understand.
- Use code-blocks with syntax highlighting. 

### Commit Messages

- Write clear, concise, and meaningful commit messages.
- Use the imperative form, e.g., "Add feature" rather than "Added feature" or "Adding feature".
- Use sentence capitalization, i.e., capitalize the first letter of the message, but not the rest.

## Notes

### Navigation

The mkdocs navigation is built using `mkdocs.yml`. To add, remove or modify pages in the navigation, edit the `nav` section in the `mkdocs.yml` file.

### Directory Structure

The directory structure should follow this pattern:

```
- Parent Directory:
    - index.md
    - Sub-Directory:
        - SubDirectoryPage: subdirectorypage.md
    - ParentDirectoryPage: parentdirectorypage.md
```

### TODOs

To leave comments in the file itself and have them not visible on the live site, you can use the HTML comment codes:

```html
<!-- TODO: Add information about XYZ here -->
```

## Submitting a Pull Request

When you're ready to submit your changes, follow these steps:

1. Commit your changes to a new branch:

```bash
git checkout -b my-feature-branch
git add .
git commit -m "Add my awesome feature"
```

2. Push your changes to your fork:

```bash
git push origin my-feature-branch
```

3. Open a pull request on the original repository:

Go to the original repository on GitHub and click on the "Pull Requests" tab. Then, click on the "New Pull Request" button and select your fork and branch to create the pull request.

Please include a descriptive title and a detailed description of your changes.

## Review Process

Once your pull request is submitted, our team will review your changes. We may request additional changes or clarification before merging your pull request. Please be patient, as we want to ensure that the documentation remains high-quality and consistent.


## MkDocs formatting

rST suggests the following “types”: attention, caution, danger, error, hint, important, note, tip, and warning; however, you’re free to use whatever you want.


```
/// admonition | Some title
    type: warning

Some content
///
```

/// admonition | Some title
    type: warning

Some content
///

```
/// note | Some title
Some content
///
```

/// note | Some title
Some content
///

note, attention, caution, danger, error, tip, hint, warning.

/// admonition | note
    type: note

Some note
///

/// admonition | caution
    type: caution

Some caution
///

/// admonition | danger
    type: danger

Some danger
///

/// admonition | error
    type: error

Some error
///


/// admonition | tip
    type: tip

Some tip
///



/// admonition | hint
    type: hint

Some hint
///

/// admonition | warning
    type: warning

Some warning
///
