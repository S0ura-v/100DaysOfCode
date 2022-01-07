from PIL import Image
import numpy as np


class WaterMark():
    def __init__(self, path_to_img):
        self.img = Image.open(path_to_img)
        self.arr_img = np.array(self.img)
        self.height, self.width = self.img.size

    def add_watermark(self, main_img: Image):
        """Adds a watermark to the main image"""
        main_arr = main_img.arr_img

        # formatting the image to suit the watermark dimensions
        self.format_image(main_img=main_img)

        # adding watermark

        # this wierd math is just to add some padding around the watermark
        for row in range(int(-1 * self.height/2), int((-1 * (self.height) / 2 * 3))):
            for pix in range(int(-1 * self.width/2), int((-1 * (self.width) / 2 * 3))):
                r = int(row - self.height/2)
                c = int(pix - self.width/2)
                main_img[row][pix] = self.img_arr[r][c]

    def format_image(self, main_img: Image):
        """This Function formats the image of the current class such that it is fit to be used as a watermark.
           However, I recommend that the watermark image should be near to a square"""
        # cropping extra edges
        if self.height not in range(self.width - 25, self.width + 25):
            if self.height > self.width:
                diff = self.height - self.width
                self.img.crop((0, round(diff/2), 0, round(diff/2)))
            else:
                diff = self.width - self.height
                self.img.crop((round(diff/2), 0, round(diff/2), 0))

        # setting the ratio of the image , The ratio will be 8:100
        self.height = 8 / 100 * main_img.height
        self.width = 8 / 100 * main_img.width
        self.img.resize((self.width, self.height))


class Image():
    def __init__(self, path_to_img):
        self.img = Image.open(path_to_img)
        self.arr_img = np.array(self.img)
        self.height, self.width = self.img.size
