

def draw_x(ctx, x, y, color=(255, 0, 0), length=5, width=1):
    ctx.move_to(x, y)
    ctx.line_to(x+length, y-length)
    ctx.move_to(x, y)
    ctx.line_to(x + length, y + length)
    ctx.move_to(x, y)
    ctx.line_to(x - length, y + length)
    ctx.move_to(x, y)
    ctx.line_to(x - length, y - length)
    ctx.set_line_width(width)
    ctx.set_source_rgb(*color)
    ctx.stroke()



