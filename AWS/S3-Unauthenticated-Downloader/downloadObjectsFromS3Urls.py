import sys
import boto3
import os
from botocore import UNSIGNED
from botocore.config import Config
import botocore
from urllib.parse import urlparse
from tqdm import tqdm

proxy_definitions = {
    'http': 'http://127.0.0.1:8118',
    'https': 'http://127.0.0.1:8118'
}

my_config = Config(
    #proxies=proxy_definitions,
    signature_version=UNSIGNED
)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " <Url file list>" + " <out put directory>")
        exit(1)

    inFile = sys.argv[1]
    outDir = sys.argv[2] + "/"
    
    s3 = boto3.resource('s3', config=my_config)

    f = open(inFile, 'r')

    for line in tqdm(f.readlines()):
        line = line.strip()

        try:
            #print("Downloading: " + line)
            url = urlparse(line)

            bucket_name = url.hostname.split('.')[0]        # getting bucketname
            file_key = url.path[1:]                         # getting path (without first /)

            file_name = os.path.basename(file_key)          # getting file name
            dir_name = os.path.dirname(file_key) + "/"      # getting only dir

            if not os.path.exists(outDir + dir_name):
                os.makedirs(outDir + dir_name)

            s3.Bucket(bucket_name).download_file(file_key, outDir + dir_name + file_name)

        except Exception as e:
            print("[-] Error on " + line + " " + str(e))
