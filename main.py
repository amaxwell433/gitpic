from PIL import Image, ImageColor
from tqdm import tqdm


imagename = input()
try :
    img = Image.open("input/" + imagename)
    width, height = img.size
    img2 = Image.new('RGB',(width + 1,height + 1),(255,255,255))
    percent = 0
    print(img.size)
    offset = 5e-02*width
    for w in tqdm(range(width)):
        for h in range(height):

            if(w<offset):
                img2.putpixel((w,h),(img.getpixel((w,h))[0],img.getpixel((w,h))[1],img.getpixel((w+offset,h))[2]))
            if(w>offset):
                img2.putpixel((w,h),(img.getpixel((w-offset,h))[0],img.getpixel((w,h))[1],img.getpixel((w,h))[2]))
            else:
                img2.putpixel((w,h),(img.getpixel((w-offset,h))[0],img.getpixel((w,h))[1],img.getpixel((w+offset,h))[2]))
    img2.save("output/" + imagename,'JPEG')
except:
    print("error: request could not be processed")



# lorem ipsum code to do
