from PIL import Image as pil_image
import im_augment as aug
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("[*] Image augmentation scripts")
    img = pil_image.open("parrots.jpg")

    fig, axes = plt.subplots(5, 5, figsize=(10, 10))
    for i in range(5):
        for j in range(5):
            axes[i, j].imshow(aug.random_augment(img))
            axes[i, j].axis("off")
    plt.tight_layout()
    plt.savefig("augment_output.png")
