import numpy as np

import os
from os.path import join

from torch.utils import data

from torchvision import transforms, datasets

from PIL import Image

# class CELEBA(data.Dataset):
#     """
#     use 100 samples for testing

#     Args:
#         root (string): Root directory of dataset where directory
#             ``cifar-10-batches-py`` exists.
#         train (bool, optional): If True, creates dataset from training set, otherwise
#             creates from test set.
#         transform (callable, optional): A function/transform that  takes in an PIL image
#             and returns a transformed version. E.g, ``transforms.RandomCrop``
#         target_transform (callable, optional): A function/transform that takes in the
#             target and transforms it.
#         download (bool, optional): If true, downloads the dataset from the internet and
#             puts it in root directory. If dataset is already downloaded, it is not
#             downloaded again.
#     """


#     def __init__(self, root, train=True, transform=None, Ntest=100):
#         self.root = os.path.expanduser(root)
#         self.train = train  # training set or test set
#         self.filename='celebA'
#         self.transform=transform

#         # now load the picked numpy arrays
#         if self.train:
#             self.train_data = np.load(join(self.root, self.filename, 'xTrain.npy'), mmap_mode='r')[Ntest:]
#             self.train_data = self.train_data.transpose((0, 2, 3, 1))  # convert to HWC
#             train_labels = np.load(join(self.root, self.filename, 'yTrain.npy'))[Ntest:]
#             self.train_labels = train_labels.astype(int)/2
#             print np.shape(self.train_labels), np.shape(self.train_data)
#             print np.unique(self.train_labels)

#         else:
#             self.test_data = np.load(join(self.root, self.filename, 'xTrain.npy'), mmap_mode='r')[:Ntest]
#             self.test_data = self.test_data.transpose((0, 2, 3, 1))  # convert to HWC
#             test_labels = np.load(join(self.root, self.filename, 'yTrain.npy'))[:Ntest]
#             self.test_labels = test_labels.astype(int)/2


#     def __getitem__(self, index):
#         """
#         Args:
#             index (int): Index
#         Returns:
#             tuple: (image, target) where target is index of the target class.
#         """

#         if self.train:
#             img, target = self.train_data[index], self.train_labels[index]
#         else:
#             img, target = self.test_data[index], self.test_labels[index]
            

#         # doing this so that it is consistent with all other datasets
#         # to return a PIL Image
#         img = Image.fromarray(img)

#         if self.transform is not None:
#             img = self.transform(img)

#         target = target.astype(int)


#         return img, target

#     def __len__(self):
#         if self.train:
#             return len(self.train_data)
#         else:
#             return len(self.test_data)

#     def _check_dir_exist(self):
#         inDir=join(self.root, self.filename)
#         assert os.path.isdir(inDir)
#         assert os.path.exists(join(inDir, 'xTrain.npy'))
#         assert os.path.exists(join(inDir, 'yTrain.npy'))


class CELEBA(data.Dataset):
    """
    Args:
        root (string): Root directory of dataset where directory
            ``celebA`` exists.
        train (bool, optional): If True, creates dataset from training set, otherwise
            creates from test set.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        download (bool, optional): If true, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
    """


    def __init__(self, root, train=True, transform=None, label='Smiling', Ntest=100):
        attributes = ['5_o_Clock_Shadow', 'Arched_Eyebrows', 'Attractive', 'Bags_Under_Eyes', 'Bald', 'Bangs', 'Big_Lips', 'Big_Nose', 'Black_Hair', 'Blond_Hair', 'Blurry', 'Brown_Hair', 'Bushy_Eyebrows', 'Chubby', 'Double_Chin', 'Eyeglasses', 'Goatee', 'Gray_Hair', 'Heavy_Makeup', 'High_Cheekbones', 'Male', 'Mouth_Slightly_Open', 'Mustache', 'Narrow_Eyes', 'No_Beard', 'Oval_Face', 'Pale_Skin', 'Pointy_Nose', 'Receding_Hairline', 'Rosy_Cheeks', 'Sideburns', 'Smiling', 'Straight_Hair', 'Wavy_Hair', 'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Young']

        self.root = os.path.expanduser(root)
        self.train = train  # training set or test set
        self.filename='celebA'
        self.transform=transform
        self.idx = attributes.index(label)
        print(self.idx)

        # now load the picked numpy arrays
        if self.train:
            self.train_data = np.load(join(self.root, self.filename, 'xTrain.npy'), mmap_mode='r')[Ntest:]
            self.train_data = self.train_data.transpose((0, 2, 3, 1))  # convert to HWC
            train_labels = np.load(join(self.root, self.filename, 'yAllTrain.npy'))[Ntest:, self.idx]
            self.train_labels = (train_labels.astype(int)+1) /2
            print(np.shape(self.train_labels), np.shape(self.train_data))
            print(np.unique(self.train_labels))

        else:
            self.test_data = np.load(join(self.root, self.filename, 'xTrain.npy'), mmap_mode='r')[:Ntest]
            self.test_data = self.test_data.transpose((0, 2, 3, 1))  # convert to HWC
            test_labels = np.load(join(self.root, self.filename, 'yAllTrain.npy'))[:Ntest, self.idx]
            self.test_labels = (test_labels.astype(int)+1) /2


    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is index of the target class.
        """

        if self.train:
            img, target = self.train_data[index], self.train_labels[index]
        else:
            img, target = self.test_data[index], self.test_labels[index]
            

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        target = target.astype(int)


        return img, target

    def __len__(self):
        if self.train:
            return len(self.train_data)
        else:
            return len(self.test_data)

    def _check_dir_exist(self):
        inDir=join(self.root, self.filename)
        assert os.path.isdir(inDir)
        assert os.path.exists(join(inDir, 'xTrain.npy'))
        assert os.path.exists(join(inDir, 'yAllTrain.npy'))


