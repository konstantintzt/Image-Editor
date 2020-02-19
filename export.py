import basic_functions
from PIL import Image

# Supported image file formats
file_formats = [".png", ".jpg"]

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
                user_format = input("Enter export format: ").lower()
                if user_format in file_formats:
                    if user_format == ".jpg":
                        img = img.convert("RGB")
                        img.save(name + user_format)
                    elif user_format == ".png":
                        img = img.cenvert("RGBA")
                        img.save(name + user_format)
                    break

    elif save_decision == "N":
        exit()
    else:
        print("Answer with Y or N")
        export(img)

def convert_channels(format, img):

