import os
import subprocess
from pathlib import Path

import git


def clone_repo(remote_url, target_dir):
    try:
        if os.path.exists(target_dir):
            repo = git.Repo(target_dir)
            print(f"Repository already exists at '{target_dir}'.")
            if repo.bare:
                print("Warning: The local repository is bare.")
            return repo

        print(f"Cloning {remote_url} into '{target_dir}'...")
        return git.Repo.clone_from(remote_url, to_path=target_dir, depth=1)

    except (git.exc.GitCommandError, git.exc.InvalidGitRepositoryError) as e:
        print(f"Git error: {e}")
        return None


def main():
    target_dir = "nixpkgs"
    clone_repo("git@github.com:lukas-sgx/nixpkgs.git", target_dir)

    if not os.path.exists(target_dir):
        print("Failed to clone or locate repository.")
        return

    os.chdir(target_dir)
    base_path = Path("pkgs/by-name")

    if not base_path.exists():
        print(f"Path '{base_path}' does not exist.")
        return

    for shard in base_path.iterdir():
        if not shard.is_dir():
            continue
        print(f"- {shard.name}")

        for subitem in shard.iterdir():
            if not subitem.is_dir():
                continue
            print(f"  |-- {subitem.name}")

            res = subprocess.run(
                [
                    "nix-shell",
                    "-p",
                    "nix-update",
                    "nix-prefetch-git",
                    "--run",
                    f"nix-update --file . --build --write-commit-message commit-file {subitem.name}",
                ],
                check=False,
            )

            if res.returncode != 0 or not os.path.exists("commit-file"):
                print("nix-update failed or commit-file was not created.")
                continue

            try:
                with open("commit-file", "r") as f:
                    first_line = f.readline().strip()

                if "->" in first_line:
                    version = first_line.split("->")[-1].strip()
                else:
                    version = "update"
            except OSError as e:
                print(f"failed to parse commit-file: {e}")
                continue

            subprocess.run(
                ["git", "checkout", "-b", f"{subitem.name}-{version}"],
                check=False,
            )

            subprocess.run(
                ["git", "add", f"pkgs/{base_path.name}/{shard.name}/{subitem.name}/**"],
                check=False,
            )

            subprocess.run(
                ["git", "commit", "-m", f"{first_line}"],
                check=False,
            )

            subprocess.run(
                [
                    "git",
                    "push",
                    "--set-upstream",
                    "origin",
                    f"{subitem.name}-{version}",
                ],
                check=False,
            )

            subprocess.run(
                [
                    "gh",
                    "pr",
                    "create",
                    "--repo",
                    "NixOS/nixpkgs",
                    "--base",
                    "master",
                    "--head",
                    f"lukas-sgx:{subitem.name}-{version}",
                    "--title",
                    f"{first_line}",
                    "--body-file",
                    ".github/PULL_REQUEST_TEMPLATE.md",
                ],
                check=False,
                env=os.environ.copy(),
            )

            subprocess.run(["rm", "commit-file"], check=False)

            subprocess.run(["git", "checkout", "master"], check=False)
