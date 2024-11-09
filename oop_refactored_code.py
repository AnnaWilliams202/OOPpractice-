class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, content):
        with open(f" Capitalized {self.file_path}", 'w') as f:
            f.write(content)


class Text:
    def __init__(self, input_text):
         self.input_text = input_text

    def capitalize_words(self):
        sentences = self.input_text.split(". ")
        corrected_sentences = []
        for sentence in sentences:
            corrected_sentences.append(sentence.capitalize())

        corrected_text = ". ".join(corrected_sentences)
        return corrected_text


file = File('snowwhite.txt')
content = file.read()

text_processor = Text(content)
corrected_text = text_processor.capitalize_words()

file_out = File('snowwhite_corrected.txt')
file_out.write(corrected_text)
print("Corrected text has been saved to snowwhite_corrected.txt.")