The downloader is composed of three programs

- getBlobUrlsFromBlobContainer.py retrieves from a Storage Blob input all objects URLs and store them inside a file (requires Azure SDK for python)
- getFilesSizeFromBlobUrls.py calculates the total size of all objects listed in a file (not require Azure SDK for python)
- downloadFilesFromBlobUrls.py.py downloads files from a list of objects URLs stored in a file (not require Azure SDK for python)

filter.sh is a grep regex to remove all media file (like images, movie, video, ..)