import pyrogram
from YUI import pbot
from pyrogram import Client , filters


@pbot.on_message(filters.photo("sketch"))
def sketch(client, message):
    a = message.reply("Creating Sketch...")
    # Download the image
    image = message.photo.download("image.jpg")
    
    # Open the image using Pillow
    from PIL import Image, ImageFilter
    im = Image.open(image)
    
    # Apply the BLUR and CONTOUR filters
    im = im.filter(ImageFilter.BLUR).filter(ImageFilter.CONTOUR)
    
    # Save the filtered image
    im.save("sketch.jpg")
    
    # Send the sketch to the user
    client.send_photo(message.chat.id, "sketch.jpg")
    a.delete()
    message.reply("Sketch Successfully Printed.")
