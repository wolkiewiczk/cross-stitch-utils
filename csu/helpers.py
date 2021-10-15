import json
from textwrap import wrap


with open('color_map.json', 'r') as file:
    COLOR_MAP = json.load(file)


def hex_to_rgb(hex_color):
    """
    Converts hex color string into rgb tuple with values in range <0, 1>.
    Args:
        hex_color (str): color as hexadecimal number.
    Returns:
        3-element tuple
    """
    hex_color = hex_color.strip('#')
    return tuple(int(color_part, 16) / 255 for color_part in wrap(hex_color, 2))


def get_divisors(num):
    """
    Gets the divisors of the given integer.
    Args:
        num (int): number for which to find the divisors.
    Returns:
        set
    """
    divisors = {i for i in range(1, num // 2 + 1) if not num % i}
    divisors.add(num)
    return divisors


def get_pixel_scale(image):
    """
    Gets the width of one pixel art square in pixels.
    Args:
        image (PIL.Image) - image from which to get the pixel scale
    Returns:
        int
    """
    width_divisors = get_divisors(image.width)
    height_divisors = get_divisors(image.height)
    divisors = sorted(list(width_divisors.intersection(height_divisors)), reverse=True)
    # The last divisor is always 1 which is always a valid choice so we don't need to check it.
    for divisor in divisors[:-1]:
        for y in range(0, image.height, divisor):
            for x in range(0, image.width, divisor):
                square = image.crop((x, y, x+divisor, y+divisor))
                if len(square.getcolors(maxcolors=len(COLOR_MAP))) != 1:
                    break
            else:
                continue
            break
        else:
            return divisor
    return 1


