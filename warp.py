import numpy as np


def inverse_warp(h, w, pts1, img1):
    img1 = np.array(img1)
    h, w, _ = img1.shape
    img2 = np.zeros((h, w, 3))
    pts2 = [[0, 0], [h, 0], [0, w], [h, w]]
    matrix = computeH(pts2, pts1)
    img2_pts = np.mgrid[0:h, 0:w]
    img2_pts = np.vstack((img2_pts[0].ravel(), img2_pts[1].ravel()))
    pts_matrix = np.vstack((img2_pts, np.ones((img2_pts.shape[1],), dtype=int)))
    img1_pts = matrix @ pts_matrix
    img1_pts = (img1_pts[:2]/img1_pts[2]).astype(int)
    img1_pts[0, :] = np.clip(img1_pts[0, :], 0, h-1)
    img1_pts[1, :] = np.clip(img1_pts[1, :], 0, w-1)
    img2[img2_pts[0, :].astype(int), img2_pts[1, :].astype(int)] = img1[img1_pts[0, :], img1_pts[1, :]]
    return img2




def computeH(pts1, pts2):
    pts1, pts2 = np.array(pts1), np.array(pts2)
    p_num = pts1.shape[0]

    a = np.zeros((p_num * 2, 8))
    b = pts2.reshape((p_num * 2,))

    for i in range(p_num):
        p1 = pts1[i]
        p2 = pts2[i]

        a[2 * i, 0:3] = np.append(p1, [1])
        a[2 * i, 6:] = [-p1[0] * p2[0], -p1[1] * p2[0]]

        a[2 * i + 1, 3:6] = np.append(p1, [1])
        a[2 * i + 1, 6:] = [-p1[0] * p2[1], -p1[1] * p2[1]]

    x = np.linalg.lstsq(a, b, rcond=None)
    x = np.append(x[0], [1]).reshape((3, 3))

    return x
