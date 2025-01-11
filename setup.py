import os
import json
from pycocotools.coco import COCO
from shutil import copyfile

# First portion is for the train dataset
# Paths
annotation_path = 'dataset/annotations_trainval2017/annotations/person_keypoints_train2017.json'
image_dir = 'dataset/train2017'
output_dir = 'dataset/output'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load COCO annotations
coco = COCO(annotation_path)

# Get all image IDs that have humans (category_id = 1)
human_category_id = 1
human_image_ids = set()
for ann in coco.anns.values():
    if ann['category_id'] == human_category_id:
        human_image_ids.add(ann['image_id'])

# Get all image file names with humans
human_images = [coco.imgs[img_id]['file_name'] for img_id in human_image_ids]

# Copy images with humans to the output directory
for image_name in human_images:
    src = os.path.join(image_dir, image_name)
    dst = os.path.join(output_dir, image_name)
    if os.path.exists(src):
        copyfile(src, dst)

print(f"Filtered {len(human_images)} images with humans.")

#Second portion is for the validation set
# Paths
annotation_path = 'dataset/annotations_trainval2017/annotations/person_keypoints_val2017.json'
image_dir = 'dataset/val2017'
output_dir = 'dataset/output_val'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load COCO annotations
coco = COCO(annotation_path)

# Get all image IDs that have humans (category_id = 1)
human_category_id = 1
human_image_ids = set()
for ann in coco.anns.values():
    if ann['category_id'] == human_category_id:
        human_image_ids.add(ann['image_id'])

# Get all image file names with humans
human_images = [coco.imgs[img_id]['file_name'] for img_id in human_image_ids]

# Copy images with humans to the output directory
for image_name in human_images:
    src = os.path.join(image_dir, image_name)
    dst = os.path.join(output_dir, image_name)
    if os.path.exists(src):
        copyfile(src, dst)

print(f"Filtered {len(human_images)} images with humans.")