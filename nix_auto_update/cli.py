from pathlib import Path

import os

import git
import subprocess


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
    base_path.cwd()

    for item in base_path.iterdir():
        if item.is_dir():
            print(f" - {item.name}")
            for subitem in item.iterdir():
                if subitem.is_dir():
                    print(f"   |-- {subitem.name}")
                    os.chdir(subitem.name)
                    subprocess.run(["nix-shell", "-p", "nix-update"], check=True)
                    subprocess.run(["nix-update"], check=True)
