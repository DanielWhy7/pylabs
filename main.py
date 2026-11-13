import argparse
import os
import sys

import cv2

from image_processor import (
  load_image,
  crop_top_left,
  rotate_image,
  overlay_transparent,
)
from visualizer import show_comparison


def build_parser() -> argparse.ArgumentParser:
  """
  Builds the command-line argument parser.
  :return: configured ArgumentParser
  """
  parser = argparse.ArgumentParser(
    description=(
      "Laboratory Work No. 3, Variant 1: cropping, rotation, and "
      "semi-transparent overlay for images downloaded in Lab No. 2."
    )
  )
  parser.add_argument("--image", required=True, help="Path to the base image")
  parser.add_argument("--overlay", required=True, help="Path to the overlay image")
  parser.add_argument("--output", required=True, help="Path to save the result")
  parser.add_argument(
    "--comparison",
    default="comparison.png",
    help="Path to save the comparison figure (default: comparison.png)",
  )
  parser.add_argument(
    "--crop_width", type=int, required=True, help="Crop width in pixels"
  )
  parser.add_argument(
    "--crop_height", type=int, required=True, help="Crop height in pixels"
  )
  parser.add_argument(
    "--angle", type=float, default=45.0, help="Rotation angle in degrees"
  )
  parser.add_argument(
    "--alpha",
    type=float,
    default=0.5,
    help="Transparency of the overlaid image in [0, 1]",
  )
  return parser


def run_pipeline() -> None:
  """
  Executes variant 1: load → crop → rotate → semi-transparent overlay
  → save → visualize.
  """
  parser = build_parser()
  args = parser.parse_args()

  try:
    base_image = load_image(args.image)
    overlay_image = load_image(args.overlay)

    print(f"📷 Original image size: {base_image.shape[1]}x{base_image.shape[0]}")
    print(f"🖼️ Overlay image size: {overlay_image.shape[1]}x{overlay_image.shape[0]}")

    cropped = crop_top_left(base_image, args.crop_width, args.crop_height)
    print(f"✂️ After cropping: {cropped.shape[1]}x{cropped.shape[0]}")

    rotated = rotate_image(cropped, args.angle)
    print(f"🔄 After rotation by {args.angle}°: {rotated.shape[1]}x{rotated.shape[0]}")

    result = overlay_transparent(rotated, overlay_image, args.alpha)
    print(f"✨ Final size: {result.shape[1]}x{result.shape[0]}")

    output_dir = os.path.dirname(os.path.abspath(args.output))
    os.makedirs(output_dir, exist_ok=True)
    if not cv2.imwrite(args.output, result):
      raise OSError(f"Failed to save result to '{args.output}'")
    print(f"💾 Result saved: {args.output}")

    show_comparison(
      original=base_image,
      result=result,
      save_path=args.comparison,
      result_path=args.output,
      show_in_terminal=True,
    )
    print(f"📊 Comparison figure saved: {args.comparison}")

  except FileNotFoundError as exc:
    print(f"❌ File not found: {exc}", file=sys.stderr)
  except ValueError as exc:
    print(f"❌ Value error: {exc}", file=sys.stderr)
  except OSError as exc:
    print(f"❌ I/O error: {exc}", file=sys.stderr)
  except Exception as exc:
    print(f"❌ Unexpected error: {exc}", file=sys.stderr)


if __name__ == "__main__":
  run_pipeline()
