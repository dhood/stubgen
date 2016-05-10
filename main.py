import ast

FILENAME = "./test/__init__.py"


def grabThingsBetweenDelimiters(leftDelim, rightDelim, string):
    string.split()
    if (string[0] is "@"):
        return

    elif (string[0] is ":"):
        # we're doxygen
        return

def main():
    with open(FILENAME) as fd:
        file_contents = fd.read()
        module = ast.parse(file_contents)

        print('loaded file')

        function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

        for f in function_definitions:
            # print('---')
            # print(f.name)
            # print('---')
            # print(ast.get_docstring(f))
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
