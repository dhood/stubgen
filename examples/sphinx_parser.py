import os
import sys

from sphinx.application import Sphinx

from stubgen import parse_docstring

thisdir = os.path.dirname(sys.argv[0])
srcdir = os.path.join(thisdir, 'sphinx', 'sphinx-settings')
confdir = os.path.join(thisdir, 'sphinx', 'sphinx-settings')
outdir = os.path.join(srcdir, 'doc')
doctreedir = os.path.join(outdir, '.doctrees')
buildername = 'dummy'

def process_docstring(app, what, name, obj, options, lines):
    if lines:
        print name
        print lines

if __name__ == '__main__':
    app = Sphinx(srcdir, confdir, outdir, doctreedir, buildername, freshenv=True)
    app.connect('autodoc-process-docstring', process_docstring)
    app.build()

