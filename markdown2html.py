#!/usr/bin/python3
"""Markdown2 rebuilt"""


import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # Error if (sys.argv) < 3
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
        
    if not os.path.exists(sys.argv[1]):
        # Error sys.argv[1] doesn't exist
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)
        
    readme = sys.argv[1]
    readhtml = sys.argv[2]
    
    # Open the markdown file
    with open(readme, 'r', encoding='utf-8') as readme_file:
        lines = readme_file.readlines()
        
        # write in the html file
        with open(readhtml, 'w', encoding='utf-8') as tohtml:
            in_list = False
            in_ord_list = False
            in_p = False

            # Browse each line
            for line in lines:

                # Closes tags if still open
                if in_list and not line.startswith("-"):
                    tohtml.write("</ul>\n")
                    in_list = False
                if in_ord_list and not line.startswith("*"):
                    tohtml.write("</ol>\n")
                    in_ord_list = False
                if in_p and (line.startswith("-") or line.startswith("*") or
                               line.startswith("#") or line.startswith("\n")):
                    tohtml.write("</p>\n")
                    in_p = False

                # Start with #
                if line.startswith('#'):
                    # Count number of #
                    count = 0
                    for char in line:
                        if char == '#':
                            count += 1
                    # Write headings with right number
                    if count > 0:
                        tohtml.write(f"<h{count}>{line.strip('#').strip()}</h{count}>\n")

                # List start with -
                elif line.startswith('-'):
                    if not in_list:
                        tohtml.write("<ul>\n")
                        in_list = True
                    tohtml.write(f"<li>{line.lstrip('-').strip()}</li>\n")

                # List start with *    
                elif line.startswith('*'):
                    if not in_ord_list:
                        tohtml.write("<ol>\n")
                        in_ord_list = True
                    tohtml.write(f"<li>{line.lstrip('*').strip()}</li>\n")
                
                elif not line.startswith('\n'):
                    if not in_p:
                        tohtml.write("<p>\n")
                        in_p = True
                    else:
                        tohtml.write("<br />\n")
                    tohtml.write(f"{line.strip()}\n")
