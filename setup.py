from distutils.core import setup

setup(name='assert_future_imports',
      version='1.0.0',
      description='Assertion to check that files import appropriately from __future__',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
      ],
      keywords='',
      author='Rob Falck',
      author_email='robfalck<at>gmail.com',
      url='http://github.com/robfalck/assert_future_imports',
      license='Apache License, Version 2.0',
      packages=[
          'assert_future_imports',
      ],
      entry_points="""
      [console_scripts]
      assert_future_imports=assert_future_imports.main:main
"""
    )
