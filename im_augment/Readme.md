# im_augment

A group of functions to augment images. These augmented images can be used
as input form Machinel Learning algorithms that need large volumes of
training data.

Note that this is not a magic bullet. Not all algorithms will have improved
accuracy when using image augmentations to increase input volume.

## Install

To install, just use:

``` sh
pip install im_augment
```

## Use

```python
from PIL import Image as pil_image
import im_augment as aug

img = pil_image.open("parrots.jpg")
img = aug.crop_image(img)
aug.show_image(img)
```

## Functionality

These functions can be called from the `im_augment` package.

```
rotate_image(img)
to_greyscale(img)
resize_image(img, factor=0.8)
crop_image(img, factor=0.8)
show_image(img)
flip_image(img)
random_augment(img)
change_sharpness(img, factor=1.8)
change_saturation(img, factor=1.8)
change_contrast(img, factor=1.8)
change_brightness(img, factor=1.8)
```