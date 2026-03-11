import sys
from PIL import Image


def main():
    img_path = sys.argv[1]

    # formation validation
    formats = [
        "PNG",
        "JPEG",
        "JPG",
        "BMP",
        "GIF",
        "TIFF",
        "WEBP",
        "ICO",
        "PPM",
        "PGM",
        "PBM",
    ]
    if not any(img_path.endswith(f".{fmt.lower()}") for fmt in formats):
        print("Unsupported file format.")
        sys.exit(1)

    rgb_matrix = get_rgb(img_path)
    edited_matrix = edit_rgb_matrix(rgb_matrix)
    output_path = "Matrix_" + img_path.split("\\")[-1]
    save_rgb_matrix_as_image(edited_matrix, output_path)
    print(f"Edited image saved as {output_path}")


def get_rgb(img_path):
    # Open the image and convert it to RGB mode
    img = Image.open(img_path)
    img = img.convert("RGB")
    width, height = img.size
    rgb_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            row.append((r, g, b))
        rgb_matrix.append(row)
    return rgb_matrix


def edit_rgb_matrix(rgb_matrix):
    # Example: Invert the colors
    edited_matrix = []
    for row in rgb_matrix:
        edited_row = []
        for r, g, b in row:
            r = r / 255.0
            g = g / 255.0
            b = b / 255.0
            r = r**1.5
            g = g**0.8
            b = b**1.5
            edited_row.append((r * 255, g * 255, b * 255))
        edited_matrix.append(edited_row)
    return edited_matrix


def save_rgb_matrix_as_image(rgb_matrix, output_path):
    height = len(rgb_matrix)
    width = len(rgb_matrix[0]) if height > 0 else 0
    img = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            r, g, b = rgb_matrix[y][x]
            img.putpixel((x, y), (int(r), int(g), int(b)))
    img.save(output_path)


if __name__ == "__main__":
    main()
