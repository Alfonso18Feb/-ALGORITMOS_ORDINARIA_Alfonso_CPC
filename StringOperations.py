from functools import partial

class StringOperations:
    """
    Clase para realizar operaciones simples en cadenas de texto.
    """
    def __init__(self,text,old, new):
        self.new=new
        self.old=old
        self.text=text
    def capitalize_text(self, text):
        for i in self.text:
            if text[0]:
                return text[0].upper()
            elif i==' ':
                text[i+1].upper()
            else:
                return i

    def replace_substring(self, text, old, new):
        return text.replace(old, new)

operations=StringOperations
apitalize_first_word= partial(operations.capitalize_text(),text.upper())
# Crear una instancia de StringOperations

# Crear versiones especializadas usando functools.partial

# Ejemplos de uso
def main():
    text = "hola mundo"
    capitalize_first_word= partial(operations.capitalize_text().replace('M','m'))
    # Usando capitalize_first_word
    print(capitalize_first_word(text))  # Output: "Hola mundo"
    replace_spaces_with_underscore=(operations.replace_substring([replace(' ','_'): for i in text ]))
    # Usando replace_spaces_with_underscore
    print(replace_spaces_with_underscore(text))  # Output: "hola_mundo"

if __name__ == "__main__":
    main()