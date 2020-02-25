from PIL import Image as pil_image
import im_augment as aug

if __name__ == "__main__":
    print("[*] Image augmentation scripts")
    img = pil_image.open("parrots.jpg")
    img = aug.change_sharpness(img, factor=1.8)
    aug.show_image(img)
