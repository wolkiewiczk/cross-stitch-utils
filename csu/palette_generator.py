import cairo
import json
from math import ceil

from helpers import hex_to_rgb


with open('color_map.json', 'r') as file:
    colors_map = json.load(file)

PIXEL_SCALE = 10
ROW_SIZE = 12
WIDTH = ROW_SIZE * PIXEL_SCALE
HEIGHT = ceil(len(colors_map) / ROW_SIZE) * PIXEL_SCALE

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

x = 0
y = 0
for color in colors_map:
    ctx.rectangle(x, y, 10, 10)
    ctx.set_source_rgb(*hex_to_rgb(color))
    ctx.fill()
    x += 10
    if x >= WIDTH:
        x = 0
        y += 10

surface.write_to_png('palette.png')
