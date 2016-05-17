stubgen
=======

Generate [stub files](https://www.python.org/dev/peps/pep-0484/#stub-files) containing hints for the
[mypy](http://mypy-lang.org/) static type checker from docstrings.

Usage
-----

```bash
pip3 install mypy-lang
python examples/sphinx_parser.py -o examples/sphinx/demo_docstrings.pyi
mypy -m examples/sphinx/demo_docstrings --disallow-untyped-defs --verbose
```
