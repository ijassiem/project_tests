import re

def get_file(filename):
    f = open(filename)
    x = f.read()
    f.seek(0)
    f.close()
    return x

def find_num(my_file, word):
    result = re.findall(word, my_file)
    print(result)
    return len(result)

######################################################################

try:
    data = get_file("text.txt") # open file and returns data
    print(data)
except:
    print("Error opening file")

try:
    num = find_num(data, "people") # data is searched and returns no of matches
    print("Matches found: ", num)
except:
    print("Error has occurred")

    
    








