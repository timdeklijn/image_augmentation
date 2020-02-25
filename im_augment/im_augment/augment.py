"""augment.py

A set of image augmentation functions
"""

import matplotlib.pyplot as plt
from PIL import Image as pil_image
from PIL import ImageEnhance


def change_sharpness(img, factor=1.8):
    """Change the sharpness of the input image.

    Parameters
    ----------
    img : PIL.Image
        Input image
    factor : float, optional
        Factor to change sharpness by, 1.0 means no change, by default 1.8

    Returns
    -------
    PIL.Image
        Output image
    """
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def change_saturation(img, factor=1.8):
    """Change the saturation of the input image.

    Parameters
    ----------
    img : PIL.Image
        Input image
    factor : float, optional
        Factor to change saturation by, 1.0 means no change, by default 1.8

    Returns
    -------
    PIL.Image
        Output image
    """
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)


def change_contrast(img, factor=1.8):
    """Change the contrast of the input image

    Parameters
    ----------
    img : PIL.Image
        Input image
    factor : float, optional
        Factor to change contrast by, 1.0 means no change, by default 1.8

    Returns
    -------
    PIL.Image
        Output image
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def change_brightness(img, factor=1.8):
    """Modify the brightness of the input image.

    Parameters
    ----------
    img : PIL.Image
        Input image
    factor : float, optional
        Factor to change the brighntess with, 1.0 is no change, by default 1.8

    Returns
    -------
    PIL.Image
        Output image
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def rotate_image(img, angle=180):
    """Rotate the image by som degrees.

    Parameters
    ----------
    img : PIL.Image
        Input image
    angle : int, optional
        Rotate the image by this angle, can be any angle, by default 180

    Returns
    -------
    PIL.Image
        Rotated image
    """
    return img.rotate(angle)


def to_greyscale(img):
    """Convert the image to greyscale

    Parameters
    ----------
    img : PIL.Image
        Input image

    Returns
    -------
    PIL.Image
        Greyscale image
    """
    return img.convert("LA")


def scale_image(img, factor=0.8):
    """Scale an image, srinking the dimensions but keeping the original
    aspect ratio.

    Parameters
    ----------
    img : PIL.Image
        Input image
    factor : float, optional
        Factor to shrink the image by, by default 0.8

    Returns
    -------
    PIL.Image
        Image with less pixels.
    """
    original_size = img.size
    return img.resize(
        (int(original_size[0] * factor), int(original_size[1] * factor)),
        pil_image.ANTIALIAS,
    )


def crop_image(img, factor=0.8):
    """Crop an image, take the center factor of each dimension.
    The PIL.crop function takes the following arguments::

        (left, top, right, bottom)

    where (0,0) is located in the top left corner of an image.

    Parameters
    ----------
    img : PIL.image
        Input image
    factor : float, optional
        Factor to crop the image by, by default 0.8

    Returns
    -------
    PIL.Image
        Cropped image.
    """
    s = img.size
    width_margin = int((s[0] * (1 - factor)) / 2)
    height_margin = int((s[1] * (1 - factor)) / 2)
    return img.crop(
        (width_margin, height_margin, s[0] - width_margin, s[1] - height_margin)
    )


def show_image(img):
    """Show the input image in a matplotlib plot

    Parameters
    ----------
    img : PIL.Image
        Input image, will be plotted.
    """
    fig, ax = plt.subplots(1, 1)
    ax.axis("off")
    ax.imshow(img.convert("RGB"))
    plt.tight_layout()
    plt.show()
