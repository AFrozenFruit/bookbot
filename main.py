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
            if letter.isalpha():
                if letter in characters:
                    characters[letter] += 1
                else:
                    characters[letter] = 1
        return characters
    

            
test = "books/Frankenstein.txt"
count = count_words(test)
print(f"{count} words found in the document")

count = count_characters(test)

# sort the directory
count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
for k,v in count.items():
    print(f"The {k} was found {v} times")