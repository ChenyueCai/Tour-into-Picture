from draw_helper import *
from warp import *
import matplotlib.pyplot as plt
import skimage.io as skio
from skimage.transform import rescale, resize



# TODO: change 2D points to 3D points


def main():

    img = skio.imread('sjerome.jpg')
    margin = 200
    new_img, img_h, img_w = add_margin(img, margin)
    bbox_params = draw_bbox(new_img)
    v_pt, corner_pts = draw_corner(bbox_params, new_img, margin, margin + img_w, margin, margin + img_h)
    corner_pts = invert_xy(corner_pts)


    h, w, d = 500, 700, 850
    bbox_params_inv = invert_xy(bbox_params)
    print(bbox_params_inv)


    pts_l_side = {'c1': corner_pts[1], 'c2': corner_pts[0], 'b1': bbox_params_inv[1], 'b2': bbox_params_inv[0]}
    pts_s_side = {'c1': corner_pts[3], 'c2': corner_pts[2], 'b1': bbox_params_inv[3], 'b2': bbox_params_inv[2]}
    pts_ceiling = {'c1': corner_pts[0], 'c2': corner_pts[2], 'b1': bbox_params_inv[0], 'b2': bbox_params_inv[2]}
    pts_floor = {'c1': corner_pts[1], 'c2': corner_pts[3], 'b1': bbox_params_inv[1], 'b2': bbox_params_inv[3]}

    pts_l_side = get_h_pts(v_pt, pts_l_side, margin, 'v')
    pts_l_side = [pts_l_side['c1'],pts_l_side['c2'], pts_l_side['b1'], pts_l_side['b2']]
    inverse_warp(h, w, pts_l_side, new_img, 'l_side.png')

    pts_r_side = get_h_pts(v_pt, pts_s_side, margin+img_w, 'v')
    pts_r_side = [pts_r_side['b1'], pts_r_side['b2'], pts_r_side['c1'], pts_r_side['c2']]
    inverse_warp(h, w, pts_r_side, new_img, 'r_side.png')

    pts_ceiling = get_h_pts(v_pt, pts_ceiling, margin, 'h')
    pts_ceiling = [pts_ceiling['b1'], pts_ceiling['c1'], pts_ceiling['b2'], pts_ceiling['c2']]
    inverse_warp(d, w, pts_ceiling, new_img, 'ceiling.png')

    pts_floor = get_h_pts(v_pt, pts_floor, margin+img_h, 'h')
    pts_floor = [pts_floor['c1'], pts_floor['b1'], pts_floor['c2'], pts_floor['b2']]
    inverse_warp(d, w, pts_floor, new_img, 'floor.png')
    

    back_pt1_x, back_pt1_y = bbox_params_inv[0]
    back_pt2_x, back_pt2_y = bbox_params_inv[-1]
    back = new_img[int(back_pt1_x): int(back_pt2_x), int(back_pt1_y): int(back_pt2_y), :].astype(np.uint8)
    back = resize(back, (h, w, 3)) * 256
    skio.imsave('back.png', back.astype(np.uint8))





if __name__ == '__main__':
    main()