ext = input("File name: ").strip().lower()
if ext.endswith(".gif"):
    print("Image/gif")
elif ext.endswith(".txt"):
    print("application/txt")
elif ext.endswith(".jpg") or ext.endswith(".jpeg") or ext.endswith(".png"):
    print("Image/jpeg")
elif ext.endswith(".pdf"):
    print("application/pdf")
elif ext.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")