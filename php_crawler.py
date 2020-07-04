import re
import os

def crawl_words(file):
    #current pattern
    pattern = ">(.*?)<"

    #if file is string than don't read inside
    if type(file) != str:
        file = file.read()

    #checks for <br /> and replaces
    file = file.replace('<br />', '#?&')

    all_found = []
    for substring in re.findall(pattern, file):
        if len(substring) >= 2:
            iter = 0
            for char in substring:
                #checks to ensure starting with alphabetic
                if char.isalpha() == False or char == ' ' or char in ':,.][\;#$%^!@-–1234567890()]'.split():
                    iter += 1
                else:
                    all_found.append(substring[iter:])
                    #dosen't need to loop more after finds alpha type sign
                    break

    #check if error with inside tag
    all = []
    for word in all_found:
        if '>' in word:
            word = word[word.find('>')+1:]
        if '<' in word:
            word = word[:word.find('<')]
        #adding for gettext purpose
        all.append('>'+word+'<')

    #replacing with working
    for word in set(all):
        file = file.replace(word, f"><?php gettext('{word[1:len(word)-1]}')?><")

    #changing break to \n when inside the gettext
    file = file.replace('#?&', '\n')

    if len(all) == 1:
        return all[0]
    if len(all) == 0:
        return False

    #in case that find more than one returns array with consecutive fidnings
    return file

#ensures that scrip is run localy (!overwrites files!)
if __name__ == '__main__':
    logs = []


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
                with open(filepath, encoding='utf-8', mode='r+') as file:
                    results = crawl_words(file)

                with open(filepath, mode = 'w', encoding='utf-8') as file:
                    if results != False:
                        file.write(results)
                        logs.append(filepath)

    #saving changed files paths
    logs_file = open('logs.txt', mode='w+', encoding='utf-8')
    logs_file.write(str(logs))
    logs_file.close()
