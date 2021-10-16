import sys

import boto3
import requests
from botocore import UNSIGNED
from botocore.config import Config
from tqdm import tqdm

proxy_definitions = {
    #'http': 'http://127.0.0.1:8118',
    #'https': 'https://127.0.0.1:8118'
}

my_config = Config(
    proxies=proxy_definitions,
    signature_version=UNSIGNED
)

Object_URL = "https://{0}.s3.amazonaws.com/{1}"

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + "<bucket name>" "<outfile.txt>")

    bucket_name = sys.argv[1]
    out_file  = sys.argv[2]

    s3 = boto3.resource('s3', config=my_config)
    bucket = s3.Bucket(bucket_name)
    object_summary_iterator = bucket.objects.all()
    
    print("Connected to the bucket...")
    print("Get number of objects inside {}...".format(bucket_name))

    object_counts = 0
    for object_summary in object_summary_iterator:
        object_counts += 1
    
    print("{} objects".format(str(object_counts)))

    input("Press enter to continue")

    url_file = open(out_file, mode='a')

    size = 0

    for object_summary in object_summary_iterator:
        size += object_summary.size
        url = Object_URL.format(bucket_name, str(object_summary.key)) # Cast to string to avoid None
        print(url)
        url_file.write(url+'\n')

    print("Size: {} MB".format(str(size/1024/1024)))


