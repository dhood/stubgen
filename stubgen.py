import ast
import re

FILENAME = "./test/__init__.py"


def parse_docstring(leftDelim, rightDelim, docstringLines):
    docfields = []
    
    fieldRegex = '\s*' + leftDelim + '(?P<fieldTag>(\w|_|\s)+)' + rightDelim + '\s+(?P<fieldText>.+)'
    pattern = re.compile(fieldRegex)

    for line in docstringLines:  # TODO: make multiline regex
        line = line.encode()
        match = pattern.match(line)
        if match:
            fieldTag = match.group('fieldTag')
            fieldText = match.group('fieldText')
            fieldTags = fieldTag.split()
            #import pdb; pdb.set_trace()
            if len(fieldTags) == 1:
                field = {
                    'fieldType': fieldTags[0],
                    'fieldText': fieldText}
            elif len(fieldTags) == 2:
                field = {
                    'fieldType': fieldTags[0],
                    'fieldArg': fieldTags[1],
                    'fieldText': fieldText}
            elif len(fieldTags) == 3:
                field = {
                    'fieldType': fieldTags[0],
                    'fieldVal': fieldTags[1],
                    'fieldArg': fieldTags[2],
                    'fieldText': fieldTags[3]}
            if field:
                docfields.append(field)
                print field
    return docfields

def main():
    with open(FILENAME) as fd:
        file_contents = fd.read()
        module = ast.parse(file_contents)

        print('loaded file')

        function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

        for f in function_definitions:
            docstring = ast.get_docstring(f)
            params = {}
            returntype = ""
            for line in docstring.splitlines():
                # if ":param" in line:
                    # param = line.split()[2]
                    # params[param] =  "Any"
                if ":type" in line:

                    # this line is a type
                    tokens = line.split()
                    param = tokens[1][:-1]
                    ty = tokens[2]
                    # print ("param is " + param + " with type " + ty)
                    params[param] = ty
            string = "def {0}({1})".format(
                   f.name, ", ".join(
                       ["%s: %s" % (param, params[param]) for param in params]))
            '''
            string = "def " + f.name + "("
            for param in params:
                string += "" + param + ": " + params[param] + ", "
            string += "):"
            '''
            print string


if __name__ == '__main__': 
    main()
