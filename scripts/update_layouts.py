import os
import re

def update_layouts(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            print(f"Processing {filename}...")
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Match front matter: text between first and second ---
            # Using MULTILINE and DOTALL to handle various structures
            match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if match:
                front_matter = match.group(1)
                rest_of_file = content[match.end():]
                
                # Check for existing layout key
                layout_match = re.search(r'^layout:.*$', front_matter, re.MULTILINE)
                if layout_match:
                    # Overwrite
                    new_front_matter = re.sub(r'^layout:.*$', 'layout: default', front_matter, flags=re.MULTILINE)
                else:
                    # Insert at the top
                    new_front_matter = "layout: default\n" + front_matter
                
                new_content = "---\n" + new_front_matter + "\n---\n" + rest_of_file
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            else:
                print(f"No front matter found in {filename}")

if __name__ == "__main__":
    update_layouts('_posts')
