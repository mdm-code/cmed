Dictionary entry data crawler for the Middle English Dictionary
([MED](https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary))
lets you crawl and parse data from MED on the command line.


## Installation

For now, `cmed` is not a distributed package, so it doesn't use
[pypi.org](https://pypi.org/) to allow you to pull it easily with `pip`.

The way to use it is, first, to clone this repository with `git` and then
install the package in the editable mode like so:

```sh
python3.10 -m venv .
. bin/activate
make install
```

Use Python 3.10 to (1) create and activate a virtual environment in the package
root directory. Then (2) use `make` to install the package in the editable
mode.


## Usage

Once installed in the editable mode, the package `cmed` exposes the following
shell commands:

* med-crawl
* med-parse

The first one takes care of crawling html data from the MED website. It has
a useful help built in. Having tested the interaction with MED server, having
five concurrent requests is fine; you can try to push it, but I do not vouch
for it to be stable.

The last MED entry to date (2022-09-28) is 54083. You can use `--last-id` to
change it, but why would you? Keep it default unless you know it crawl fewer
web entry pages or you can set to a million and crawl 404 for ages.

The second one is responsible for parsing the crawled data. It also has a 
built in help, so you can easily reach out to it, but there isn't much to
it aside from input, output and verbose flags.


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

Consult [Makefile](Makefile) for further details.


## License

Copyright (c) 2022 Michał Adamczyk.

This project is licensed under the [MIT license](https://opensource.org/licenses/MIT).
See [LICENSE](LICENSE) for more details.
