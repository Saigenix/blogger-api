from PIL import Image, ImageDraw, ImageFont
import textwrap
import random

emojis = ["📊","🔧","🎛️","🤖","📺",'💡','👨‍🔧','✨','🎆','🎯','🥇','🗝️','💸','⏳','🌍','⚡','🤍','💫','✅','✳️']
def generate_image(title):

    myFont = ImageFont.truetype('raw/f1.ttf', 70)
    width, height = (1280, 720)
    im = Image.open("raw/bg.jpg")
    d1 = ImageDraw.Draw(im)
    lines = textwrap.wrap(title, width=35)
    y = 0;
    for line in lines:
        print()
        (font_width, font_height), (offset_x, offset_y) = myFont.font.getsize(line)
        # font_width, font_height = myFont.getmetrics(line)
        new_width = (width - font_width) / 2
        new_height = (height - font_height) / 2
        d1.multiline_text((new_width+3, new_height+3+y), line, font=myFont,align='center',fill=(0, 0, 0,128))
        d1.multiline_text((new_width, new_height+y), line, font=myFont,fill=(256, 256, 256))
        y = y + 65
    im.show()
    im.save(f"raw/new.png")
    # im.save(f"raw/{title}.png")


# generate_image("why you should learn Typescript?")