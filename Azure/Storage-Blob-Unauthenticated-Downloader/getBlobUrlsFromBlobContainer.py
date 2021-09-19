import xml.etree.ElementTree as ET
import requests
import sys
import time


def urlExtractor(fileOut, target, response):

    if response.status_code != 200:
        print ("[+] End")
        exit(1)

    root = ET.fromstring(response.text)
    #root = tree.getroot()

    try:
        blobs = root.find('Blobs')

        for blob in blobs:
            print("[+] Blob Url: " + blob.find('Url').text)
            fileOut.write(blob.find('Url').text + '\n')
            time.sleep(1)
    except:
        pass

    try:
        nextMarker = root.find('NextMarker').text
        print("[+] New Page! " + nextMarker)
        response = requests.get(target + "&marker=" + nextMarker)
        urlExtractor(fileOut,target,response)

    except:
        print("[+] No other NextMarker tags, ending...")



def main():
    if len(sys.argv) != 4:
        print(sys.argv[0] + " <account> <container> <outfile>")
        exit(1)

    target = "https://" + sys.argv[1] + ".blob.core.windows.net/" + sys.argv[2] + "?restype=container&comp=list"
    print(target)
    response = requests.get(target)
    
    if response.status_code != 200:
        print ("[-]" + "Reponse code" + str(response.status_code) + " " + target)
        exit(1)
    

    fileOut = open(sys.argv[3],'a')
    urlExtractor(fileOut,target,response)


if __name__ == "__main__":
    main()