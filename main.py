from draw_helper import *
from warp import *
import matplotlib as plt
import skimage.io as skio


# TODO: change 2D points to 3D points


def main():

    img = skio.imread('sjerome.jpg')
    bbox_params = draw_bbox(img)
    corner_pts = draw_corner(bbox_params, img)
    print(corner_pts)
    a = bbox_params[1]
    b = bbox_params[0]
    pts1 = [corner_pts[1], corner_pts[0], (a[1],a[0]), (b[1],b[0])]
    im = inverse_warp(300, 600, pts1, img)
    skio.imsave('warped.png', im)


if __name__ == '__main__':
    main()