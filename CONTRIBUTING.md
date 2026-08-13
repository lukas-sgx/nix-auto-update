# Contributing

Thanks for considering a contribution to nix-auto-update. This project is focused on automating nixpkgs updates and pull-request workflows, so contributions should stay clear, targeted, and easy to review.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Commit Convention](#commit-convention)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs / Requesting Features](#reporting-bugs--requesting-features)
- [Release Process](#release-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

Be respectful, constructive, and patient. Disagreements about implementation are fine; personal attacks are not.

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git
- A local environment capable of installing the project in editable mode
- Optional: a Nix environment if you want to validate package-update workflows locally

### Setup

```bash
git clone https://github.com/lukas-sgx/nix-auto-update.git
cd nix-auto-update
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Verify your environment works by running the CLI entry point:

```bash
nix-auto-update
```

## Project Structure

| Path | Purpose |
|------|---------|
| `nix_auto_update/` | Main Python package and project logic |
| `nix_auto_update/modules/` | Feature modules and reusable logic |
| `tests/` | Automated tests and regression checks |
| `README.md` | Project overview and usage instructions |
| `release-config.json` | Release metadata and versioning configuration |
| `assets/` | Images, logos, and other static files |

## Development Workflow

1. Fork the repo
2. Create a branch from `main`:
   ```bash
   git checkout -b feature/short-description
   # or
   git checkout -b fix/short-description
   ```
3. Make your changes, with tests where applicable
4. Run the relevant validation commands locally (see [Testing](#testing))
5. Push and open a Pull Request describing the update workflow or bug fix you addressed

## Commit Convention

This project follows **[Conventional Commits](https://www.conventionalcommits.org/)**. Keeping commit messages consistent helps with automation and release management based on `release-config.json`.

```
<type>(<scope>): <short description>

[optional body]
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `chore`.

## Testing

- Add or update tests when changing behavior.
- Run the project’s validation commands before opening a PR.
- If your change affects the CLI, package update logic, or release automation, verify it with the relevant local checks.
- Keep regression tests focused on the actual behavior being changed.

## Submitting Changes

Open a pull request with a clear summary of the issue or feature, the files changed, and the validation you ran locally.

A PR is ready for review when:

- the change is focused and easy to understand
- the relevant tests or checks have been run
- the description explains the goal and effect of the update

Reviewers may ask for changes before merging — that's normal and part of the process.

## Reporting Bugs / Requesting Features

Please use an issue template when available, or open a clear issue with enough context to reproduce or discuss the request.

- **Bug report**: include reproduction steps, expected behavior, actual behavior, and environment details.
- **Feature request**: include goals, scope, and any constraints or dependencies.
- **Nix update workflow request**: describe the package or workflow affected and the expected automation behavior.

## Release Process

*(Maintainers only — included for transparency.)*

1. Ensure all merged commits on `main` follow Conventional Commits
2. Confirm `release-config.json` reflects the intended release metadata
3. Validate the package and CLI still behave as expected
4. Prepare a release commit or release PR when the update is ready to ship
5. If a published release causes regressions, fix the issue quickly and ship a corrective patch instead of forcing a broken release

## Style Guidelines

- Keep changes focused and easy to review.
- Follow the existing style of the repository.
- Prefer clear naming, small commits, and concise documentation.
- Adapt the tooling and conventions to the stack you are using.

---

Questions that aren't a bug or feature request can go in [Discussions](https://github.com/your-name/your-repo/discussions) instead of an issue.