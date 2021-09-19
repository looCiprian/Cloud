The downloader is composed of three programs, and does not require Azure SDK for python

- getBlobUrlsFromBlobContainer.py retrieves from a Storage Blob input all objects URLs and store them inside a file.
- getFilesSizeFromBlobUrls.py calculates the total size of all objects listed in a file. 
- getFilesFromBlobUrls.py downloads objects from a list of objects URLs stored in a file.
