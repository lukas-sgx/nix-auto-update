import os
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

    except (git.exc.GitCommandError) as e:
        print(e)
    except (git.exc.InvalidGitRepositoryError) as e:
        print(e)

def main():
    clone_repo("git@github.com:lukas-sgx/nixpkgs.git", "nixpkgs")
    os.chdir("nixpkgs/pkgs/by-name")
    for name in os.listdir("."):
        print(name)
