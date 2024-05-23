import os
import sys

import requests
from tqdm import tqdm
from urllib.parse import urlparse


proxy_definitions = {
    #'http': 'http://127.0.0.1:8118',
    #'https': 'http://127.0.0.1:8118'
}

def downloadFile(inFile, outPath):
    with open(inFile, 'r') as fp:
        for line in tqdm(fp):
            line = line.strip()
            try: 
                r = requests.get(line, allow_redirects=True, proxies= proxy_definitions)
                if r.status_code == 200:
                    try:
                        
                        url = urlparse(line)

                        file_key = url.path[1:]                         # getting path (without first /)

                        file_name = os.path.basename(file_key)          # getting file name
                        dir_name = os.path.dirname(file_key) + "/"      # getting only dir

                        if not os.path.exists(outPath + dir_name):
                            os.makedirs(outPath + dir_name)
                        
                        outFile = open(outPath + dir_name + file_name, 'wb')
                        outFile.write(r.content)
                        outFile.close()

                    except:
                        print()
                        print("[-] Error for file: " + file_name + "Error: " + e)
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
