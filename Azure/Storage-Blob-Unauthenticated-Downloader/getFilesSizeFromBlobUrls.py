import requests
import sys

def getFilesSize(inFile):
    finalSize = 0
    with open(inFile, 'r') as fp:
        for line in fp:
            line = line.strip()
            try: 
                r = requests.head(line)             # https://docs.microsoft.com/en-us/rest/api/storageservices/get-file-properties
                if r.status_code == 200:
                    try:
                        currentFileSize = r.headers['Content-Length']
                        finalSize += int(currentFileSize)
                        print("Bytes: " + str(finalSize), end="\r", flush=True)
                    except:
                        print("[-] Cannot print result of: " + line)
                        pass
                else:
                    print("[-] Status code not OK for: " + line)
            except:
                print("[-] Cannot perform request for: " + line)
                pass

    return finalSize

def main():
    if len(sys.argv) != 3:
        print(sys.argv[0] + " <inFile - containing list of urls> <outfile - will contain total bytes>")
        exit(1)

    finalSize = getFilesSize(sys.argv[1])
    outFile = open(sys.argv[1], 'w')
    outFile.write(str(finalSize) + '\n')
    outFile.close()
    
    print("[+] Done")

if __name__ == "__main__":
    main()