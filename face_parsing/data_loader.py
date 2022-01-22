import torch
import ipdb
import torchvision.datasets as dsets
from torchvision import transforms
from PIL import Image
import os

class CelebAMaskHQ():
    def __init__(self, img_path, label_path, transform_img, transform_label, mode, train_split_size, suffix='jpg'):
        self.img_path = img_path
        self.label_path = label_path
        self.transform_img = transform_img
        self.transform_label = transform_label
        self.train_dataset = []
        self.test_dataset = []
        self.mode = mode
        self.train_split_size = train_split_size
        self.img_suffix = suffix
        self.preprocess()
        
        if mode == True:
            self.num_images = len(self.train_dataset)
        else:
            self.num_images = len(self.test_dataset)

    def preprocess(self):
        
        for i in range(len([name for name in os.listdir(self.img_path) if os.path.isfile(os.path.join(self.img_path, name))])):
            # img_path = os.path.join(self.img_path, str(i)+'.jpg')
            img_path = os.path.join(self.img_path, str(i)+f'.{self.img_suffix}')

            label_path = os.path.join(self.label_path, str(i)+'.png')
            # print (img_path, label_path) 
            if self.mode == True:
                self.train_dataset.append([img_path, label_path])
                # print(f'Training dataset size: {len(self.train_dataset)}')
            else:
                self.test_dataset.append([img_path, label_path])
                # print(f'Eval dataset size: {len(self.test_dataset)}')

        # ipdb.set_trace()
        if self.train_split_size != -1:
            self.train_dataset = self.train_dataset[:self.train_split_size]
            
        print('Finished preprocessing the CelebA dataset...')

    def __getitem__(self, index):
        
        dataset = self.train_dataset if self.mode == True else self.test_dataset
        img_path, label_path = dataset[index]
        image = Image.open(img_path)
        label = Image.open(label_path)
        # ipdb.set_trace()
        return self.transform_img(image), self.transform_label(label)

    def __len__(self):
        """Return the number of images."""
        return self.num_images

class Data_Loader():
    def __init__(self, img_path, label_path, image_size, batch_size, mode, train_split_size=-1, suffix='.jpg'):
        self.img_path = img_path
        self.label_path = label_path
        self.imsize = image_size
        self.batch = batch_size
        self.mode = mode
        self.img_suffix = suffix
        self.train_split_size = train_split_size


    def transform_img(self, resize, totensor, normalize, centercrop):
        options = []
        if centercrop:
            options.append(transforms.CenterCrop(160))
        if resize:
            options.append(transforms.Resize((self.imsize,self.imsize)))
        if totensor:
            options.append(transforms.ToTensor())
        if normalize:
            options.append(transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)))
        transform = transforms.Compose(options)
        return transform

    def transform_label(self, resize, totensor, normalize, centercrop):
        options = []
        if centercrop:
            options.append(transforms.CenterCrop(160))
        if resize:
            options.append(transforms.Resize((self.imsize,self.imsize)))
        if totensor:
            options.append(transforms.ToTensor())
        if normalize:
            options.append(transforms.Normalize((0, 0, 0), (0, 0, 0)))
        transform = transforms.Compose(options)
        return transform

    def loader(self):
        transform_img = self.transform_img(True, True, True, False) 
        transform_label = self.transform_label(True, True, False, False)  
        dataset = CelebAMaskHQ(self.img_path, self.label_path, transform_img, transform_label, self.mode, self.train_split_size, self.img_suffix)

        loader = torch.utils.data.DataLoader(dataset=dataset,
                                             batch_size=self.batch,
                                             shuffle=True,
                                            #  num_workers=0,
                                             num_workers=4,
                                             drop_last=False)
        return loader

