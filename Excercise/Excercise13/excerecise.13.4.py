names = input("Enter names separated by commas (no spaces):")

def lennames(names):
    spli= names.split(",")
    total_lenght = len(spli)
    return total_lenght

print(lennames(names))