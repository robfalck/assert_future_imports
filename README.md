assert_future_imports
=====================

assert_future_imports raises an AssertionError if the file in question does not import
the specified imports from __future.  This gives developers an some additional assurance that
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

## License

Apache v2.0
