filetype = input("Ask file type and you will be answered 😒 : ")
filetype = filetype.strip().lower()

if filetype.endswith(".gif"):
    print("This is a GIF")
elif filetype.endswith(".jpg") or filetype.endswith("jpeg"):
    print("This is a jpg/jpeg Image")
elif filetype.endswith(".png"):
    print("This is a PNG image")
elif filetype.endswith(".pdf"):
    print("This is a PDF file")
elif filetype.endswith(".txt"):
    print("This is a text file")
elif filetype.endswith(".zip" or ".rar"):
    print("This is a compressed archive")
    print("Reminder: Your 40 day winrar trial expired in 2010 😁")
else:
    print("hmm, that's application/octet-stream")


    #ვიცი, რომ ზუსტად ისე არ შევასრულე, როგორც check50-ზე, მაგრამ ესე უფრო სახალისო იყო 😬