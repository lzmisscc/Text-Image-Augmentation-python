# coding utf8
from os import cpu_count
from posixpath import split
import albumentations as A
import cv2
import pdb
from os.path import join, basename, exists
import ray
import pickle
from math import ceil
import numpy as np


# Declare an augmentation pipeline
transforms = [
    # A.RandomBrightnessContrast(always_apply=True),
    # A.RandomContrast(always_apply=True),
    # A.RandomShadow(always_apply=True),
    # # A.RandomFog(always_apply=True),
    # A.ChannelDropout(always_apply=True),
    # # A.ChannelShuffle(always_apply=True),
    # A.RandomToneCurve(always_apply=True),
    # # A.RandomRain(always_apply=True, blur_value=5),
    # # A.RandomSnow(always_apply=True),
    # # A.RandomSunFlare(always_apply=True),
    # # A.ToGray(always_apply=True),
    # A.RandomBrightness(always_apply=True),
    # # A.MedianBlur(always_apply=True),
    # A.MotionBlur(always_apply=True),
    # A.GaussianBlur(always_apply=True),
    # # A.Blur(always_apply=True, blur_limit=5),
    # A.CLAHE(always_apply=True),
    # A.JpegCompression(always_apply=True),
    # # A.ToSepia(always_apply=True),
    # A.Sharpen(always_apply=True),
    # A.ISONoise(always_apply=True),
    # A.InvertImg(always_apply=True),
    # A.MultiplicativeNoise(always_apply=True),
    # # A.RGBShift(always_apply=True),
    # A.HueSaturationValue(always_apply=True),
    # # A.HistogramMatching(always_apply=True),
    # # A.GlassBlur(always_apply=True, sigma=0.3),
    # # A.FancyPCA(always_apply=True),
    # # A.FDA(always_apply=True),
    # # A.Emboss(always_apply=True),
    # # A.ColorJitter(always_apply=True),
    # # A.Downscale(always_apply=True),
    # # A.Superpixels(),
]

transforms += [
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
