import re

def modify_headings_and_code_blocks(file_path):
    # Regular expressions for HTML and Markdown headings
    html_h1_pattern = re.compile(r'<h1.*?>(.*?)</h1>')
    html_h2_pattern = re.compile(r'<h2.*?>(.*?)</h2>')
    md_heading_pattern = re.compile(r'(#+) ')

    # Regular expression to find code blocks
    code_pattern = re.compile(r'```(\w+)\n(.*?)```', re.DOTALL)

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace HTML headings with Markdown headings
    content = html_h1_pattern.sub(r'# \1', content)
    content = html_h2_pattern.sub(r'## \1', content)

    # Function to increase Markdown heading levels
    def increase_heading_level(match):
        return '#' + match.group(0)

    # Increase Markdown heading levels by one
    content = md_heading_pattern.sub(increase_heading_level, content)

    # Function to replace each match in code blocks
    def replacer(match):
        language = match.group(1)
        code = match.group(2).rstrip()  # Remove trailing white spaces and newlines
        aligned_code = '\n'.join('    ' + line for line in code.split('\n'))
        return f'=== "{language}"\n\n    ```{language}\n{aligned_code}\n    ```'

    # Replace all matches in code blocks
    modified_content = code_pattern.sub(replacer, content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Example usage
file_path = 'openapi.md'  # Replace with your markdown file path
modify_headings_and_code_blocks(file_path)
