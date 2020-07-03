import re
import os

def crawl_words(file):
    #current pattern
    pattern = ">(.*?)<"
    if type(file) != str:
        file = file.read()
    all = []

    for substring in re.findall(pattern, file):
        if len(substring) >= 3:
            iter = 0
            for char in substring:
                if char.isalpha() == False:
                    iter += 1
                else:
                    all.append(substring[iter:])
                    break

    # for word in all:
    #     str = "<?php gettext('" + word + "')?>"
    #     # print(str)
    #     # print(word+'\n')

    if len(all) == 1:
        return all[0]
    if len(all) == 0:
        return False
    #in case that find more than one returns array with consecutive fidnings
    return all


test_case = []

#ensures that scrip is run localy (!overwrites files!)
if __name__ == '__main__':

    #gets current directory
    directory =  os.getcwd()
    print("Working directory:",directory)

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

                # with open(filepath, mode = 'w', encoding='utf-8') as file:
                #     #overwriting files
                #     pass
