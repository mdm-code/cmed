Dictionary entry data crawler for the Middle English Dictionary
[MED](https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary).


## Installation

An account of how to install and deploy `cmed` on the machine.


## Usage

A detailed description on how to use `cmed`.

Now the plan is to have either (1) multiple commands declared in `pyproject.toml`
pointing to `__main__` files in separate packages (crawler, parser, db-loader, ...)
or (2) have a single command with multiple sub-commands. I like the later one
better, however, the first one might be more Pythonic.

It is important to specify the last MED entry ID number for the crawler to know
where to stop making requests to the server. At this point in time (2022-08-28),
the last MED entry is `54083`.


## Development

This program relies on Python version 3.10 and later.

To get the development environment up and running, first, create Python virtual
environment with this `venv` command:

```sh
python3.10 -m venv .
```

Acitivate (and deactivate) the virtual environment with the following commands:

```sh
. bin/activate
deactivate
```

Install the package in the editable mode alongside all of its development
dependencies and upgrade `pip` with `make`:

```sh
make install
```

Type annotation checking, code formatting and automatic testing can be initiated
with the following `make` command:

```sh
make test
```

Use `pre-commit` to run the CI routine when committing code to VCS by
installing it with `pre-commit install`. You can manualy run the routine with
`pre-commit run`.

Consult [Makefile](Makefile) for further details.


## License

Copyright (c) 2022 Michał Adamczyk.

This project is licensed under the [MIT license](https://opensource.org/licenses/MIT).
See [LICENSE](LICENSE) for more details.
