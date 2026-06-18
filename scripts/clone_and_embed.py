#!/usr/bin/env python3
import os
import glob
import yaml
import subprocess
import shutil

REPOS = {
    'vllm-project/vllm-ascend': 'https://github.com/vllm-project/vllm-ascend.git',
    'Ascend/cann-ops-adv': 'https://gitee.com/ascend/cann-ops-adv.git',
    'Ascend/catlass': 'https://gitee.com/ascend/catlass.git',
    'sgl-project/sgl-kernel-npu': 'https://github.com/sgl-project/sgl-kernel-npu.git',
    'Ascend/samples': 'https://gitee.com/ascend/samples.git'
}

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

def clone_repos(base_dir):
    repo_dir = os.path.join(base_dir, 'tmp_repos')
    os.makedirs(repo_dir, exist_ok=True)
    
    for repo_name, url in REPOS.items():
        local_path = os.path.join(repo_dir, repo_name.replace('/', '_'))
        if not os.path.exists(local_path):
            print(f"Cloning {url} into {local_path}...")
            # Use depth=1 to make it faster
            cmd = ['git', 'clone', '--depth', '1', url, local_path]
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to clone {url}: {e}")
        else:
            print(f"Repo {local_path} already exists. Skipping clone.")
    return repo_dir

def get_code_from_path(local_repo_path, target_path):
    full_path = os.path.join(local_repo_path, target_path)
    if not os.path.exists(full_path):
        return f"// Path {target_path} not found in repo."
    
    output = ""
    if os.path.isfile(full_path):
        with open(full_path, 'r', errors='ignore') as f:
            content = f.read()
        ext = os.path.splitext(full_path)[1].lower()
        lang = 'cpp' if ext in ['.cpp', '.h', '.c', '.hpp'] else ('python' if ext == '.py' else '')
        output += f"\n### `{os.path.basename(full_path)}`\n```{lang}\n{content[:5000]}"
        if len(content) > 5000:
            output += "\n// ... (truncated due to length) ...\n"
        output += "\n```\n"
    elif os.path.isdir(full_path):
        # find up to 3 cpp/py/h files
        files = []
        for root, _, filenames in os.walk(full_path):
            for filename in filenames:
                if filename.endswith(('.cpp', '.h', '.py')):
                    files.append(os.path.join(root, filename))
            if len(files) >= 3:
                break
        
        if not files:
            return "// No source files found in directory."
            
        for filepath in files[:3]:
            with open(filepath, 'r', errors='ignore') as f:
                content = f.read()
            ext = os.path.splitext(filepath)[1].lower()
            lang = 'cpp' if ext in ['.cpp', '.h', '.c', '.hpp'] else ('python' if ext == '.py' else '')
            rel_path = os.path.relpath(filepath, local_repo_path)
            output += f"\n### `{rel_path}`\n```{lang}\n{content[:5000]}"
            if len(content) > 5000:
                output += "\n// ... (truncated due to length) ...\n"
            output += "\n```\n"
    return output

def process_file(filepath, repo_dir):
    with open(filepath, 'r') as f:
        content = f.read()
    
    metadata, body = parse_frontmatter(content)
    if not metadata or 'repo' not in metadata or 'path' not in metadata:
        return

    repo = metadata['repo']
    path = metadata['path']
    
    # Try to match the repo to our cloned dirs
    # E.g. "Ascend/cann-ops-adv" might be "Ascend_cann-ops-adv"
    # But sometimes the case is different, or it's just 'vllm-project/vllm-ascend'
    # Check REPOS keys case-insensitively
    matched_repo_key = None
    for k in REPOS.keys():
        if k.lower() == repo.lower():
            matched_repo_key = k
            break
            
    if not matched_repo_key:
        print(f"Repo {repo} not in REPOS list.")
        return

    local_repo_path = os.path.join(repo_dir, matched_repo_key.replace('/', '_'))
    
    print(f"Extracting code for {filepath}...")
    code_md = get_code_from_path(local_repo_path, path)
    
    # Replace the Fetched Source section
    if "## Fetched Source" in content:
        parts = content.split("## Fetched Source")
        new_content = parts[0] + "## Fetched Source\n\n" + code_md
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f" Updated {filepath}")

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    repo_dir = clone_repos(base_dir)
    
    search_path = os.path.join(base_dir, 'sources', 'code', '**', '*.md')
    files = glob.glob(search_path, recursive=True)
    
    for filepath in files:
        process_file(filepath, repo_dir)

if __name__ == "__main__":
    main()
