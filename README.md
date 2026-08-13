<div align="center">
  <a href="https://github.com/lukas-sgx/nix-auto-update/">
    <img src="https://github.com/lukas-sgx/nix-auto-update/blob/main/assets/template-logo.png?raw=true" alt="Logo" height="180" style="border-radius: 10px">
  </a>

  <h3 align="center">nix-auto-update</h3>

  [![License](https://img.shields.io/github/license/lukas-sgx/nix-auto-update?style=for-the-badge)](./LICENSE)
  [![Build Status](https://img.shields.io/github/actions/workflow/status/lukas-sgx/nix-auto-update/ci.yml?style=for-the-badge)](https://github.com/lukas-sgx/nix-auto-update/actions)

  <p align="center">
    Auto update nixpkgs & automate PR to it.
    <br />
    <a href="https://github.com/lukas-sgx/nix-auto-update"><strong>Explore the repository »</strong></a>
    <br />
    <br />
    <a href="https://github.com/lukas-sgx/nix-auto-update">View Demo</a>
    &middot;
    <a href="https://github.com/lukas-sgx/nix-auto-update/issues/new?template=bug-report.yml">Report Bug</a>
    &middot;
    <a href="https://github.com/lukas-sgx/nix-auto-update/issues/new?template=feature-request.yml">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

nix-auto-update is a small automation tool designed to help maintainers keep Nix package definitions in sync with upstream changes and streamline the creation of update pull requests. The project focuses on a repeatable workflow for checking nixpkgs updates, preparing the relevant changes, and facilitating the PR process.

### Built With

[![Python][Python-shield]][Python-url]
[![Nix][Nix-shield]][Nix-url]

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.10 or newer
- Git
- A working Nix environment if you plan to test package updates locally

### Installation

#### Development mode (clone the repo, with local changes)
1. Clone the repository
```sh
git clone https://github.com/lukas-sgx/nix-auto-update.git
cd nix-auto-update
```
2. Create a virtual environment and install the project
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

#### Release mode
```sh
pip install nix-auto-update
```

## Usage

After installing the project, run the CLI entry point:

```sh
nix-auto-update
```

This command is the entry point for the automation workflow and can be extended to automate nixpkgs checks, update generation, and PR creation.

## Roadmap

- [ ] Detect upstream nixpkgs updates automatically
- [ ] Generate the relevant package update diff
- [ ] Prepare a clean commit message and patch set
- [ ] Automate pull request creation for upstream changes
- [ ] Add tests and CI validation

See the [open issues](https://github.com/lukas-sgx/nix-auto-update/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are welcome and appreciated. Please review the contribution guide and follow the repository conventions when making changes.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for setup instructions, commit conventions, and the PR process.

### Top contributors:

<a href="https://github.com/lukas-sgx/nix-auto-update/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=lukas-sgx/nix-auto-update" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

## Contact

`@lukas-sgx` - lukas.soigneux@epitech.eu

## Acknowledgments

* [Python](https://www.python.org/) - Main language used for the project automation
* [Nix](https://nixos.org/) - The package ecosystem this project targets

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Nix-shield]: https://img.shields.io/badge/Nix-5277C3?style=for-the-badge&logo=nixos&logoColor=white
[Nix-url]: https://nixos.org/

