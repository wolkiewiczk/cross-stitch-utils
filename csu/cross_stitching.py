import cairo
from PIL import Image

from helpers import get_pixel_scale
from figures import draw_x

THICK_LINE_DENSITY = 10
THICK_LINE = 2
SLIM_LINE = 1


def generate_pattern(image_path, new_pixel_scale=10):
    image = Image.open(image_path)
    pixel_scale = get_pixel_scale(image)
    new_pixel_scale = new_pixel_scale or pixel_scale
    width_in_squares = image.width // pixel_scale
    height_in_squares = image.height // pixel_scale
    thick_lines_width = THICK_LINE * (width_in_squares // THICK_LINE_DENSITY - 1)
    thick_lines_height = THICK_LINE * (height_in_squares // THICK_LINE_DENSITY - 1)
    slim_lines_width = SLIM_LINE * (width_in_squares - 1) - (width_in_squares // THICK_LINE_DENSITY - 1)
    slim_lines_height = SLIM_LINE * (height_in_squares - 1) - (height_in_squares // THICK_LINE_DENSITY - 1)

    surface_width = width_in_squares * new_pixel_scale + thick_lines_width + slim_lines_width
    surface_height = height_in_squares * new_pixel_scale + thick_lines_height + slim_lines_height
    surface = cairo.ImageSurface(
        cairo.FORMAT_ARGB32,
        surface_width,
        surface_height
    )
    ctx = cairo.Context(surface)
    x = 0
    y = 0
    ctx.rectangle(x, y, surface_width, surface_height)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    for row_num in range(1, height_in_squares+1):
        if not row_num % THICK_LINE_DENSITY:
            horizontal_line = THICK_LINE
        else:
            horizontal_line = SLIM_LINE
        for column_num in range(1, width_in_squares+1):
            if not column_num % THICK_LINE_DENSITY:
                vertical_line = THICK_LINE
            else:
                vertical_line = SLIM_LINE
            ctx.rectangle(x, y, new_pixel_scale, new_pixel_scale)
            color = image.getpixel(((column_num-1)*pixel_scale, (row_num-1)*pixel_scale))
            ctx.set_source_rgba(*(value / 255 for value in color))
            ctx.fill()
            x += new_pixel_scale + vertical_line
        x = 0
        y += new_pixel_scale + horizontal_line
    draw_x(ctx, surface_width/2, surface_height/2)
    surface.write_to_png(f'pattern_{image_path}')
