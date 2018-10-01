# Hactar Code Style

Hactar's python code style mostly follows PEP8 with a few small additions and differences.

## 100 character maximum line length

We use a 100 character maximum line length because the standard 80 can make code harder to read instead of easier.

## Use Google style docstrings

[Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) are easier to read for both humans and computers.

*Pro-tip:* Install the [AutoDocstring](https://packagecontrol.io/packages/AutoDocstring) SublimeText package and auto generate half your docstrings with `Cmd+Alt+'`

## Use type hints as much as is useful

MyPy and type hinting are extremely useful in a lot of cases, it can make it much easier to reason with your own code, let alone someone else's. Use them wherever you think it's helpful, but in cases where it simply gets in the way, try to leave appropriate comments instead.

## Service classes

Models in code should be little more than a python representation of your database - as much as possible keep business logic out of your models. For this reason we provide a base service class which can be subclassed for each of your models. It provides a consistent set of methods that can remain consistent even if the ORM is swapped out.

If you ever find yourself writing business logic on a model, try to re-think the problem so that this logic can work on the service instead.

## The little things

* No trailing spaces
* Ensure line continuations are [correctly formatted](https://stackoverflow.com/a/7942617/1381789)


## Class Structure

Some frameworks have a convention of adding metadata to classes using an inner class called `Meta`, as this is often used for describing how the class should be used, place it at the top of the class definition so that other team members can find it easily.

#### Example

    class SomePageMixin(Page):

        class Meta:
            abstract = True
        ...

It's also a good idea to keep methods and properties etc. on a class grouped. The preferred order for organising a class would be...

* Docstring
* Inner classes
* properties
* class methods
* methods
* defined properties (using the @property or @cached_property decorators
* __repr__ / __str__ methods

A fuller example would look something like...


    class SomePageMixin(Page):

        """This mixin adds x abilities to a Page model.
        """

        class Meta:
            abstract = True

        template = 'something.jinja'
        some_field = models.CharField(default='Oh hai', null=True, blank=True)

        @classmethod
        def do_something(cls):
            ...

        def get_absolute_url(self):
            return f'{}settings.BASE_URL}{self.url}'

        @property
        def foo(self):
            return self._foo

        def __str__(self):
            return f'<{self.__class__.__name__}> {self.some_field}'


## Linting with Flake8

We use Flake8 for linting with a few small config options such as allowing a line length of 100 characters and suppression of warnings about module level imports not being at the top of the file. For SublimeLinter 4, the settings file should look like this.


    "linters": {
            "flake8": {
                "python": null,
                "disable": false,
                "args": [
                    "--max-complexity", "10",
                    "--max-line-length", "100",
                    "--ignore", "E402"
                ],
                "excludes": [],
                "ignore": "E402",
                "max-complexity": 10,
                "max-line-length": 100,
                "select": "",
            },
        ....


#### Complexity

The linter settings above include a McCabe Complexity limit of 10. This provides you with a sensible level at which the linter will start suggesting that you need to refactor your code. Functions and methods that contain a lot of `if/else` blocks or a lot of `try/except` blocks will quickly hit this limit and you should probably look at how you could encapsulate these sections better.

#### NOQA

Sometimes you _have_ to write a line of code that Flake8 will show a warning for. For instance, often you'll want to access key parts of a module from the top level of that module, this means importing them from their individual files into the `__init__.py` of your module. Flake8 sees this as an unused import and shows warnings. You can suppress these warnings though with `  # NOQA` (two spaces between the code and the comment).

    from .snippets import SidebarBlock  # NOQA
    from .images import CustomImage  # NOQA

## setup.cfg
All our Python projects should have a setup.cfg file - this is an emerging standard for describing a project's settings across multiple tools. Our `setup.cfg` files should have sections for both `isort` and `pytest`.

## Imports order

Not one that we're strict about, but keeping your imports sorted nicely can make them easier to understand for other team members. Use [isort](http://isort.readthedocs.io/en/latest/) along with the [plugin for your preferred editor](https://github.com/timothycrosley/isort/wiki/isort-Plugins) to make this easier. The isort settings we use in our `setup.cfg` files looks like this...

    [isort]
    line_length=100
    force_to_top=
    skip=
    known_standard_libary=std,std2
    known_third_party=django,money,hues,arrow,django_cron,wagtail*
    known_first_party=modules,helpers,assets,config,middelware
    indent='    '
    multi_line_output=5
    length_sort=True
    import_heading_stdlib=stdlib
    import_heading_firstparty=Project
    import_heading_thirdparty=3rd party
    import_heading_localfolder=Module
    lines_after_imports=2
    default_section=THIRDPARTY

You will probably want to customise the `known_third_party` and `known_first_party` lines on a per-project basis.

## Pytest

We use [Pytest](https://docs.pytest.org/en/latest/) for our tests. It's simply better in every way than Python's built in test classes.

Try to write as many of your tests to be non-dependent on database access as possible. Not only does this make your tests run faster, it can help you refactor your code into more sensible patterns. For instance, if you have a class that performs various transformations on a piece of data before saving it to the database, refactoring this to have separate methods for each transformation and a separate save method will allow you to cleanly write very fast tests for each of the transformation steps and a single slow step for the save method. Over a whole project, these speed savings can add up to a lot.

Pytest's settings can also be added to the `setup.cfg` file. A typical pytest block would look something like this...

    [tool:pytest]
    DJANGO_SETTINGS_MODULE = config.settings.test
    python_files = tests.py test_*.py *_tests.py
    django_find_project = false
    python_paths = .
    addopts = --failed-first
    testpaths = .


#### Coverage

Use coverage as much as possible to identify which parts of your code are untested. Side-note: django-pytest has a bug which affects coverage results, so on Django projects use coverage as a guide, but not authoritative.

## Codacy

We use Codacy as a code-quality checking service. You'll want to limit the parts of your code that Codacy checks against, so the project should have a `.codacy.yaml` file at the root that contains a list of files and folders to ignore. This should look something like this...

    ---
    exclude_paths:
      - docs/**/*
      - redis/**/*
      - data/**/*
      - guide/**/*
      - devops/**/*
      - fabfile/**/*
      - web/project/assets/_dev/js/lib/**/*
      - web/project/assets/_dev/js/lib/*.js
      - web/project/assets/_dev/js/lib/*
      - web/project/assets/_dev/scss/lib/**/*
      - web/project/assets/_dev/scss/lib/*
      - web/project/modules/*/migrations/*.py
      - web/project/modules/*/*/migrations/*.py
      - web/project/assets/js/main.min.js
      - web/project/tests/**/*
      - web/project/tests/*.py
      - web/project/modules/*/tests/*.py
      - web/project/modules/*/*/tests/*.py
      - web/project/htmlcov/**/*
