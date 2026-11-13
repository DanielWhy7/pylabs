import cv2
import numpy as np


def load_image(image_path: str) -> np.ndarray:
  """
  Loads an image from disk.
  :param image_path: path to the image file
  :return: image in BGR format as a numpy array
  """
  image = cv2.imread(image_path)
  if image is None:
    raise FileNotFoundError(f"Failed to read image file: '{image_path}'")
  return image


def crop_top_left(image: np.ndarray, width: int, height: int) -> np.ndarray:
  """
  Transformation (1): crops the image to specified dimensions,
  starting from the top-left corner. The crop is clamped to the
  image bounds if the requested size exceeds the image.
  :param image: source image
  :param width: target width in pixels
  :param height: target height in pixels
  :return: cropped image
  """
  if width <= 0 or height <= 0:
    raise ValueError("Crop dimensions must be positive")

  img_h, img_w = image.shape[:2]
  actual_w = min(width, img_w)
  actual_h = min(height, img_h)

  if (actual_w, actual_h) != (width, height):
    print(
      f"⚠️ Crop size {width}x{height} exceeds image "
      f"{img_w}x{img_h}; using {actual_w}x{actual_h} instead."
    )

  return image[:actual_h, :actual_w].copy()


def rotate_image(image: np.ndarray, angle: float) -> np.ndarray:
  """
  Transformation (4): rotates the image by a specified angle
  around the center, preserving all content (expanding the canvas).
  :param image: source image
  :param angle: rotation angle in degrees (counter-clockwise)
  :return: rotated image
  """
  img_h, img_w = image.shape[:2]
  center = (img_w / 2.0, img_h / 2.0)

  matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

  cos = abs(matrix[0, 0])
  sin = abs(matrix[0, 1])
  new_w = int(img_h * sin + img_w * cos)
  new_h = int(img_h * cos + img_w * sin)

  matrix[0, 2] += new_w / 2.0 - center[0]
  matrix[1, 2] += new_h / 2.0 - center[1]

  return cv2.warpAffine(image, matrix, (new_w, new_h))


def overlay_transparent(base: np.ndarray, overlay: np.ndarray, alpha: float) -> np.ndarray:
  """
  Transformation (10): overlays one image on another,
  making the overlaid image semi-transparent.
  :param base: bottom (opaque) image
  :param overlay: top image that is overlaid
  :param alpha: transparency of the top image in range [0, 1]
  :return: resulting image
  """
  if not 0.0 <= alpha <= 1.0:
    raise ValueError(f"Alpha must be in range [0, 1], got: {alpha}")

  base_h, base_w = base.shape[:2]
  resized_overlay = cv2.resize(overlay, (base_w, base_h))

  return cv2.addWeighted(base, 1.0 - alpha, resized_overlay, alpha, 0.0)
