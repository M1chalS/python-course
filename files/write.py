text = "This is some text\nRobert Kubica\nOMG\n"

# w nadpisuje
with open("text.txt", "w") as file:
    file.write(text)

# a dopisuje
with open("text.txt", "a") as file:
    file.write(text)