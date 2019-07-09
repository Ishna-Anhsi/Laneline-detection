import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from importlib import reload
import utils; reload(utils)
from utils import *

calibration_dir = "camera_cal"


cal_imgs_paths = glob.glob(calibration_dir + "/*.jpg")

cx = 9
cy = 6

def findChessboardCorners(img, nx, ny):
    """
    Finds the positions of internal corners of the supplied chessboard image (must be grayscale)
    nx and ny parameters respectively indicate the number of inner corners in the x and y directions
    """
    return cv2.findChessboardCorners(img, (nx, ny), None)        
	

	


def findImgObjPoints(imgs_paths, nx, ny):
    """
    Returns the objects and image points computed for a set of chessboard pictures taken from the same 
    camera. nx and ny parameters respectively indicate the number of inner corners in the x and y 
    directions.
    
    """
    
    # Arrays to store object points and image points from all the images.
    objpts = []  # 3d point in real world space
    imgpts = []  # 2d points in image plane(These image points are locations where two black squares
    
    #touch each other in chess boards).
    
    # Pre-compute what our object points in the real world should be (the z dimension is 0 as we 
    # assume a flat surface)
    
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    
    objp = np.zeros((nx * ny, 3), np.float32) # pattern 9*6 grid

    objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
    
    for img_path in imgs_paths:
        img = load_image(img_path)
        gray = to_grayscale(img)
        ret, corners = findChessboardCorners(gray, nx, ny)
        
        if ret:
            # Found the corners of an image
            #corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpts.append(corners)
            # Add the same object point since they don't change in the real world
            
            objpts.append(objp)
    
    
    return objpts, imgpts
opts, ipts = findImgObjPoints(cal_imgs_paths, cx, cy)
   