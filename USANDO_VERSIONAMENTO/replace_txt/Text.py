class Text:
    def __init__(self, text: str, selected_char: str, replaced_char: str) -> None:
        self.__txt = text
        self.__selec_char = selected_char
        self.__repl_char = replaced_char

    @property
    def txt(self):
        return self.__txt

    @property
    def sl_char(self):
        return self.__selec_char
    
    @property
    def rp_char(self):
        return self.__repl_char
    
    @sl_char.setter
    def sl_char(self, char):
        self.sl_char = char
    
    @rp_char.setter
    def rp_char(self, char):
        self.rp_char = char

    def get_text(self):
        replaced_upper = self.txt.replace(self.sl_char.upper(), self.rp_char.upper())
        replaced_casefold = replaced_upper.replace(self.sl_char, self.rp_char)
        return replaced_casefold