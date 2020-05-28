from PIL import Image, ImageColor


# img.getpixel((x/y))
# puts out rgb values
# 2 layer for loop get average color
# find value on white to dark green
#

img = Image.open("pic.jpg")
width, height = img.size
img2 = Image.new('RGB',(width,height),(255,255,255))
percent = 0

#img2.putpixel((50,50),(50,50,50,255))
#test = img.getpixel(50, 50)
#print(test)




for w in range(width):
    for h in range(height):
        percent+=1
        img2.putpixel((h,w),(50,50,50,255))
        print(percent/(width*height))

    print("---------------------------------------------------------------")
"""
        if(w<20):
            img2.putpixel((h,w),50,50,50)
        #    img2.putpixel((h,w), 50,50,50)
        #    img2.putpixel((h,w),        )

        if(w<20):

            img2.Draw.point((h,w-20),(img.getpixel((h,w)),img.getpixel((h,w)),img.getpixel((h,w))))
        else:

            img2.Draw.point((h,w-20),(img.getpixel((h,w)),img.getpixel((h,w)),img.getpixel((h,w+20))))

        percent+=1
"""



img2.save('glitchpic.jpg','JPEG')



#print(col)
print(width)
print(height)


# lorem ipsum code to do
