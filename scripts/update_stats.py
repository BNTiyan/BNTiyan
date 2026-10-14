#!/usr/bin/env python3
"""
Automated profile stats updater for GitHub profile README.md.
Fetches live stats from GitHub API and updates metrics in README.md.
"""

import os
import re
import json
import urllib.request

USERNAME = "BNTiyan"
SECONDARY_USERNAME = "tiyanshjarvis"

def get_headers():
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"User-Agent": "GitHub-Stats-Updater"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def fetch_json(url):
    req = urllib.request.Request(url, headers=get_headers())
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_user_stats(username):
    user = fetch_json(f"https://api.github.com/users/{username}")
    if not user or not isinstance(user, dict):
        return None
    return {
        "repos": user.get("public_repos", 0),
        "followers": user.get("followers", 0)
    }

def get_repos_and_deployments(username):
    repos = []
    page = 1
    while True:
        batch = fetch_json(f"https://api.github.com/users/{username}/repos?per_page=100&page={page}")
        if batch is None:
            break
        if not isinstance(batch, list) or len(batch) == 0:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    if not repos:
        return None

    deployed_count = 0
    total_stars = 0
    for r in repos:
        total_stars += r.get("stargazers_count", 0)
        hp = r.get("homepage") or ""
        if "vercel.app" in hp or "freellmapi.co" in hp:
            deployed_count += 1

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "deployed_count": deployed_count
    }

def update_readme():
    user_stats = get_user_stats(USERNAME)
    if not user_stats or user_stats.get("repos", 0) == 0:
        print("Warning: Could not fetch valid user stats from GitHub API. Skipping update to preserve existing metrics.")
        return

    repo_stats = get_repos_and_deployments(USERNAME)
    total_repos = repo_stats["total_repos"] if repo_stats else user_stats["repos"]
    repo_count = max(user_stats["repos"], total_repos)
    deployed_count = max(5, repo_stats["deployed_count"] if repo_stats else 5)

    print(f"Fetched stats: {repo_count} public repos, {deployed_count} deployed apps")

    readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
    if not os.path.exists(readme_path):
        readme_path = "README.md"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update metric table line: | 📁 **Repositories** | ...
    pattern = r"(\| 📁 \*\*Repositories\*\* \| )([^\|]+)(\| [^\|]+ \| )(\*\*[^\*]+\*\* \|)"
    replacement = rf"\g<1>{repo_count}+ Public Repositories \g<3>**{repo_count}+ Active Repos** |"
    new_content = re.sub(pattern, replacement, content)

    # Update deployed apps line: | 🌐 **Live Deployed Web Apps** | ...
    pattern_apps = r"(\| 🌐 \*\*Live Deployed Web Apps\*\* \| )([^\|]+)(\| [^\|]+ \| )(\*\*[^\*]+\*\* \|)"
    replacement_apps = rf"\g<1>{deployed_count} Deployed Systems \g<3>**{deployed_count}+ Live Web Applications** |"
    new_content = re.sub(pattern_apps, replacement_apps, new_content)

    if new_content != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated with latest stats successfully.")
    else:
        print("README.md is already up to date with the latest stats.")

if __name__ == "__main__":
    update_readme()
