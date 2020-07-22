import re
import os

def crawl_file(file):
    if type(file) != str:
        file = file.read()

    rp_file = file
    findings = re.findall("gettext\(.(.*?)\W\)", rp_file)
    for found in findings:
        if '$' not in found or '=' not in found:
            rp_file = rp_file.replace(found, found.strip().replace('\r','').replace('\n',''))


    #in case that find more than one returns array with consecutive fidnings
    return rp_file

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
            if filepath.endswith(".php") and "script.py" not in str(filepath) and 'error' not in str(filepath):
                #ensures encoding with polish signs (does not remove tags, spaces etc.)
                with open(filepath, encoding='utf-8', mode='r+') as file:
                    results = crawl_file(file)
                with open(filepath, mode = 'w', encoding='utf-8') as file:
                    file.write(results)


    # with open('logs.txt', mode='a+', encoding='utf-8') as logs_file:
    #     for log in logs:
    #         logs_file.write(log+'\n')
