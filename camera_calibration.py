import numpy as np
import cv2 as cv
import time

def calib_camera_from_chessboard(input_file, board_pattern, board_cellsize, K=None, dist_coeff=None, calib_flags=None):
    # Find 2D corner points from given images
    video = cv.VideoCapture(0)
    assert video.isOpened(), "Cannot read the given input, " + input_file

    img_points = []
    time_captured = 0

    valid, img = video.read()
    chessboard = np.zeros(img.shape, dtype=np.uint8)

    while True:
        valid, img = video.read()
        assert valid, "Video is not valid"

        display = img.copy()
        cv.putText(display, f"Selected: {len(img_points)}", (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        complete, pts = cv.findChessboardCorners(gray, board_pattern, flags=(cv.CALIB_CB_ADAPTIVE_THRESH+cv.CALIB_CB_NORMALIZE_IMAGE+cv.CALIB_CB_FAST_CHECK))

        if complete and time_captured + 3 < time.time():
            chessboard = img.copy()
            cv.drawChessboardCorners(chessboard, board_pattern, pts, complete)
            img_points.append(pts)
            time_captured = time.time()

        cv.imshow("Camera Calibration", cv.hconcat([display, chessboard]))

        key = cv.waitKey(10)
        if key == 27: # ESC
            break

    assert len(img_points) > 0, 'There is no set of complete chessboard points!'

    # Prepare 3D points of the chess board
    obj_pts = [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
    obj_points = [np.array(obj_pts, dtype=np.float32) * board_cellsize] * len(img_points) # Must be 'np.float32'

    video.release()

    # Calibrate the camera
    return cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], K, dist_coeff, flags=calib_flags)

if __name__ == '__main__':
    rms, K, dist_coeff, rvecs, tvecs = calib_camera_from_chessboard(input_file=0, board_pattern=(10, 7), board_cellsize=0.025)

    # Print calibration results
    print('## Camera Calibration Results')
    print(f'* RMS error = {rms}')
    print(f'* Camera matrix (K) = \n{K}')
    print(f'* Distortion coefficient (k1, k2, p1, p2, k3, ...) = {dist_coeff.flatten()}')