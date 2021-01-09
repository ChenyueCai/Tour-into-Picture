import matplotlib.pyplot as plt
import skimage.io as skio
import numpy as np


# Key Func
def draw_bbox(img):

    plt.imshow(img)
    lu, rd = plt.ginput(2)
    ld = (lu[0], rd[1])
    ru = (rd[0], lu[1])

    fig, ax = plt.subplots()
    ax.imshow(img)
    print(lu, ld)
    ax.plot((lu[0], ld[0]), (lu[1], ld[1]),
            (ru[0], rd[0]), (ru[1], rd[1]),
            (lu[0], ru[0]), (lu[1], ru[1]),
            (ld[0], rd[0]), (ld[1], rd[1]), '-', linewidth=2)
    fig.savefig('bbox.png')
    return [lu, ld, ru, rd]


# Given (a,b), (c,d), give b and m in y = mx + n
# if a == c, return x = a
def to_line(pt1, pt2):
    a, b = pt1
    c, d = pt2
    if (c - a) != 0:
        m = (d - b) / (c - a)
        n = (b * c - a * d ) / (c - a)
        return [m, n]
    else:
        return [a]


def to_corner(vanishing_pt, b_bt, v2, h2):
    line_param = to_line(vanishing_pt, b_bt)
    v_pt1, v_pt2 = vanishing_pt
    b1, b2 = b_bt
    if v_pt1 < b1 and v_pt2 <= b2:
        h, v = h2, v2
    elif v_pt1 < b1 and v_pt2 > b2:
        h, v = 0, v2
    elif v_pt1 >= b1 and v_pt2 <= b2:
        h, v = h2, 0
    else:
        h, v = 0, 0
    if len(line_param) == 1:
        print('Parallel to y axis')
    elif line_param[0] == 0:
        print('Parallel to x axis')
    else:
        m, n = line_param
        h_x, h_y = (h - n) / m, h
        v_x, v_y = v, m * v + n
        if 0 <= h_x <= v2 and 0 <= h_y <= h2:
            return h_x, h_y
        else:
            return v_x, v_y


# Key Func
def draw_corner(bbox_params, img):
    h, w, _ = np.array(img).shape
    fig, ax = plt.subplots()
    ax.imshow(img)
    vanishing_pt = plt.ginput(1)[0]
    corner_pts = []
    for b_pt in bbox_params:
        x, y = to_corner(vanishing_pt, b_pt, w, h)
        corner_pts.append((x, y))
    for i in range(4):
        ax.plot((corner_pts[i][0], vanishing_pt[0]), (corner_pts[i][1], vanishing_pt[1]), '-', linewidth=2)
    lu, ld, ru, rd = bbox_params[0], bbox_params[1], bbox_params[2], bbox_params[3]
    ax.plot((lu[0], ld[0]), (lu[1], ld[1]),
            (ru[0], rd[0]), (ru[1], rd[1]),
            (lu[0], ru[0]), (lu[1], ru[1]),
            (ld[0], rd[0]), (ld[1], rd[1]), '-', linewidth=2)
    fig.savefig('bbox_with_corner.png')
    return

