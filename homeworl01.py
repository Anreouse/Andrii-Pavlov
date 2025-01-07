import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html = file.read()
    except FileNotFoundError:
        print(f"Error: The file {html_file} was not found.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return
    cleaned_text = re.sub(r'<[^>]+>', '', html)
    cleaned_text = '\n'.join(line for line in cleaned_text.splitlines() if line.strip())

    try:
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(cleaned_text)
        print(f"Cleaned text has been saved to {result_file}")
    except Exception as e:
        print(f"Error writing to the file: {e}")

delete_html_tags('draft.html')