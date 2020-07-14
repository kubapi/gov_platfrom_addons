import re
import os

def crawl_file(file):
    if type(file) != str:
        file = file.read()



    # file = file.replace('<br />', '#?#')
    # file = file.replace('<br>', '#?#')

    #making copy before deleting script tags
    rp_file = file

    #deleting all script tags
    pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'  # mach any char zero or more times
    file = re.sub(pattern, '', file, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    all = []
    flags = 0
    searching = False

    if 'echo' in file:
        #when php is inserting html might cause detection error
        flags += 2

    for e, char in enumerate(file):
        if char == '>':
            start = e
            searching = True
        if char == '<':
            if searching == True:
                end = e
                if '{' not in file[start+1:end] and '&' not in file[start+1:end] and '$' not in file[start+1:end] and '}' not in file[start+1:end] and "'" not in file[start+1:end]:
                    if file[start+1:end].islower() == False:
                        #deleting if does not contain alpabetic
                        if any(c.isalpha() for c in file[start+1:end]):
                            all.append(file[start+1:end])
                    else:
                        #lowercases are in minority but sometimes than can represent useful information
                        flags += 1
                searching = False

    #replacing with working
    for word in set(all):
        rp_file = rp_file.replace('>'+word+'<', f"><?php echo gettext('{word[0:len(word)]}')?><")

    #changing break to \n when inside the gettext
    # rp_file = rp_file.replace('#?#', '\n')

    #in case that find more than one returns array with consecutive fidnings
    return rp_file, len(all), flags

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
            if filepath.endswith(".php") and "script.py" not in str(filepath) and 'error' not in str(filepath):
                #ensures encoding with polish signs (does not remove tags, spaces etc.)
                with open(filepath, encoding='utf-8', mode='r+') as file:
                    results = crawl_file(file)
                with open(filepath, mode = 'w', encoding='utf-8') as file:
                    if results[2] >= 3:
                        logs.append(filepath + ' 🚩')
                    else:
                        logs.append(filepath + ' ✔️')
                    file.write(results[0])


    # with open('logs.txt', mode='a+', encoding='utf-8') as logs_file:
    #     for log in logs:
    #         logs_file.write(log+'\n')
