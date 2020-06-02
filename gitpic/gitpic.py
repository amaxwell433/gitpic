from PIL import Image, ImageColor
from tqdm import tqdm

class Gitpic:
    def __init__(self, **kwargs):
        self.path = kwargs.get('img')
        self.img = Image.open(self.path)
        self.width, self.height = self.img.size
        self.new_img = Image.new('RGB',(self.width + 1,self.height + 1),(255,255,255))
        self.percent = 0

        self.offset = 5e-02

    def generate_image(self):
        print(self.img)
        for w in tqdm(range(self.width)):
            for h in range(self.height):
                if(w<self.offset):
                    self.new_img.putpixel((w+1,h+1),(self.img.getpixel((w,h))[0],self.img.getpixel((w,h))[1],self.img.getpixel((w,h))[2]))
                if(w<self.offset):
                    self.new_img.putpixel((w,h),(self.img.getpixel((w,h))[0],self.img.getpixel((w,h))[1],self.img.getpixel((w,h))[2]))
                else:
                    self.new_img.putpixel((w,h),(self.img.getpixel((w,h))[0],self.img.getpixel((w,h))[1],self.img.getpixel((w,h))[2]))

        path = self.path.replace(".jpg", "") #change to be any file format
        self.new_img.save(f"{path}_glitched.jpg")
