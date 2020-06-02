from PIL import Image, ImageColor
from tqdm import tqdm


# img.getpixel((x/y))
# puts out rgb values
# 2 layer for loop get average color
# find value on white to dark green
#

img = Image.open("pic.jpg")
width, height = img.size
img2 = Image.new('RGB',(width + 1,height + 1),(255,255,255))
percent = 0

#img2.putpixel((50,50),(50,50,50,255))
#test = img.getpixel(50, 50)
#print(test)
#r = img.getpixel((50,50))[0]
#print(r)


w = 0
h = 0
for w in tqdm(range(3,width)):
    for h in range(3,height):
        #percent+=1
        #img2.putpixel((int(h/2),w),(w,h,50,255))
        #print(percent/(width*height))


        if(w<20):
            img2.putpixel((h+1,w+1),(img.getpixel((h,w))[0],img.getpixel((h,w))[1],img.getpixel((h,w))[2]))
        if(w<20):
            img2.putpixel((h,w),(img.getpixel((h,w))[0],img.getpixel((h,w))[1],img.getpixel((h,w))[2]))
        else:
            img2.putpixel((h,w),(img.getpixel((h,w))[0],img.getpixel((h,w))[1],img.getpixel((h,w))[2]))



img2.save('glitchpic.jpg','JPEG')



#print(col)
print(width)
print(height)


# lorem ipsum code to do
