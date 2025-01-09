def main():
    pass

def count_words(book):
    with open(book) as f:
        file_contents = f.read()

        return len(file_contents.split())

def count_characters(book):
    with open(book) as f:
        file_contents = f.read()

        characters = {}


        file_contents = file_contents.lower()
        for letter in file_contents:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
        return characters
    
            

count = count_words("books/Frankenstein.txt")
print(count)

count = count_characters("books/Frankenstein.txt")
print(count)