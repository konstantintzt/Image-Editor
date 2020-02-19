import basic_functions
from PIL import Image

# Supported image file formats
file_formats = (".png", ".jpg")

# Export image
def export(img):

    save_decision = input("Would you like to save the file? (Y/N)").upper()

    if save_decision == "Y":
        name = input("Enter file name for export: ")

        if name.lower().endswith(file_formats):
            save_with_format(name, img)
        else:
            save_without_format(name, img)

    elif save_decision == "N":
        exit()
    else:
        print("Answer with Y or N")
        export(img)

# Save if user does not provide a format with the name
def save_without_format(name, img):

    export_format = input("Enter export format: ").lower()

    if export_format == ".jpg":
        img = img.convert("RGB")
    elif export_format == ".png":
        img = img.convert("RGBA")
    img.save(name + export_format)

# Save if user provides a format with the name
def save_with_format(name, img):

    name = name.lower()
    if name.endswith(".jpg"):
        img = img.convert("RGB")
        img.save(name)
    elif name.endswith(".png"):
        img = img.convert("RGBA")
        img.save(name)