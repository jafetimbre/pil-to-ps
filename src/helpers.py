from PIL import Image, ImageOps


def obj_mask(im):
    """Computes the mask for an image with transparent background

    Keyword arguments:
    im -- the input image (must be RGBA)
    """
    A = im.split()[-1]
    T = ImageOps.invert(A)
    return Image.merge("RGBA", (T, T, T, A))