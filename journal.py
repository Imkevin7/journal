def main():
    
    import datetime
    x = datetime.datetime.now()
    x = x.strftime("\n\n%B, %A-%d, %G - %I:%M %p\n")
    x = str(x)
    the_file(x)

def the_file(x):
    # view last entry
    f = open("journal.txt", "r")
    print(f.read())

    # Ask for new entry today
    myText = str(input("What should I say today? "))

    # write the new journal entry to file
    f = open("journal.txt", "a")
    f.write(x + myText)
    f.close()

    # read entry just entered
    f = open("journal.txt", "r")
    print(f.read())

main()
