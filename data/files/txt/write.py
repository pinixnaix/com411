def search(path):
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"

    with open(path) as file:
        for line in file:

            if line.startswith("Section"):
                sections += line
            else:
                books += line

    print("Done")
    return f"{sections}\n\n{books}"


def save(path, string):
    print("Saving..", end="")
    with open(path, "w") as file:
        file.write(string)
    print("Done!")


def run():
    data = search("books.txt")
    save("sections_books.txt", data)


if __name__ == "__main__":
    run()
