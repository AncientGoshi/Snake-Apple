# The documentation for Snake-Apple

* [GitHub Link](https://github.com/AncientGoshi/Snake-Apple)

## Setup

* [MacOS Instructions](#MacOS-Instructions)
* [Linux Instructions](#Linux-Instructions)
* [Windows Instructions](#Windows-Instructions)

#### MacOS Instructions

If you have homebrew already you can skip to [Installing Python](#Installing-Python)

Quick Setup Script:
```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Copy and paste that into your prefered terminal
<small>note: my prefered terminal is iTerm2
link: [iTerm2](https://iterm2.com)</small>

Installing Python:
> run `brew update && brew upgrade && brew install python3`
> <small>note: it may require your password because it usually run installers with sudo</small>

If you already have python3 still run `brew update && brew upgrade` it is good to keep your packages up to date

If you have done that then go to [Setting up the venv and installing neccesary packages](#Setting-up-the-venv-and-installing-neccesary-packages)

#### Linux Instructions

I have put homebrew for linux in because it is a lot easier for me and for you like that because there a A LOT of different distributions.

Quick Setup Script:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Copy and paste that into your terminal

Then run `brew update && brew upgrade && brew install python3`

#### Windows Instructions

Install python3.13 using the microsoft store: 

1. Go into the Microsoft Store
2. Search for python3.13
3. Click on install

and also search and install winget and execute:
```powershell
winget install Git.Git
```

### Setting up the venv and installing the neccesary package :)

Clone the repository: `git clone https://github.com/AncientGoshi/Snake-Apple.git`

Then, `cd Snake-Apple` OR on windows `chdir Snake-Apple`

and execute `python3 -m venv ./`
That will create a venv in the Snake-Apple directory

after that, execute `source ./bin/activate`

then, execute `pip install pygame`

You will also need to create a file called high-score.json in the Snake-Apple directory

and then, you should be able to just execute it by running `python3 execute_functions`

## Controls

The controls are a normal ↑ ↓ ← → and you can also use WASD if you prefer