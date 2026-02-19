import pyfiglet

text = input("Enter the text to convert to ASCII art: ")
ascii_text = pyfiglet.figlet_format(text, font="ansi_shadow")

print("Copy This:\n")
print(ascii_text)

with open("banner.txt", "w", encoding="utf-8") as file:
    file.write(ascii_text)

print("ASCII art has been saved to banner.txt")