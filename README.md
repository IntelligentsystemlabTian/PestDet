# PestDet
## Describe
Our framework needs to run in the PyTorch framework and utilizes Nvidia GPUs. The dataset employed is our previously established GrainPest dataset.
## How to use
### requirements
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
1. cd PestDet
2. pip install requirements.txt
### Train
1.Modify the dataset path in PestDet/data/data.yaml.

2.Enter commands (python train) in the root directory of the project.

## Dataset
We provide a portion of pest data for training and testing. The model training utilizes a dataset in VOC format, which can be accessed at the following link: [https://github.com/IntelligentsystemlabTian/PestDataset](https://github.com/IntelligentsystemlabTian/PestDataset).
