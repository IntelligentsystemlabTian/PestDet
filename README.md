# PestDet
## Describe
Our framework needs to run in the PyTorch framework and utilizes Nvidia GPUs. The dataset employed is our previously established GrainPest dataset.
## How to use
### Requirements
Training PestDet requires the following libraries:
<details>
  <summary>Requirements</summary>
  matplotlib>=3.2.2  
  
  numpy>=1.18.5  
  opencv-python>=4.1.2  
  Pillow>=7.1.2  
  PyYAML>=5.3.1  
  requests>=2.23.0  
  scipy>=1.4.1  
  torch>=1.7.0  
  torchvision>=0.8.1  
  tqdm>=4.41.0 .  
</details>
To install the requirements, enter the root directory of PestDet and execute the command "pip install -r requirements.txt".

### Train
Modify the dataset path in "PestDet/data/data.yaml", then run the following command to start training:  
<details>
  <summary>Train PestDet</summary>
  python train.py --data data/data.yaml --cfg models/PestDet.yaml
</details>

### Validation
After training is complete, run the following code for verification:
<details>
  <summary>Val PestDet</summary>
  python val.py --data data/data.yaml --weights "The path where the weight is located"
</details>

## Dataset
We provide post-processed data for training and testing. The dataset is initially in VOC format and needs to be converted to YOLO format before use. Our dataset can be accessed via the following link: [PestDataset](https://github.com/IntelligentsystemlabTian/PestDataset).

Please make sure dataset with the following folder structure：
<details>
  <summary>Folde Structure</summary>
  │PestDataset/  
  
  ├──images/  
  │  ├── train  
  │  │   ├── 1.jpg  
  │  │   ├── ......  
  │  ├── val  
  │  │   ├── 2.jpg  
  │  │   ├── ......  
  │  ├── test  
  │  │   ├── 3.jpg  
  │  │   ├── ......  
  ├──labels/  
  │  ├── train  
  │  │   ├── 1.txt  
  │  │   ├── ......  
  │  ├── val  
  │  │   ├── 2.txt  
  │  │   ├── ......  
  │  ├── test  
  │  │   ├── 3.txt  
  │  │   ├── ......  
</details>  
