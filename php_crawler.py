import re
import os

def crawl_file(file):
    if type(file) != str:
        file = file.read()

    file = file.replace('<br />', '#?#')
    file = file.replace('<br>', '#?#')

    #deleting all script tags
    pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'  # mach any char zero or more times
    file = re.sub(pattern, '', file, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    all = []
    searching = False
    for e, char in enumerate(file):
        if char == '>':
            start = e
            searching = True
        if char == '<':
            if searching == True:
                end = e
                if '{' not in file[start+1:end] and '&' not in file[start+1:end] and '$' not in file[start+1:end] and '}' not in file[start+1:end] and "'" not in file[start+1:end] and file[start+1:end].islower() == False:
                    #deleting if does not contain alpabetic
                    if any(c.isalpha() for c in file[start+1:end]):
                        all.append(file[start+1:end])
                searching = False

    #replacing with working
    for word in set(all):
        file = file.replace('>'+word+'<', f"><?php gettext('{word[0:len(word)]}')?><")

    #changing break to \n when inside the gettext
    file = file.replace('#?#', '\n')
    #in case that find more than one returns array with consecutive fidnings
    return file, len(all)

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
                with open(filepath, encoding='utf-8', mode='r+') as file:
                    results = crawl_file(file)

                with open(filepath, mode = 'w', encoding='utf-8') as file:
                    if results[1] != False:
                        file.write(results[0])
                        logs.append(filepath)

    #saving changed files paths
    logs_file = open('logs.txt', mode='w+', encoding='utf-8')
    logs_file.write(str(logs))
    logs_file.close()
