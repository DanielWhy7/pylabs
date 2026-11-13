import cv2
import matplotlib.pyplot as plt
import numpy as np


def _show_in_terminal(image_path: str) -> bool:
  """
  Renders an image file inline in a Kitty-protocol terminal using term-image.
  :param image_path: path to the image file
  :return: True if the image was rendered, False if term-image is unavailable
       or the terminal does not support the Kitty graphics protocol
  """
  try:
    from term_image.image import from_file
  except ImportError:
    print(
      "ℹ️ term-image is not installed; skipping terminal preview. "
      "Install with: pip install term-image --no-deps"
    )
    return False

  try:
    from_file(image_path).draw()
    return True
  except Exception as exc:
    print(f"ℹ️ Terminal image rendering skipped: {exc}")
    return False


def show_comparison(
  original: np.ndarray,
  result: np.ndarray,
  save_path: str,
  result_path: str | None = None,
  show_in_terminal: bool = True,
) -> None:
  """
  Displays the original and processed images side by side, saves the plot,
  and optionally renders the processed result inline in the terminal.
  :param original: original image in BGR
  :param result: processed image in BGR
  :param save_path: path to save the comparison figure
  :param result_path: path to the saved result image (needed for terminal display);
            if None, the result array is written to a temp file
  :param show_in_terminal: if True, render the result using term-image
  """
  ## fig, axes = plt.subplots(1, 2, figsize=(14, 7))

  ## axes[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
  ## axes[0].set_title(f"Original image ({original.shape[1]}x{original.shape[0]})")
  ## axes[0].axis("off")

  ## axes[1].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
  ## axes[1].set_title(
  ##   f"Result: crop + rotate + overlay ({result.shape[1]}x{result.shape[0]})"
  ## )
  ## axes[1].axis("off")

  ## fig.tight_layout()
  ## fig.savefig(save_path, dpi=120)
  ## plt.show()

  if not show_in_terminal:
    return

  if result_path is None:
    import tempfile, os
    fd, result_path = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    cv2.imwrite(result_path, result)

  _show_in_terminal(result_path)
