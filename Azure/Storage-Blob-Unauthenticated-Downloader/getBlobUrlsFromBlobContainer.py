import sys
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

#os.environ["HTTP_PROXY"] = "http://127.0.0.1:8118"
#os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8118"


Object_URL = "https://{0}.blob.core.windows.net/{1}/{2}"

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + "<account name>" + "<container name>" + "<outfile.txt>")
        exit(1)

    account_name = sys.argv[1]
    container_name = sys.argv[2]
    out_file  = sys.argv[3]

    service = ContainerClient(account_url="https://" + account_name + ".blob.core.windows.net", container_name= container_name)

    # List the blobs in the container
    blob_list = service.list_blobs()

    url_file = open(out_file, mode='a')

    size = 0

    for blob in blob_list:
        size += blob.size
        url = Object_URL.format(account_name, container_name, str(blob.name)) # Cast to string to avoid None
        print(url)
        url_file.write(url+'\n')

    print("Size: {} MB".format(str(size/1024/1024)))
