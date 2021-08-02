from PIL import Image
from numpy import random

def random_localtion(x, y):
    w = x[0] - y[0]
    h = x[1] - y[1]
    w, h = abs(w) + 1, abs(h) + 1
    w, h = random.choice(range(w)), random.choice(range(h))
    return w, h

def random_size(size, ratio=1.1):
    w, h = size
    w, h = abs(w), abs(h)
    w, h = int(w * ratio), int(h * ratio)
    source_w, source_h = int(w), int(h)
    w, h = random.choice(range(source_w, w + 1)), random.choice(range(source_h, h + 1))
    return w, h

def blend_images1():
    img1 = Image.open("merge_5000/0_20200102094021_4035a4f85da6444f822afb9da80b1424_OCR_HAIMA_TextMixFormula_1.jpg")
    img1 = img1.convert('RGBA')

    img2 = Image.open("merge_5000/D0002928.jpg")
    img2 = img2.convert('RGBA')
    img2 = img2.resize(random_size(img2.size, 1.3))

    mask = Image.new(mode="L", size=img2.size, color=(random.randint(1, 100), ))
    img1.paste(img2, box=random_localtion(img1.size, img2.size), mask=mask)
    # img1.show()

    # img2 = img2.resize(img1.size)
    # img = Image.blend(img1, img2, 0.1)
    # img = img.convert('RGB')
    # img.show()

if __name__ == '__main__':
    import time
    for i in range(1000):
        blend_images1()