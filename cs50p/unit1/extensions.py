i = input("File name:")
if "." in i:
    i = i.lower().strip().split(".")[-1]
    if i == 'gif':
        print("image/gif")
    elif i == 'jpeg' or i == 'jpg':
        print("image/jpeg")
    elif i == 'png':
        print("image/png")
    elif i == 'pdf':
        print("application/pdf")
    elif i == 'txt':
        print("text/plain")
    elif i == 'zip':
        print("application/zip")
    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')


