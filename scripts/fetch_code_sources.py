#!/usr/bin/env python3
import os
import glob
import yaml
import subprocess
import urllib.request
import re

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    try:
        metadata = yaml.safe_load(parts[1])
        return metadata, parts[2]
    except Exception as e:
        print(f"Error parsing YAML: {e}")
        return None, content

def convert_tree_url_to_raw(url):
    # Convert github/gitee tree URL to a raw URL if it's a file, 
    # but these are mostly directories. 
    # We will just append a note to clone the repo path.
    return url

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    metadata, body = parse_frontmatter(content)
    if not metadata or 'url' not in metadata:
        return

    url = metadata['url']
    print(f"Processing {filepath} -> {url}")
    
    # If the file already has code appended, skip
    if "## Fetched Source" in body:
        print(" Already contains fetched source, skipping.")
        return

    repo = metadata.get('repo', '')
    path = metadata.get('path', '')
    
    # Create the markdown to append
    append_md = f"\n\n## Fetched Source\n\n"
    append_md += f"> **Note**: The source code for this component is located at the directory `/{path}` in the `{repo}` repository.\n"
    append_md += f"> \n> To explore the code locally, you can use a sparse checkout:\n"
    append_md += "```bash\n"
    append_md += f"git clone --filter=blob:none --sparse https://github.com/{repo}.git\n"
    append_md += f"cd {repo.split('/')[-1]}\n"
    append_md += f"git sparse-checkout add {path}\n"
    append_md += f"git checkout\n"
    append_md += "```\n"

    with open(filepath, 'a') as f:
        f.write(append_md)
    print(f" Updated {filepath}")

def main():
    search_path = os.path.join(os.path.dirname(__file__), '..', 'sources', 'code', '**', '*.md')
    files = glob.glob(search_path, recursive=True)
    
    for filepath in files:
        process_file(filepath)

if __name__ == "__main__":
    main()
