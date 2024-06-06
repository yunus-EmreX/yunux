class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def analyze(self):
        for node in self.ast:
            if node[0] == 'ASSIGNMENT':
                self.handle_assignment(node)

    def handle_assignment(self, node):
        var_name = node[1]
        value = node[2]
        if value[0] == 'NUMBER':
            self.symbol_table[var_name] = int(value[1])
        else:
            # Diğer türler için işlem yapılacak
            pass

if __name__ == "__main__":
    ast = [('ASSIGNMENT', 'a', ('NUMBER', '5'))]
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
    print(analyzer.symbol_table)
