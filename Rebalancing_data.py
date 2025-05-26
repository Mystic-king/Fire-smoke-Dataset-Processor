# For Train Data
import os
import shutil
import pandas as pd
from sklearn.utils import resample

# --- Paths ---
csv_path = '/Users/shreyas_mavale/Desktop/Project/train/labels.csv'
image_dir = '/Users/shreyas_mavale/Desktop/Project/train/images'
label_dir = '/Users/shreyas_mavale/Desktop/Project/train/labels'
output_image_dir = '/Users/shreyas_mavale/Desktop/Project/train_balanced/images'
output_label_dir = '/Users/shreyas_mavale/Desktop/Project/train_balanced/labels'

# --- Create folders ---
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# --- Load CSV ---
df = pd.read_csv(csv_path)

# --- Split into majority and minority ---
df_majority = df[df['fire'] == 1]
df_minority = df[df['fire'] == 0]

# --- L1-style balancing via downsampling majority ---
df_majority_downsampled = resample(df_majority,
                                   replace=False,
                                   n_samples=len(df_minority),
                                   random_state=42)

# --- Combine and shuffle ---
df_balanced = pd.concat([df_majority_downsampled, df_minority])
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# --- Copy images and labels to new balanced folders ---
for _, row in df_balanced.iterrows():
    filename = row['filename']
    base = os.path.splitext(filename)[0]

    # Image file
    src_img = os.path.join(image_dir, filename)
    dst_img = os.path.join(output_image_dir, filename)

    # Label file
    src_label = os.path.join(label_dir, base + '.txt')
    dst_label = os.path.join(output_label_dir, base + '.txt')

    if os.path.exists(src_img):
        shutil.copy(src_img, dst_img)

    if os.path.exists(src_label):
        shutil.copy(src_label, dst_label)

# --- Save new balanced CSV ---
balanced_csv_path = '/Users/shreyas_mavale/Desktop/Project/train_balanced/labels.csv'
df_balanced.to_csv(balanced_csv_path, index=False)

print(f"✅ Balanced dataset saved to:\n{output_image_dir}\n{output_label_dir}\nCSV: {balanced_csv_path}")




# For Test Data
import os
import shutil
import pandas as pd
from sklearn.utils import resample

# --- Paths ---
csv_path = '/Users/shreyas_mavale/Desktop/Project/test/labels.csv'
image_dir = '/Users/shreyas_mavale/Desktop/Project/test/images'
label_dir = '/Users/shreyas_mavale/Desktop/Project/test/labels'
output_image_dir = '/Users/shreyas_mavale/Desktop/Project/test_balanced/images'
output_label_dir = '/Users/shreyas_mavale/Desktop/Project/test_balanced/labels'

# --- Create folders ---
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# --- Load CSV ---
df = pd.read_csv(csv_path)

# --- Split into majority and minority ---
df_majority = df[df['fire'] == 1]
df_minority = df[df['fire'] == 0]

# --- L1-style balancing via downsampling majority ---
df_majority_downsampled = resample(df_majority,
                                   replace=False,
                                   n_samples=len(df_minority),
                                   random_state=42)

# --- Combine and shuffle ---
df_balanced = pd.concat([df_majority_downsampled, df_minority])
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# --- Copy images and labels to new balanced folders ---
for _, row in df_balanced.iterrows():
    filename = row['filename']
    base = os.path.splitext(filename)[0]

    # Image file
    src_img = os.path.join(image_dir, filename)
    dst_img = os.path.join(output_image_dir, filename)

    # Label file
    src_label = os.path.join(label_dir, base + '.txt')
    dst_label = os.path.join(output_label_dir, base + '.txt')

    if os.path.exists(src_img):
        shutil.copy(src_img, dst_img)

    if os.path.exists(src_label):
        shutil.copy(src_label, dst_label)

# --- Save new balanced CSV ---
balanced_csv_path = '/Users/shreyas_mavale/Desktop/Project/test_balanced/labels.csv'
df_balanced.to_csv(balanced_csv_path, index=False)

print(f"✅ Balanced dataset saved to:\n{output_image_dir}\n{output_label_dir}\nCSV: {balanced_csv_path}")



# For Validation Data
import os
import shutil
import pandas as pd
from sklearn.utils import resample

# --- Paths ---
csv_path = '/Users/shreyas_mavale/Desktop/Project/valid/labels.csv'
image_dir = '/Users/shreyas_mavale/Desktop/Project/valid/images'
label_dir = '/Users/shreyas_mavale/Desktop/Project/valid/labels'
output_image_dir = '/Users/shreyas_mavale/Desktop/Project/valid_balanced/images'
output_label_dir = '/Users/shreyas_mavale/Desktop/Project/valid_balanced/labels'

# --- Create folders ---
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# --- Load CSV ---
df = pd.read_csv(csv_path)

# --- Split into majority and minority ---
df_majority = df[df['fire'] == 1]
df_minority = df[df['fire'] == 0]

# --- L1-style balancing via downsampling majority ---
df_majority_downsampled = resample(df_majority,
                                   replace=False,
                                   n_samples=len(df_minority),
                                   random_state=42)

# --- Combine and shuffle ---
df_balanced = pd.concat([df_majority_downsampled, df_minority])
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# --- Copy images and labels to new balanced folders ---
for _, row in df_balanced.iterrows():
    filename = row['filename']
    base = os.path.splitext(filename)[0]

    # Image file
    src_img = os.path.join(image_dir, filename)
    dst_img = os.path.join(output_image_dir, filename)

    # Label file
    src_label = os.path.join(label_dir, base + '.txt')
    dst_label = os.path.join(output_label_dir, base + '.txt')

    if os.path.exists(src_img):
        shutil.copy(src_img, dst_img)

    if os.path.exists(src_label):
        shutil.copy(src_label, dst_label)

# --- Save new balanced CSV ---
balanced_csv_path = '/Users/shreyas_mavale/Desktop/Project/valid_balanced/labels.csv'
df_balanced.to_csv(balanced_csv_path, index=False)

print(f"✅ Balanced dataset saved to:\n{output_image_dir}\n{output_label_dir}\nCSV: {balanced_csv_path}")
