The downloader is composed of two programs:

getObjectUrlsFromS3.py retrieves from a S3 bucket all objects URLs and store them inside a file.

downloadObjectsFromS3Urls.py downloads objects from a list of objects URLs stored in a file.

filter.sh is a grep regex to remove all media file (like images, movie, video, ..)