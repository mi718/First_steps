contents = ["All carrots are to be sliced logitudinally.",
            "The carrots were reportedly sliced",
            "The slicing process was well presented"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", "w")
    file.write(content)