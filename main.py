from PIL import Image, ImageDraw


# img.getpixel((x/y))
# puts out rgb values
# 2 layer for loop get average color
# find value on white to dark green
#

img = Image.open("pic.jpg")
width, height = img.size
img2 = Image.new('RGB',(width,height),0)
percent = 0

#test = img.getpixel(50, 50)
#print(test)
"""
for x in range(img.size[0]):
  for y in range(img.size[1]):
    #print(img.getpixel((x,y)))
    with open("imgval.txt", "a") as file:
        file.write(str(img.getpixel((x,y))))

file.close()

"""
for w in range(width):
    for h in range(height):
        percent+=1

        if(w<20):
            img2.ImageDraw.ImageDraw.point((h,w),(img.getpixel((h,w)),img.getpixel((h,w)),img.getpixel((h,w+20))))
        #    img2.putpixel((h,w), 50,50,50)
        #    img2.putpixel((h,w),        )

        if(w<20):

            img2.ImageDraw.point((h,w-20),(img.getpixel((h,w)),img.getpixel((h,w)),img.getpixel((h,w))))
        else:

            img2.ImageDraw.point((h,w-20),(img.getpixel((h,w)),img.getpixel((h,w)),img.getpixel((h,w+20))))

        percent+=1
        print(percent/(width*height))
    print("---------------------------------------------------------------")


img2.save('glitchpic.jpg','JPEG')



#print(col)
print(width)
print(height)


# lorem ipsum code to do
