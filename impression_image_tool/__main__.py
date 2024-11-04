"""
The main CLI application
"""
import io
import os
from distutils.command.install import value

import cairosvg
import rich_click as click
from PIL import Image


def rasterize_svg(svg_path: str, output_size: int = 100):
    """
    :param svg_path: Path to the SVG file that needs to be rasterized.
    :type svg_path: str
    :param output_size: The desired width and height of the output PNG image.
    :type output_size: int
    :return: A PIL Image object of the rasterized SVG.
    :rtype: PIL.Image.Image
    """
    png_data = cairosvg.svg2png(url=svg_path, output_width=output_size, output_height=output_size)
    return Image.open(io.BytesIO(png_data))


def arrange_logos_on_canvas(logos: list, canvas_size: tuple[int, int], logo_size: int, padding: int):
    """
    :param logos: List of logo images to be arranged on the canvas.
    :param canvas_size: Tuple indicating the size of the canvas (width, height).
    :param logo_size: Integer specifying the size of each logo (assumed to be square).
    :param padding: Integer specifying the padding between logos.
    :return: A PIL Image object with the logos arranged on the canvas.
    """
    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))
    num_rows = canvas_size[1] // (logo_size + padding)
    num_cols = canvas_size[0] // (logo_size + padding)
    x_offset = (canvas_size[0] - (num_cols * logo_size + (num_cols - 1) * padding)) // 2
    y_offset = (canvas_size[1] - (num_rows * logo_size + (num_rows - 1) * padding)) // 2

    for row in range(num_rows):
        for col in range(num_cols):
            idx = row * num_cols + col
            if idx >= len(logos):
                break
            x = x_offset + col * (logo_size + padding)
            y = y_offset + row * (logo_size + padding)
            canvas.paste(logos[idx], (x, y), logos[idx])

    return canvas


def create_logo_grid(input_folder, canvas_size=(1000, 1000), logo_size=100, padding=20):
    """
    :param input_folder: Directory path containing SVG files to be included in the logo grid.
    :param canvas_size: Tuple specifying the size of the canvas in pixels (width, height).
    :param logo_size: Integer specifying the size in pixels to which each logo should be resized.
    :param padding: Integer specifying the amount of padding in pixels between logos on the canvas.
    :return: A canvas object with the logos arranged in a grid pattern.
    """
    logos = []

    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            svg_path = os.path.join(input_folder, filename)
            logo = rasterize_svg(svg_path, logo_size)
            logos.append(logo)

    canvas = arrange_logos_on_canvas(logos, canvas_size, logo_size, padding)
    return canvas


def generate_unique_filename() -> str:
    """

    :return:
    """
    return


@click.group(help="The base command-line interface for the tool.")
@click.option("--logos-path", type=str, help="The absolute path to where the logos are stored.")
@click.pass_context
def cli(context: click.Context, logos_path: str) -> None:
    """
    The base command-line interface for the tool.
    :param logos_path:
    :param context:
    :return:
    """
    if not context:
        raise ValueError("The click context is invalid.")

    context.ensure_object(dict)
    context.obj["LOGOS_PATH"] = logos_path


@cli.command("generate", help="Generate a logo.")
@click.option("--output-path", type=str, help="The absolute path to where generated logos should be stored.")
@click.option("--logo-size", type=int, help="The uniform size of the logo.")
@click.option("--padding", type=int, help="The amount to pad the logos by.")
@click.pass_context
def cli_generate(context: click.Context, padding: int, logo_size: int, output_path: str) -> None:
    """
    Generate a logo.
    :param padding:
    :param logo_size:
    :param output_path:
    :param context:
    :return:
    """
    # Usage example
    logos_path: str = context.obj["LOGOS_PATH"]
    if not logos_path:
        raise ValueError("The absolute path to where the logos are stored is required.")
    if not os.path.isdir(logos_path):
        raise IOError("The absolute path to where the logos are stored is invalid.")
    input_folder = logos_path  # Set this to the path where SVG logos are stored
    output_image_path = "output_logo_grid.png"
    canvas_size = (1000, 1000)
    logo_size = 100
    padding = 20

    canvas = create_logo_grid(input_folder, canvas_size, logo_size, padding)
    canvas.save(output_image_path)
    print(f"Saved logo grid to {output_image_path}")


if __name__ == "__main__":
    try:
        cli()
    except Exception as exc:
        print(exc)
