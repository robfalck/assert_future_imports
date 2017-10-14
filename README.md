assert_future_imports
=====================

assert_future_imports raises an AssertionError if the file in question does not import
the specified imports from __future__.  This gives developers an some additional assurance that
their code will be backwards compatible.

## Installation

```
pip install git+https://github.com/robfalck/assert_future_imports.git
```

## Usage

```
from assert_future_imports import assert_future_imports

assert_future_imports('mypath', imports=['print_function', 'division'], ignores=['__init__.py'])
```

## From the command line:

```
$ assert_future_imports --help
usage: assert_future_imports [-h] [--imports IMPORTS] [--excludes EXCLUDES]
                             path

Example with long option names

positional arguments:
  path                 the path to be searched for __future__ imports

optional arguments:
  -h, --help           show this help message and exit
  --imports IMPORTS    Space-delimited sequence of things that must be
                       imported from __future__. Defaults to'print_function
                       division absolute_import'
  --excludes EXCLUDES  Filenames to be ommitted from assertion. '__init__.py'
                       might be a common exclude, for instance.
```

Running assert_future_imports from within this repo, for instance, will give

```
$ assert_future_imports .
Traceback (most recent call last):
  File "/Users/rfalck/anaconda/envs/blue2/bin/assert_future_imports", line 11, in <module>
    load_entry_point('assert-future-imports==1.0.0', 'console_scripts', 'assert_future_imports')()
  File "/Users/rfalck/Codes/assert_future_imports.git/assert_future_imports/main.py", line 142, in main
    assert_future_imports(args.path, imports=imports, excludes=excludes)
  File "/Users/rfalck/Codes/assert_future_imports.git/assert_future_imports/main.py", line 118, in assert_future_imports
    raise AssertionError(err_msg)
AssertionError: Files are missing imports from __future__
    ./setup.py: division, print_function, absolute_import
```

## License

Apache v2.0
