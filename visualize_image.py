import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mimg
def visualize_image():
    folder_path = './runs/detect/exp'
    detect_image_paths = os.listdir(folder_path)
    random_lst =  random.sample(detect_image_paths, 8)
    lst = [folder_path + i for i in random_lst]
    print(lst)
    fig, axes = plt.subplots(2,4, figsize=(15,8))
    axes = axes.flatten()
    for i, image_path in enumerate(lst):
        image = mimg.imread(image_path)
        print(image)
        axes[i].imshow(image)
        axes[i].axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    visualize_image()