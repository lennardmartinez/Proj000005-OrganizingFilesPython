# Create new File

with open("numbers.txt", "w") as writer:
    for in range(0,31):
        if num % 2 == 0:
            writer.write(f"{num}\n")

with open("read.txt", "w") as reader:
    with open("copy.txt", w) as copy:
        copy.write(reader.read())