def main():
    import os
    file_stat = os.stat('journal.txt')
    print(f"File Size: {file_stat.st_size}")
    import datetime
    x = datetime.datetime.now()
    x = str(x.strftime("\n\n%A, %B %d, %G - %I:%M %p\n"))
    the_file(x)

def read_file():
    f = open("journal.txt", "r")
    print(f.read())
    f.close()
    print()


def the_file(x):
    while True:
        try:
            # view last entry
            read_file()

            # Ask for new entry today
            myText = str(input("What should I say today? ").strip())

            # write the new journal entry to file
            f = open("journal.txt", "a")
            f.write(x + myText)
            f.close()

            # read entry just entered
            read_file()
        
        except EOFError:
           break

main()
