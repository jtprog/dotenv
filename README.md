Python Dot Env Handler
======================

[![Build Status](https://travis-ci.org/jtprog/ndenv.svg?branch=master)](https://travis-ci.org/jtprog/ndenv)


Based on [ https://github.com/pedroburon/dotenv ](https://github.com/pedroburon/dotenv)

Shell Command and Library to write and read `.env` like files.

`.env` files are commonly used with `Procfile`-based apps.

Usage
-----

### Shell

Inspect file

```shell
$ ndenv
FOO: bar
Bar: baz
```

Get value for key

```shell
$ ndenv FOO
FOO: bar
```

Set value for key

```shell
$ ndenv FOO baz
FOO: baz
```

### As a library

```python
>>> from ndenv import NDenv
>>> ndenv = DotEnv('/path/to/.env')
>>> print ndenv
{"FOO": "bar", "Bar": "baz"}
>>> ndenv['FOO']
"bar"
>>> ndenv['FOO'] = "baz"
>>> ndenv['FOO']
"baz"
>>> del ndenv['FOO']
>>> print ndenv
{"Bar": "baz"}
```

> Every action is persisted.


### Use with Django

```python
# add this to manage.py above `execute_from_command_line(sys.argv)`

from ndenv import NDenv
ndenv = NDenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(ndenv)

```
