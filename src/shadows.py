from PIL import Image, ImageFilter


def drop_shadow(im, blur=5, offset=(0,0), col=(0,0,0)):
    """Creates a drop shadow for the objects on a transparent background

    Keyword arguments:
    im -- the input image (must be RGBA)
    blur -- amount of the shadow blur
    offset -- the (x, y) offset of the shadow relative to the object
    col -- (r, g, b) values for the shadow color
    """
    bg = Image.new('RGBA', im.size, (0, 0, 0, 0))
    sh_base = Image.new('RGBA', im.size, (col[0], col[1], col[2], 0))
    sh = Image.new("RGBA", im.size, color=(col[0], col[1], col[2], 255))
    A = im.split()[-1]
    A = A.filter(ImageFilter.GaussianBlur(blur))
    sh_base = Image.composite(sh, sh_base, A)

    bg.paste(sh_base, (offset[0], offset[1]))
    bg.paste(im, (0, 0), im)
    return bg


def inner_shadow(im,):
    pass