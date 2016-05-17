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

filename = 'output.pyi'

def process_docstring(app, what, name, obj, options, lines):
    if lines:
        docfields = parse_docstring(':', ':', lines)
        print('----')
        params = {}
        returnType = None
        for field in docfields:
            fieldType = field['fieldType']
            if fieldType == 'param':
                fieldArg = field['fieldArg']
                if 'fieldVal' in field:
                    params[fieldArg] = field['fieldVal']
                else:
                    params[fieldArg] = 'Any'
        for field in docfields:
            fieldType = field['fieldType']
            if fieldType == 'type':
                fieldArg = field['fieldArg']
                if fieldArg in params:
                    params[fieldArg] = field['fieldText']
        shortName = name.split('.')[-1]
        string = 'def {0}({1}) -> {2}: ...\n\n'.format(
            shortName,
            ', '.join(
                ['%s: %s' % (param, params[param]) for param in params]),
            returnType if returnType else 'Any')
        with open(filename, 'a') as f:
            f.write(string)

if __name__ == '__main__':
    with open(filename, 'w') as f:
        f.write('from typing import Any\n\n')

    app = Sphinx(srcdir, confdir, outdir, doctreedir, buildername, freshenv=True)
    app.connect('autodoc-process-docstring', process_docstring)
    app.build()
