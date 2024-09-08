import re
import webbrowser
import os

def bbcode_to_html(bbcode):
    """ Converts BBCode to HTML. """
    
    bbcode = bbcode.replace("\n", "<br>") # Replace newline characters with <br> for HTML line breaks
    
    conversions = {
        r'\[b\](.*?)\[/b\]': r'<strong>\1</strong>',
        r'\[i\](.*?)\[/i\]': r'<em>\1</em>',
        r'\[u\](.*?)\[/u\]': r'<u>\1</u>',
        r'\[hr\]': r'<hr>',
        r'\[align=(center|left|right|justify)\](.*?)\[/align\]': r'<div style="text-align:\1;">\2</div>',
        r'\[size=(\d+)\](.*?)\[/size\]': lambda m: f'<span style="font-size:{12 if int(m.group(1)) <= 4 else max(8, int(m.group(1)) * 5)}px;">{m.group(2)}</span>',  # Adjust 5 to (3-8) for [size]
        r'\[font=(.*?)\](.*?)\[/font\]': r'<span style="font-family:\'\1\';">\2</span>',
        r'\[url\](.*?)\[/url\]': r'<a href="\1">\1</a>',
        r'\[url=(.*?)\](.*?)\[/url\]': r'<a href="\1">\2</a>',
        r'\[img\](.*?)\[/img\]': r'<img src="\1" />',
        r'\[color=(.*?)\](.*?)\[/color\]': r'<span style="color:\1;">\2</span>',
        r'\[list\](.*?)\[/list\]': r'<ul>\1</ul>',
        r'\[li\](.*?)\[/li\]': r'<li>\1</li>'
    }

    # Convert BBCode to HTML
    html = bbcode
    for bb, html_tag in conversions.items():
        html = re.sub(bb, html_tag, html, flags=re.DOTALL)

    return f"<html><body>{html}</body></html>"

def read_bbcode_from_file(file_path):
    """ Read BBCode from a text file. """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    file_path = input("Enter the path to the BBCode text file: ")
    bbcode_input = read_bbcode_from_file(file_path)
    html_content = bbcode_to_html(bbcode_input)

    # Save to HTML file
    output_file_path = os.path.join(os.path.dirname(file_path), 'output.html')
    with open(output_file_path, 'w') as file:
        file.write(html_content)

    # Open in browser
    webbrowser.open(output_file_path)

if __name__ == "__main__":
    main()
