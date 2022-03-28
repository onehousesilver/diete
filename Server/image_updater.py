# coding=utf8
import os
from PIL import Image
import glob

class ImageUpdater():
    
    def update(self):
        files = glob.glob('C:\\SSAFY\\workspace\\2학기\\02_특화_프로젝트\\clone\\특화-프로젝트\\Server\\images\\*.jpg')

        for f in files:
            img = Image.open(f)
            img_resize = img.resize((512, 512))
            title, ext = os.path.splitext(f)
            img_resize.save(title + ext)
    

def main():
    print("start imageUpdater")

    print("initializing imageUpdater")
    imageUpdater = ImageUpdater()
    print("finished")

    print("start update")
    imageUpdater.update()
    print("finished")

    print("finished imageUpdater")


if __name__ == '__main__':
    main()
