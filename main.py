# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open("./story.txt" ,"r") as openfile:
        read_file= openfile.read()
        print(read_file)
        print("This file is available")
    
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
   

    return {"as": 10, "would": 20}
