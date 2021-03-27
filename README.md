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