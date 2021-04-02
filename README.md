<div align="center">

<img src="https://code.visualstudio.com/assets/docs/python/tutorial/intellisense01.png" width="400px">


**Visual Studio Code for python projects**

---

<p align="center">
  <a href="https://code.visualstudio.com/">Visual Studio Code</a> •
  <a href="#setting-up-vscode">Setting up vscode</a> •
  <a href="#config-filse">Config files</a> •
  <a href="#autoformat">Autoformat</a> •
  <a href="#linting</a>Linting</a> •
  <a href="#debug</a>Debug</a> •
  <a href="#tests</a>Tests</a> •
  <a href="#type-hints">Type hints</a>
</p>

![Python Badge](https://img.shields.io/badge/-python-3776AB?style=flat-square&logo=python&logoColor=white)
![Visual Studio Code Badge](https://img.shields.io/badge/-vscode-007ACC?style=flat-square&logo=vscode&logoColor=white)
[![CI](https://github.com/ivanCanaveral/vscode-python-project-setup/actions/workflows/main.yml/badge.svg)](https://github.com/ivanCanaveral/vscode-python-project-setup/actions/workflows/main.yml)

</div>


## Setting up vscode

Create a virtual environment with pipenv.

Open vscode.

Select a python interpreter. VSCode should detect the virtual environment automatically. If not, `ctrl + shift + p` and then `select environment`.

Now, if you create a python file, you can see how intelliSense helps you with some autocompletion.

**Tip:** If you select a piece of code and press `shift + enter`, a RELP will be opened, and your piece of code executed.

**Tip:** Right click + execute file in a terminal, will execute the file in a terminal, using the proper environment.

### Config files

Now you should be able to find a folder called `.vscode`, where the editor saves its configuration files. For the moment, just a `settings.json` file, with the environment path should be there. We can add some options, but also is okay if we edit those settings through the `File > Preferences > Settings [Ctrl + ,]` menu.

### Autoformat

Although there is a little overlap between formatting and linting, the two capabilities are complementary.

```
pipenv install autopep8
```

Now, with `ctrl + shift + i` your code will be formatted.

### Linting

Linting is thus distinct from Formatting because linting analyzes how the code runs and detects errors whereas formatting only restructures how code appears.

```
pipenv install pylint
```

`ctrl + shipt + p` -> select linter -> pylint
`ctrl + shipt + p` -> enable linter -> pylint


### Debug

```
ctrl + shif + d
```

### Tests

`ctrl + shif + p` > Configure test. This will update your config settings. Python: Discovery tests, looks for tests. Since this moment, you can run tests from the status bar.

This will activate the Test Explorer.

### Type hints

Let's use pyright for the moment.
