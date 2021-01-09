import matplotlib.pyplot as plt
import skimage.io as skio
import numpy as np


# Key Func
def draw_bbox(img):

    plt.imshow(img)
    lu, rd = plt.ginput(2, timeout=60)
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


# Given vanishing point, a single bounding box corner points
# and bounding vertical and horizontal lines
def to_corner(vanishing_pt, b_bt, v1, v2, h1, h2):
    line_param = to_line(vanishing_pt, b_bt)
    v_pt1, v_pt2 = vanishing_pt
    b1, b2 = b_bt
    if v_pt1 < b1 and v_pt2 <= b2:
        h, v = h2, v2
    elif v_pt1 < b1 and v_pt2 > b2:
        h, v = h1, v2
    elif v_pt1 >= b1 and v_pt2 <= b2:
        h, v = h2, v1
    else:
        h, v = h1, v1
    if len(line_param) == 1:
        print('Parallel to y axis')
    elif line_param[0] == 0:
        print('Parallel to x axis')
    else:
        m, n = line_param
        h_x, h_y = (h - n) / m, h
        v_x, v_y = v, m * v + n
        if v1 <= h_x <= v2 and h1 <= h_y <= h2:
            return v_x, v_y
        else:
            return h_x, h_y


# Key Func
def draw_corner(bbox_params, img, w1, w2, h1, h2):

    fig, ax = plt.subplots()
    ax.imshow(img)
    vanishing_pt = plt.ginput(1)[0]
    corner_pts = []
    for b_pt in bbox_params:
        x, y = to_corner(vanishing_pt, b_pt, w1, w2, h1, h2)
        corner_pts.append((x, y))
    for i in range(4):
        ax.plot((corner_pts[i][0], vanishing_pt[0]), (corner_pts[i][1], vanishing_pt[1]), '-', linewidth=2)
    lu, ld, ru, rd = bbox_params[0], bbox_params[1], bbox_params[2], bbox_params[3]
    ax.plot((lu[0], ld[0]), (lu[1], ld[1]),
            (ru[0], rd[0]), (ru[1], rd[1]),
            (lu[0], ru[0]), (lu[1], ru[1]),
            (ld[0], rd[0]), (ld[1], rd[1]), '-', linewidth=2)
    fig.savefig('bbox_with_corner.png')
    return vanishing_pt, corner_pts


def invert_xy(pts):
    inverted = []
    for pt in pts:
        inverted.append((pt[1], pt[0]))
    return inverted


def add_margin(img, width):
    img = np.array(img)
    h, w, _ = img.shape
    new_im = np.zeros((h + 2 * width, w + 2 * width, 3))
    new_im[width: h + width, width: w + width, :] = img
    return new_im.astype(np.int), h, w


def get_h_pts(v_pt, key_points, line, pos):
    c1, c2 = key_points['c1'], key_points['c2']
    b1, b2 = key_points['b1'], key_points['b2']
    l1_param = to_line(v_pt, c1)
    l2_param = to_line(v_pt, c2)
    if pos == 'h':
        c1 = (line, line * l1_param[0] + l1_param[1])
        c2 = (line, line * l2_param[0] + l2_param[1])
    else:
        c1 = ((line - l1_param[1]) / l1_param[0], line)
        c2 = ((line - l2_param[1]) / l2_param[0], line)

    return {'c1': c1, 'c2': c2, 'b1': b1, 'b2': b2}





# TODO: Define 3D location for each phase and learn how to plot in matplotlib
# TODO: using some margin methods to extend 