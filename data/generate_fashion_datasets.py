import os
import shutil
from PIL import Image

IMG_EXTENSIONS = [
'.jpg', '.JPG', '.jpeg', '.JPEG',
'.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

def is_image_file(filename):
	return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def make_dataset(dir):
	images = []
	assert os.path.isdir(dir), '%s is not a valid directory' % dir
	new_root = './fashion'
	if not os.path.exists(new_root):
		os.mkdir(new_root)

	train_root = './fashion/train'
	if not os.path.exists(train_root):
		os.mkdir(train_root)

	test_root = './fashion/test'
	if not os.path.exists(test_root):
		os.mkdir(test_root)

	train_images = []
	train_f = open('./fashion/train.lst', 'r')
	for lines in train_f:
		lines = lines.strip()
		if lines.endswith('.jpg'):
			train_images.append(lines)

	test_images = []
	test_f = open('./fashion/test.lst', 'r')
	for lines in test_f:
		lines = lines.strip()
		if lines.endswith('.jpg'):
			test_images.append(lines)

	print(train_images, test_images)
	

	for root, _, fnames in sorted(os.walk(dir)):
		for fname in fnames:
			# print(fname)
			if is_image_file(fname):
				path = os.path.join(root, fname)
				# print(path)
				path_names = path.split('/') 
				
				del path_names[2]
				del path_names[0]
				# print(path_names)
				# path_names[2] = path_names[2].replace('_', '')
				path_names[3] = path_names[3].replace('_', '')
				path_names[4] = path_names[4].split('_')[0] + "_" + "".join(path_names[4].split('_')[1:])
				path_names = "".join(path_names)
				# print(root)
				# new_path = os.path.join(root, path_names)
				# print(path_names)
				img = Image.open(path)
				imgcrop = img.crop((40, 0, 216, 256))
				if path_names in train_images:
					imgcrop.save(os.path.join(train_root, path_names))
				elif path_names in test_images:
					imgcrop.save(os.path.join(test_root, path_names))


os.chdir('/content/Dual-task-Pose-Transformer-Network/dataset')
make_dataset('./fashion')