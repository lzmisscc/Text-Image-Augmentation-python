from PIL import Image
from numpy import random
import albumentations as A
import numpy as np

transforms = [
    # A.Affine(always_apply=True, shear=None, scale=(0.8, .9), rotate=(-5, 5)),
    A.Perspective(always_apply=True, keep_size=True, scale=(0.01, 0.05)),
    # A.PiecewiseAffine(always_apply=True,
    #                   absolute_scale=False, ),
    A.ShiftScaleRotate(always_apply=True, ),
    A.GridDistortion(always_apply=True),
    A.OpticalDistortion(always_apply=True),
    A.NoOp(always_apply=True),
    A.RandomGridShuffle(always_apply=True)
]


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
    w, h = random.choice(range(source_w, w + 1)
                         ), random.choice(range(source_h, h + 1))
    return w, h


def blend_images1():
    img1 = Image.open(
        "merge_5000/0_20200102094021_4035a4f85da6444f822afb9da80b1424_OCR_HAIMA_TextMixFormula_1.jpg")
    img1 = img1.convert('RGBA')

    img2 = Image.open("merge_5000/D0002928.jpg")
    aug_fun = random.choice(transforms)
    aug_image = np.array(img2, np.uint8)
    aug_image = aug_fun(image=aug_image)['image']
    img2 = Image.fromarray(aug_image)

    img2 = img2.convert('RGBA')
    img2 = img2.resize(random_size(img2.size, 1.3))

    mask = Image.new(mode="L", size=img2.size,
                     color=(random.randint(1, 100), ))
    img1.paste(img2, box=random_localtion(img1.size, img2.size), mask=mask)
    img1.show()

    # img2 = img2.resize(img1.size)
    # img = Image.blend(img1, img2, 0.1)
    # img = img.convert('RGB')
    # img.show()


def mixup(image_a: Image, image_b: Image):
    img1, img2 = image_a.copy(), image_b.copy()

    aug_fun = random.choice(transforms)
    aug_image = np.array(img2, np.uint8)
    aug_image = aug_fun(image=aug_image)['image']
    img2 = Image.fromarray(aug_image)
    img2 = img2.convert('RGBA')
    img2 = img2.resize(random_size(img2.size, 1.3))

    mask = Image.new(mode="L", size=img2.size,
                     color=(random.randint(1, 100), ))
    img1.paste(img2, box=random_localtion(img1.size, img2.size), mask=mask)
    return img1


if __name__ == '__main__':
    import time
    for i in range(100):
        blend_images1()
