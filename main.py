from draw_helper import *


# TODO: change 2D points to 3D points


def main():

    img = plt.imread('sjerome.jpg')
    bbox_params = draw_bbox(img)
    corner_pts = draw_corner(bbox_params, img)







if __name__ == '__main__':
    main()