class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_char = ''
        self.current_position = -1
        self.advance()

    def advance(self):
        self.current_position += 1
        self.current_char = self.source_code[self.current_position] if self.current_position < len(self.source_code) else None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isalpha():
                self.tokens.append(self.make_identifier())
            elif self.current_char.isdigit():
                self.tokens.append(self.make_number())
            else:
                self.advance()
        return self.tokens

    def make_identifier(self):
        identifier = ''
        while self.current_char is not None and self.current_char.isalnum():
            identifier += self.current_char
            self.advance()
        return ('IDENTIFIER', identifier)

    def make_number(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return ('NUMBER', number)

if __name__ == "__main__":
    source_code = "let a = 5"
    lexer = Lexer(source_code)
    tokens = lexer.generate_tokens()
    print(tokens)
