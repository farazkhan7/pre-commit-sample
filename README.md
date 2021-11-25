![Ekbana](/static/logo.png)
# Pre-commit Configuration Guide
The main aim of this repository is to act as a guide on how to configure the
pre-commit hooks in your existing projects.

Pre-commit hooks are small “scripts” that are run locally on staged files when
using the git commit command. Basically these scripts run each time right when
you try to commit your code locally. We can set configurations such that code
quality is checked each time we attempt to commit the code and commit is
prevented if the pre-defined standards are not met. This ensures that only
quality code gets staged and is pushed to the repository.


## Instructions to configure the pre-commit hooks

### Navigate to your project's root directory and activate your virtual environment

### Install the required packages
```
pip install pre-commit
pip install pylint
```

### Copy files
Copy the following files from this project to your own project's root directory
- .pre-commit-config.yaml
- .flake8
- pyproject.toml

### Install the pre-commit
Run these commands within the virtual environment:
```
pre-commit install
```

### Stage your files
Note that pre-commit runs only on files that you have already staged;
meaning you have performed the `git add` command on them
So if you have not staged your changes you can do so with the following command
```
git add .
```

Now the pre-commit script will check the project formatting when you attempt to
commit your code. Commit is approved only when the pre-commit script finds your
code well formatted and documented.

Note: You can also run the pre-commit script without attempting to commit for test purposes.
Use the command below to run the pre-commit script manually.
```
pre-commit run --all-files
```
