import os
from PIL import Image

def compress_jpg_inplace(start_path="."):
    # Normalize the path
    start_path = os.path.abspath(start_path)

    for root, _, files in os.walk(start_path):
        for file in files:
            if file.lower().endswith(".jpg"):   # handles .jpg and .JPG
                file_path = os.path.join(root, file)

                try:
                    print(f"Compressing: {file_path}")

                    # Open image
                    img = Image.open(file_path)

                    # Re-save (overwrite) with optimized compression
                    img.save(
                        file_path,
                        "JPEG",
                        optimize=True,          # better compression
                        quality=85,             # visually lossless
                        progressive=True,       # more compressed
                        subsampling=0           # best (no color loss)
                    )

                    print(f"✔ Done: {file_path}")

                except Exception as e:
                    print(f"❌ Error compressing {file_path}: {e}")

    print("\nAll JPGs processed.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 2:
        compress_jpg_inplace(sys.argv[1])
    else:
        compress_jpg_inplace(".")   # default: current directory
