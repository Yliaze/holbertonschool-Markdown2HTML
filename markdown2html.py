#!/usr/bin/python3
"""Script that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name"""
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        """Error if (sys.argv) < 3"""
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        """Error sys.argv[1] doesn't exist"""
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)
    
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    """Open the markdown file"""
    with open(markdown_file, 'r', encoding='UTF-8') as file:
        all_lines = file.readlines()

        output_lines = []
        
        for lines in all_lines:
            if lines.startswith('#'):
                """Count number of #"""
                count = lines.count('#')
                """Suppr space and # from text"""
                text = lines[count:].strip()
                """Format text"""
                html_title = f'<h{count}>{text}</h{count}>\n'
                output_lines.append(html_title)
    
    """write in the html file"""
    with open(html_file, 'w') as output_file:
        output_file.writelines(output_lines)

exit(0)