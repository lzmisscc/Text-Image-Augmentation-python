from augment import distort, perspective, stretch
from random import choice


def distort_(src):
    return distort(src, 8)


def perspective_(src):
    return perspective(src, )


def stretch_(src):
    return stretch(src, 4)


def No_Op_(src):
    return src


aug_colletion = [distort_, perspective_, stretch_, No_Op_]


def random_ocraug(src):
    aug = choice(aug_colletion)
    dst = aug(src)
    return dst

