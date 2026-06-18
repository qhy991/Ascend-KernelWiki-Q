#!/usr/bin/env python3
import json
import os

SCRATCH_DIR = "/Users/haiyan-mini/.gemini/antigravity/brain/94869b0c-ed94-4506-a713-22e5e2ffceaa/scratch"
OUTPUT_FILE = "/Users/haiyan-mini/.gemini/antigravity/brain/94869b0c-ed94-4506-a713-22e5e2ffceaa/scratch/pr_checklist.md"

JSON_FILES = [
    "pr_research.json",
    "pr_research_2.json",
    "pr_research_3.json",
    "pr_research_catlass.json"
]

# We need to filter out the ones we already did in Phase 4, 5, 6, 7:
ALREADY_DONE = [
    ("vllm-project/vllm-ascend", 10026),
    ("vllm-project/vllm-ascend", 10617),
    ("vllm-project/vllm-ascend", 10199),
    ("sgl-project/sgl-kernel-npu", 268),
    ("sgl-project/sgl-kernel-npu", 546),
    ("sgl-project/sgl-kernel-npu", 540),
    ("sgl-project/sgl-kernel-npu", 517),
    ("sgl-project/sgl-kernel-npu", 515),
    ("sgl-project/sgl-kernel-npu", 503),
    ("ascend/cann-ops-adv", 84),
    ("ascend/cann-ops-adv", 58),
    ("ascend/MindSpeed", 2671),
    ("ascend/MindSpeed", 2825),
    ("ascend/MindSpeed", 2829),
    ("ascend/MindSpeed", 2721),
    ("ascend/catlass", 238),
    ("ascend/catlass", 201),
    ("ascend/catlass", 266),
    ("ascend/catlass", 282),
    ("ascend/catlass", 123)
]

def format_repo_name(repo_key):
    # Some keys have ' (page 2)' etc. Map them to a cleaner name.
    if 'vllm' in repo_key.lower():
        return "vllm-project/vllm-ascend"
    elif 'sgl' in repo_key.lower():
        return "sgl-project/sgl-kernel-npu"
    elif 'cann' in repo_key.lower():
        return "ascend/cann-ops-adv"
    elif 'mindspeed' in repo_key.lower():
        return "ascend/MindSpeed"
    elif 'modellink' in repo_key.lower():
        return "ascend/ModelLink"
    elif 'catlass' in repo_key.lower():
        return "ascend/catlass"
    else:
        return repo_key

def sanitize_title(title):
    return title.replace('"', "'").replace('\n', ' ')

def main():
    checklist = ["# Phase 8 Tasks: Agent-driven PR Analysis\n"]
    
    # Track to avoid duplicates if PR is in multiple pages
    seen = set()
    
    for json_file in JSON_FILES:
        full_path = os.path.join(SCRATCH_DIR, json_file)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r') as f:
            data = json.load(f)
            
        for repo_key, prs in data.items():
            repo_name = format_repo_name(repo_key)
            for pr in prs:
                num = pr['number']
                if (repo_name, num) in ALREADY_DONE:
                    continue
                if (repo_name, num) in seen:
                    continue
                
                # Check for completely useless CI/Doc ones to save token space if desired.
                # But the user said "EVERY PR". We will let the Agent decide if it's maintenance.
                
                seen.add((repo_name, num))
                title = sanitize_title(pr['title'])
                
                checklist.append(f"- [ ] {repo_name} #{num}: {title}")
                
    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(checklist))
        
    print(f"Generated checklist with {len(seen)} PRs.")

if __name__ == "__main__":
    main()
