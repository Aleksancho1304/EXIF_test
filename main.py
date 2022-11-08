from exif import Image

with open("photo_2022-06-23_13-01-37.jpg", "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

#for index, image in enumerate(images):
    if palm_1_image.has_exif:
        status = f"contains EXIF (version {palm_1_image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {status}")