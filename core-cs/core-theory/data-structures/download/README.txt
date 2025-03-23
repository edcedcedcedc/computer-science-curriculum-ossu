how to use it:
    python downloader.py link path/to/save

updates:
23/03/2025 - recursively lookup n-nested folders and download files
            NOTES:
                This update is very specific and is searching folder under "folder/" and files undr "files",
                For this to be more generalized, you need a more advanced match for "folder/".
            FOR EXAMPLE:
                Now it will download a folder which has inside n-nested folders as "folder/" but not as "folder"