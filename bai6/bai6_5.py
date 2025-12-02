class WordReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
s = WordReverser("hello .py")
print(s.reverse_words())  # Kết quả: .py hello
