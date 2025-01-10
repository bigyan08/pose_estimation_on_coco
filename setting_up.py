import os
from pycocotools.coco import COCO

# Define the path to your COCO annotations and images
image_dir_train = 'dataset/train2017/'
ann_file_train = 'dataset/annotations_trainval2017/annotations/person_keypoints_train2017.json'
image_dir_val = 'path/to/coco/images/val2017/'
ann_file_val = 'path/to/coco/annotations/person_keypoints_val2017.json'

# Load COCO annotations for the training and validation sets
coco_train = COCO(ann_file_train)
coco_val = COCO(ann_file_val)

# Function to delete images without any human keypoints
def delete_images_without_humans(coco, image_dir):
    # Get all image IDs
    image_ids = coco.getImgIds()
    
    # Get the IDs of images that contain at least one person (keypoints)
    images_with_person_ids = []
    
    for image_id in image_ids:
        annotations = coco.loadAnns(coco.getAnnIds(imgIds=image_id))
        
        # Check if there are any keypoints for the 'person' category (category ID = 1)
        if any(ann['category_id'] == 1 and len(ann['keypoints']) > 0 for ann in annotations):
            images_with_person_ids.append(image_id)

    # Find the image IDs that do not contain humans
    images_without_person_ids = set(image_ids) - set(images_with_person_ids)

    # Get the image filenames for those images
    images_to_delete = coco.loadImgs(list(images_without_person_ids))

    # Delete the images from the file system
    for image_info in images_to_delete:
        image_file = image_info['file_name']
        image_path = os.path.join(image_dir, image_file)
        
        # Check if the file exists and then delete it
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Deleted: {image_file}")
    
    print(f"Total images deleted: {len(images_to_delete)}")

# Delete images without humans from both train and val sets
delete_images_without_humans(coco_train, image_dir_train)
delete_images_without_humans(coco_val, image_dir_val)
