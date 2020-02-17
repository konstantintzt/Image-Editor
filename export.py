import basic_functions

# Supported image file formats
file_formats = ["png", "jpg"]

# Export image
def export(img):

    save_decision = input("Would you like to save the file? (Y/N)").upper()

    if save_decision == "Y":
        name = input("Enter file name for export: ")

        for i in file_formats:
            if name.lower().endswith(i):
                img.save(name)
                break
            else:
                user_format = input("Enter export format: ")
                if user_format.lower() in file_formats:
                    img.save(name + "." + user_format.lower())

    elif save_decision == "N":
        exit()
    else:
        print("Answer with Y or N")
        export(img)
