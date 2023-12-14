class Word:
    def __init__(self, ipt: str) -> None:
        self.__ipt = ipt
    
    @property
    def ipt(self):
        return self.__ipt

    def get_reversed(self) -> str:
        strings_list = self.ipt.split()

        if(len(strings_list) > 1):
            strings_list.reverse()
            return ' '.join(strings_list)
        else:
            # solução mind blowing do prof. Eu poderia usar apenas ela no lugar deste bloco if
            word_reversed = str()
            for char in strings_list[0]:
                word_reversed = char + word_reversed 
            return word_reversed