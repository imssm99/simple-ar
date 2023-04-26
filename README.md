# Simple AR

Simple AR project using OpenCV, written in Python3

## Contents

- `simple_ar.py`: Main AR script
- `camera_calibration.py`: Camera calibration module/script
- `calibration_result.npz`: My Camera (C270) calibration data
- `bunny.xyz`: Stanford bunny xyz point data

## Usage

### Simple AR

- If `calibration_result.npz` not exist, it runs camera calibration first
- It visualizes object on chessboard
- `w`, `a`, `s`, `d`: Move object
- `q`, `e`: Rotate object
- `esc`: Exit

### Camera Calibration

- It calibrates automatically when chessboard recognized
- Result is saved as `calibration_result.npz`
- `esc`: End calibration

## Calibration Data

### Logitech C270

```
K: [[1.41541639e+03 0.00000000e+00 6.78406116e+02]
 [0.00000000e+00 1.41585591e+03 3.59810488e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
dist coefficient: [[ 8.47980499e-02  5.57913636e-01  2.86036812e-03  4.13857551e-03  -4.42017221e+00 ]]
```

## Example (stanford bunny)

https://user-images.githubusercontent.com/15193055/234592479-429dd65b-7bf8-4782-ba51-52a857c57cfc.mp4

