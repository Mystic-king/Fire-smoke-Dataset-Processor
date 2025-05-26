# For Train Data
import os
import csv

# 🔧 Set paths
images_dir = '/Users/shreyas_mavale/Desktop/Project/train/images'
labels_dir = '/Users/shreyas_mavale/Desktop/Project/train/labels'
output_csv = '/Users/shreyas_mavale/Desktop/Project/train/labels.csv'

# 🧠 TEMP class mapping override (if you know it)
# CLASS_MAP = {0: 'fire', 1: 'smoke'}  # Comment this if using dynamic check

# Get all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Write CSV
with open(output_csv, 'w', newline='') as csvfile:
    fieldnames = ['filename', 'fire', 'smoke']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for img_file in image_files:
        basename = os.path.splitext(img_file)[0]
        label_file = basename + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        fire_flag = 0
        smoke_flag = 0

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if not parts:
                        continue
                    try:
                        class_id = int(parts[0])
                        # 👇 Change these IDs if fire/smoke are different
                        if class_id == 0:
                            fire_flag = 1
                        elif class_id == 1:
                            smoke_flag = 1
                    except ValueError:
                        print(f"[WARNING] Invalid line in {label_file}: {line.strip()}")
        else:
            print(f"[INFO] No label file found for: {img_file}")

        writer.writerow({
            'filename': img_file,
            'fire': fire_flag,
            'smoke': smoke_flag
        })

print(f"\n✅ Done! CSV saved to {output_csv}")



# For Test Data
import os
import csv

# 🔧 Set paths
images_dir = '/Users/shreyas_mavale/Desktop/Project/test/images'
labels_dir = '/Users/shreyas_mavale/Desktop/Project/test/labels'
output_csv = '/Users/shreyas_mavale/Desktop/Project/test/labels.csv'

# 🧠 TEMP class mapping override (if you know it)
# CLASS_MAP = {0: 'fire', 1: 'smoke'}  # Comment this if using dynamic check

# Get all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Write CSV
with open(output_csv, 'w', newline='') as csvfile:
    fieldnames = ['filename', 'fire', 'smoke']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for img_file in image_files:
        basename = os.path.splitext(img_file)[0]
        label_file = basename + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        fire_flag = 0
        smoke_flag = 0

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if not parts:
                        continue
                    try:
                        class_id = int(parts[0])
                        # 👇 Change these IDs if fire/smoke are different
                        if class_id == 0:
                            fire_flag = 1
                        elif class_id == 1:
                            smoke_flag = 1
                    except ValueError:
                        print(f"[WARNING] Invalid line in {label_file}: {line.strip()}")
        else:
            print(f"[INFO] No label file found for: {img_file}")

        writer.writerow({
            'filename': img_file,
            'fire': fire_flag,
            'smoke': smoke_flag
        })

print(f"\n✅ Done! CSV saved to {output_csv}")



# for Validation Data
import os
import csv

# 🔧 Set paths
images_dir = '/Users/shreyas_mavale/Desktop/Project/valid/images'
labels_dir = '/Users/shreyas_mavale/Desktop/Project/valid/labels'
output_csv = '/Users/shreyas_mavale/Desktop/Project/valid/labels.csv'

# 🧠 TEMP class mapping override (if you know it)
# CLASS_MAP = {0: 'fire', 1: 'smoke'}  # Comment this if using dynamic check

# Get all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Write CSV
with open(output_csv, 'w', newline='') as csvfile:
    fieldnames = ['filename', 'fire', 'smoke']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for img_file in image_files:
        basename = os.path.splitext(img_file)[0]
        label_file = basename + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        fire_flag = 0
        smoke_flag = 0

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if not parts:
                        continue
                    try:
                        class_id = int(parts[0])
                        # 👇 Change these IDs if fire/smoke are different
                        if class_id == 0:
                            fire_flag = 1
                        elif class_id == 1:
                            smoke_flag = 1
                    except ValueError:
                        print(f"[WARNING] Invalid line in {label_file}: {line.strip()}")
        else:
            print(f"[INFO] No label file found for: {img_file}")

        writer.writerow({
            'filename': img_file,
            'fire': fire_flag,
            'smoke': smoke_flag
        })

print(f"\n✅ Done! CSV saved to {output_csv}")
