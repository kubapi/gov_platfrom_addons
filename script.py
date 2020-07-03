import re
import os
from bs4 import BeautifulSoup

def get_all_words_and_replace(file):
    pattern = ">(.*?)<"
    file = file.read()
    substrings = re.findall(pattern, file)
    all = []
    for substring in substrings:
        if len(substring) >= 3:
            iter = 0
            for char in substring:
                if char.isalpha() == False:
                    iter += 1
                else:
                    all.append(substring[iter:])
                    break

    for word in all:
        str = "<?php gettext('" + word + "')?>"
        print(str)
        print(word+'\n')
        file = file.replace(word, str)

    return file

def get_all_words_and_replace2(file):
    soup = BeautifulSoup(file.read(), 'lxml')
    print(soup.text)


#ensures that scrip is run localy (!overwrites files!)
if __name__ == '__main__':
    #gets current directory
    directory =  os.getcwd()
    #print(directory)

    #iterating over all files under script.py (also digs over sub-directories)
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            #creates relative filepath
            filepath = subdir + os.sep + filename

            #restrics only .php files and skips itself
            if filepath.endswith(".php") and "script.py" not in str(filepath):
                #ensures encoding with polish signs (does not remove tags, spaces etc.)
                with open(filepath, encoding='utf-8') as file:
                    #loading of file to script
                    pass

                with open(filepath, mode = 'w', encoding='utf-8') as file:
                    #overwriting files
                    pass
