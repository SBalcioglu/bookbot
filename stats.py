def count_words(text):
    num_words = len(text.split()) 
    return num_words

def appearances(text):
    a = text.lower()
    x = {}
    for letter in a:
        if letter in x:
            x[letter] += 1
        else:
            x[letter] = 1
    return x
            
def sorted_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list