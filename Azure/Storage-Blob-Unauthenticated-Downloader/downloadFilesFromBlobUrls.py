import os
import sys

import time
import requests
from tqdm import tqdm

proxy_definitions = {
    'http': 'http://127.0.0.1:8118',
    'https': 'http://127.0.0.1:8118'
}

def downloadFile(inFile, outPath):
    with open(inFile, 'r') as fp:
        for line in tqdm(fp):
            line = line.strip()
            try: 
                r = requests.get(line, allow_redirects=True, proxies= proxy_definitions)
                if r.status_code == 200:
                    try:
                        fileName = os.path.basename(line)
                        if os.path.exists(outPath + fileName): # if file already exist store adding timestamp to it
                            fileNameSplitted = os.path.splitext(fileName)
                            if len(fileNameSplitted) == 2: # if file have an extension
                                outFile = open(outPath + fileNameSplitted[0] + "_" +str(time.time())[0:5] + fileNameSplitted[1], 'wb') # file-123.txt
                                outFile.write(r.content)
                                outFile.close()
                                continue # go for the next item
                        
                        outFile = open(outPath + fileName, 'wb')
                        outFile.write(r.content)
                        outFile.close()

                    except:
                        print()
                        print("[-] Error for file: " + fileName + "Error: " + e)
                        pass
                else:
                    print()
                    print("[-] Status code: " + str(r.status_code) + " for url: " + line)
            except Exception as e:
                print()
                print("[-] Cannot perform request for: " + line + " " + str(e))
                pass

def main():
    if len(sys.argv) != 3:
        print(sys.argv[0] + " <inFile - containing list of urls> <outfile directory - where store files>")
        exit(1)

    downloadFile(sys.argv[1], sys.argv[2] + '/')
    
    print()
    print("[+] Done")

if __name__ == "__main__":
    main()