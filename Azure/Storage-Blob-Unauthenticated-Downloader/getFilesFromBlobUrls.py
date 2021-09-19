import requests
import sys
import os

def downloadFile(inFile, outPath):
    with open(inFile, 'r') as fp:
        for line in fp:
            line = line.strip()
            try: 
                r = requests.get(line, allow_redirects=True)
                if r.status_code == 200:
                    try:
                        fileName = os.path.basename(line)
                        print("Writing: " + fileName, end="\r", flush=True)
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
            except:
                print()
                print("[-] Cannot perform request for: " + line)
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