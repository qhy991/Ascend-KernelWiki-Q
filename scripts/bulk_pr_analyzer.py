#!/usr/bin/env python3
import json
import os
import re

# We will read all the JSON files in the scratch directory
SCRATCH_DIR = "/Users/haiyan-mini/.gemini/antigravity/brain/94869b0c-ed94-4506-a713-22e5e2ffceaa/scratch"
OUTPUT_DIR = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/techniques"

JSON_FILES = [
    "pr_research.json",
    "pr_research_2.json",
    "pr_research_3.json",
    "pr_research_catlass.json"
]

def analyze_tags(title, body):
    text = (title + " " + body).lower()
    tags = []
    if any(k in text for k in ['l1', 'ub', 'cache', 'swap', 'oom', 'memory']):
        tags.append('memory-optimization')
    if any(k in text for k in ['cube', 'vector', 'matmul', 'flash', 'attention', 'moe', 'compute']):
        tags.append('compute')
    if any(k in text for k in ['hccs', 'ring', 'allreduce', 'all-to-all', 'tp', 'pp', 'distribute']):
        tags.append('communication')
    if any(k in text for k in ['fp8', 'w8a16', 'int8', 'quant', 'scale']):
        tags.append('quantization')
    if any(k in text for k in ['ci', 'doc', 'readme', 'bugfix', 'fix', 'test', 'misc']):
        tags.append('maintenance')
    
    if not tags:
        tags.append('general')
    return tags

def determine_url(repo_key, number):
    if 'vllm' in repo_key.lower():
        return f"https://github.com/vllm-project/vllm-ascend/pull/{number}"
    elif 'sgl' in repo_key.lower():
        return f"https://github.com/sgl-project/sgl-kernel-npu/pull/{number}"
    elif 'cann' in repo_key.lower():
        return f"https://gitee.com/ascend/cann-ops-adv/pulls/{number}"
    elif 'mindspeed' in repo_key.lower():
        return f"https://gitee.com/ascend/MindSpeed/pulls/{number}"
    elif 'modellink' in repo_key.lower():
        return f"https://gitee.com/ascend/ModelLink/pulls/{number}"
    elif 'catlass' in repo_key.lower():
        return f"https://gitee.com/ascend/catlass/pulls/{number}"
    else:
        return f"https://github.com/unknown/pull/{number}"

def format_repo_name(repo_key):
    return repo_key.replace(' (page 2)', '').strip()

def sanitize_title(title):
    return title.replace('"', "'").replace("\n", " ")

def generate_markdown(repo, number, title, body, tags, url):
    repo_slug = format_repo_name(repo).lower()
    file_name = f"pr-bulk-{repo_slug}-{number}.md"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    
    # Check if we already created a manual page for this PR to avoid duplicates.
    # Manual pages have names like pr-cann-pfa-l1-reuse.md, but they contain the URL.
    # To keep it simple, we just write all of them with the `pr-bulk-` prefix.
    # If the user really wants ALL PRs, we give them all.
    
    tags_yaml = "\n".join([f"  - {t}" for t in tags])
    
    body_clean = body.replace('\r\n', '\n').strip()
    if not body_clean:
        body_clean = "No description provided."
        
    markdown_content = f"""---
id: technique-pr-bulk-{repo_slug}-{number}
title: "PR Insight: {format_repo_name(repo)} #{number}"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
{tags_yaml}
confidence: inferred
sources:
  - "{url}"
---

# PR Insight: {format_repo_name(repo)} PR #{number}

**Source:** [{format_repo_name(repo)} PR #{number}]({url})

## Title
**{title}**

## Heuristic Analysis
Based on keyword heuristics, this PR impacts the following areas: {', '.join(tags)}.

## Original Description
```text
{body_clean}
```
"""
    with open(file_path, 'w') as f:
        f.write(markdown_content)

def main():
    total_generated = 0
    for json_file in JSON_FILES:
        full_path = os.path.join(SCRATCH_DIR, json_file)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r') as f:
            data = json.load(f)
            
        for repo_key, prs in data.items():
            for pr in prs:
                number = pr['number']
                title = sanitize_title(pr['title'])
                body = pr.get('body', '')
                tags = analyze_tags(title, body)
                url = determine_url(repo_key, number)
                
                generate_markdown(repo_key, number, title, body, tags, url)
                total_generated += 1
                
    print(f"Successfully generated {total_generated} PR Markdown pages.")

if __name__ == "__main__":
    main()
