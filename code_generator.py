class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate_code(self):
        code = ""
        for node in self.ast:
            if node[0] == 'ASSIGNMENT':
                code += self.generate_assignment(node)
        return code

    def generate_assignment(self, node):
        var_name = node[1]
        value = node[2][1]
        return f"{var_name} = {value}\n"

if __name__ == "__main__":
    ast = [('ASSIGNMENT', 'a', ('NUMBER', '5'))]
    generator = CodeGenerator(ast)
    code = generator.generate_code()
    print(code)
