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
        repo = git.Repo.clone_from(remote_url, to_path=target_dir, depth=1)
        return repo

    except git.exc.GitCommandError as e:
        print(e)
    except git.exc.InvalidGitRepositoryError as e:
        print(e)


def main():
    clone_repo("git@github.com:lukas-sgx/nixpkgs.git", "nixpkgs")

    base_path = Path("nixpkgs/pkgs/by-name")

    for item in base_path.iterdir():
        if not item.is_dir():
            continue
        print(f"- {item.name}")

        for subitem in item.iterdir():
            if not subitem.is_dir() or subitem.name != "lmms":
                continue
            print(f"  |-- {subitem.name}")

            res = subprocess.run(
                [
                    "nix-shell",
                    "-p",
                    "nix-update",
                    "--run",
                    f"nix-update --file . --write-commit-message commit-file {subitem.name}",
                ],
                check=False,
            )

            if res.returncode != 0:
                continue

            subprocess.run(
                [
                    "git",
                    "checkout",
                    "-b",
                    f"{subitem.name}-$(head -n 1 commit-file | cut -d '>' -f 2)",
                ],
                check=False,
            )

            subprocess.run(
                ["git", "add", f"pkgs/by-name/{item.name}/{subitem.name}/*"],
                check=False,
            )

            subprocess.run(["git", "commit", "-m", "$(cat commit-file)"], check=False)

            subprocess.run(
                [
                    "git",
                    "push",
                    "--set-upstream",
                    "origin",
                    f"{subitem.name}-$(head -n 1 commit-file | cut -d '>' -f 2)",
                ],
                check=False,
            )

            subprocess.run(
                [
                    "gh",
                    "pr",
                    "create",
                    "--base",
                    "NixOS/nixpkgs",
                    "--head",
                    f"{subitem.name}-$(head -n 1 commit-file | cut -d '>' -f 2)",
                    "--title",
                    "$(head -n 1 commit-file)",
                ],
                check=False,
            )

            subprocess.run(["rm", "commit-file"], check=False)

            subprocess.run(["git", "checkout", "master"], check=False)
