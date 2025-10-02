# Append "welcome to PLP" to readme.md
with open("readme.md", "a", encoding="utf-8", errors="ignore") as file:
    file.write("\nWelcome to Power Learn Project Africa")
# print("File structure module loaded successfully.")# Now read and print the updated file
with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
    print(file.read())