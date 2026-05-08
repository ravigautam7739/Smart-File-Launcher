import os

# change path to your Desktop
desktop_path = "C:/Users/ravir/OneDrive/Desktop"

while True:
    command = input("Enter file name: ").lower()

    found = False

    for file in os.listdir(desktop_path):
        if command in file.lower():
            os.startfile(os.path.join(desktop_path, file))
            found = True
            break

    if not found:
        print("File not found")

    if command == "exit":
        break