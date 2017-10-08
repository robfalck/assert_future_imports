from __future__ import print_function
from __future__ import division, absolute_import

import ast
import fnmatch
import os
import os.path

_valid_future_imports = set(('print_function', 'division', 'absolute_import', 'unicode_literals',
                         'with_statement', 'generators', 'nested_scopes'))


def get_future_imports(filename):
    """
    Returns the names imported from __future__ in the given file.

    Parameters
    ----------
    filename : str
        A Python file to check for __future__ imports.

    Returns
    -------
    tuple
        The names imported from __future__ in the given file.  If nothing
        is imported from __future__ the returned tuple is empty.

    Raises
    ------
    IOError
        If the given filename is unable to be parsed as Python.


    """
    with open(filename, 'r') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except:
        raise IOError('Unable to parse {0} as a Python file'.format(filename))

    future_imports = []

    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == '__future__':
            for alias in node.names:
                future_imports.append(alias.name)

    return tuple(future_imports)


def assert_future_imports(s, imports=None, excludes=None):
    """
    Raises an AssertionError if the provided imports from future are not found in the given file.

    Parameters
    ----------
    s : str
        A Python file or directory to recursively check for __future__ imports.

    Returns
    -------
    tuple
        The names imported from __future__ in the given file.  If nothing
        is imported from __future__ the returned tuple is empty.

    Raises
    ------
    IOError
        If the given filename is unable to be parsed as Python.
    ValueError
        If the one or more strings in imports is not valid import from __future__.
    AssertionError
        If the specified file does not import all of the given imports from __future__.
    """
    if imports is None:
        test_set = {'print_function', 'division', 'absolute_import', 'unicode_literals'}
    else:
        test_set = set(imports)
        if not test_set.issubset(_valid_future_imports):
            raise ValueError('Invalid imports from __future__: '
                             '{0}'.format(' ,'.join([i for i in test_set - _valid_future_imports])))

    if os.path.isfile(s):
        files = [s]
    elif os.path.isdir(s):
        files = []
        for root, dirnames, filenames in os.walk(s):
            for filename in fnmatch.filter(filenames, '*.py'):
                if filename not in excludes:
                    files.append(os.path.join(root, filename))

    failures = {}

    for filename in files:
        imported = set(get_future_imports(filename))

        missing_imports = test_set - imported

        if missing_imports:
            failures[filename] = missing_imports

    if failures:
        err_msg = 'Files are missing imports from __future__\n'
        for f in failures:
            err_msg += '    ' + f + ': ' + ', '.join([i for i in failures[f]]) + '\n'

        raise AssertionError(err_msg)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Example with long option names')

    parser.add_argument('paths', action='store')
    parser.add_argument('--imports', action='store',
                        default='print_function division absolute_import')
    parser.add_argument('--ignores', action='store', default='__init__.py')

    args = parser.parse_args()

    print(args)

if __name__ == '__main__':
    assert_future_imports('..',
                          imports=('print_function', 'division', 'absolute_import'),
                          excludes=['__init__.py'])
