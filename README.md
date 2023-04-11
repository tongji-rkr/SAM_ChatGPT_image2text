# SAM_ChatGPT_image2text
This is an easy image2txt idea using [Segment Anything](https://github.com/facebookresearch/segment-anything) and [ChatGPT Api](https://chat.openai.com). Thanks to the authors of Segment Anything and ChatGPT for their wonderful work! In addition, I would like to thank .[Prompt-Segment-Anything](https://github.com/RockeyCoss/Prompt-Segment-Anything)'s idea very much for inspiring me, and I would like to thank it for providing me with technical support by disclosing its code.

This repository is based on [MMDetection](https://github.com/open-mmlab/mmdetection) and includes some code from [H-Deformable-DETR](https://github.com/HDETR/H-Deformable-DETR) and [FocalNet-DINO](https://github.com/FocalNet/FocalNet-DINO).

**原图：**

<img src="assets/1.jpg" alt="example1" style="zoom: 150%;" />

**SAM+MMCV:**

<img src="assets/1_box.jpg" alt="example1" style="zoom: 150%;" />

**ChatGPT Api:**

```
提问:参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)：(bowl,0.41),(banana,0.57),(banana,0.31),(orange,0.55),(orange,0.52),(orange,0.51),(orange,0.51),(orange,0.44),(chair,0.76),(chair,0.71),(chair,0.52),(potted plant,0.31),(dining table,0.67),(oven,0.67),(sink,0.34),(refrigerator,0.8),(vase,0.45),想象出一个场景，并回答以下两个问题。
1. 请用一句话形容这个场景。
2. 请详细描述这个场景，并分析这段描述是否符合常理。
回答: 1. 一张餐桌上有水果和花瓶，旁边有几把椅子和一个冰箱。
2. 场景描述：一张长方形的餐桌上放着两个香蕉和四个橙子，旁边有一个花瓶。餐桌周围有三把椅子，其中一把椅子上放着一件衣服。在房间的另一侧有一个冰箱和一个水槽，旁边还有一个烤箱。房间的一角有一个盆栽。 场景符合常理，因为餐桌上放水果和花瓶是一个常见的装饰方式，同时房间内有椅子、冰箱、水槽和烤箱也是比较常见的生活用品。盆栽的存在也很常见。
```

## Installation

We test the models under `python=3.8,pytorch=1.11.0,cuda=11.3`. Other versions might be available as well.
!!! must linux

1. Clone this repository
```
git clone https://github.com/tongji_rkr/Instance-Segment-Anything
cd Instance-Segment-Anything
```

3. Install MMCV
```
pip install -U openmim
mim install "mmcv>=2.0.0"
```

4. Install MMDetection's requirements
```
pip install -r requirements.txt
```

5. Compile CUDA operators
```bash
cd projects/instance_segment_anything/ops
python setup.py build install
cd ../../..
```

## Prepare COCO Dataset

Please refer to [data preparation](https://mmdetection.readthedocs.io/en/latest/user_guides/dataset_prepare.html).

## Prepare Checkpoints

1. Install wget
```
pip install wget
```
2. SAM checkpoints
```bash
mkdir ckpt
cd ckpt
python -m wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
python -m wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth
python -m wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
cd ..
```

3. Swin-L+H-Deformable-DETR and FocalNet-L+DINO checkpoints

```bash
cd ckpt
python -m wget https://github.com/HDETR/H-Deformable-DETR/releases/download/v0.1/decay0.05_drop_path0.5_swin_large_hybrid_branch_lambda1_group6_t1500_n900_dp0_mqs_lft_deformable_detr_plus_iterative_bbox_refinement_plus_plus_two_stage_36eps.pth -o swin_l_hdetr.pth
python -m wget https://projects4jw.blob.core.windows.net/focalnet/release/detection/focalnet_large_fl4_o365_finetuned_on_coco.pth -o focalnet_l_dino.pth
cd ..

# convert checkpoints
python tools/convert_ckpt.py ckpt/swin_l_hdetr.pth ckpt/swin_l_hdetr.pth
python tools/convert_ckpt.py ckpt/focalnet_l_dino.pth ckpt/focalnet_l_dino.pth
```

## Run Evaluation

1. Visualize Segmentation Results
```bash
python tools/test.py path/to/the/config/file --show-dir path/to/the/visualization/results
```

2. get msg.txt

If you are lucky,you can get your answer. However, you can see msg.txt in your dir.

please ask by yourselves，api or not

## More Image2Text Examples

**example2**

![example2](assets/2.jpg)

![example2](assets/2_box.jpg)

```
提问: 参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)：(person,0.91),(person,0.48),(cup,0.37),(spoon,0.42),(bowl,0.74),(bowl,0.69),(bowl,0.46),(bowl,0.48),(bowl,0.3),(pizza,0.32),(dining table,0.51),(oven,0.36),(oven,0.35),(sink,0.38),想象出一个场景，并回答以下两个问题。
1. 请用一句话形容这个场景。
2. 请详细描述这个场景，并分析这段描述是否符合常理。
回答: 1. 一个人在餐桌上吃饭，旁边放着碗、勺和杯子。
2. 场景描述：一个人坐在餐桌旁，桌子上放着四个碗，其中两个装着已经吃过的饭，一个装着一块披萨，另一个则是空的。旁边放着一个勺子和一个杯子。餐桌上还摆着一个烤箱和一个水槽。 场景符合常理，因为人们通常在餐桌上用碗、勺和杯子吃饭，同时存在多个碗也是比较常见的，而烤箱和水槽也是厨房中常见的设备。
```

**example3**

![example3](assets/3.jpg)

![example3](assets/3_box.jpg)

```
提问:参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)：(person,0.9),(person,0.84),(person,0.86),(traffic light,0.74),(traffic light,0.34),(umbrella,0.52),(umbrella,0.42),(handbag,0.38),(cup,0.38),想象出一个场景，并回答以下两个问题。
1. 请用一句话形容这个场景。
2. 请详细描述这个场景，并分析这段描述是否符合常理。
回答: 1. 有几个人站在路口，其中一些人拿着雨伞和手提包。
2. 场景描述：在一个路口，有三个人站在人行道上，其中一个人拿着一个手提包，另外两个人拿着雨伞。在路口的中央，一个人正在穿越马路，此时路灯为绿灯。路灯的另一侧有一个人站在等待过马路，旁边有一个空的杯子。 场景符合常理，因为人们在路口等待过马路时通常会拿着雨伞和手提包。在路口等待过马路时也可能会有人拿着杯子喝饮料。
```

**example4**

![example4](assets/4.jpg)

![example4](assets/4_box.jpg)

```
提问:参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)：(person,0.87),(person,0.79),(person,0.63),(person,0.57),(person,0.55),(person,0.49),(person,0.47),(person,0.46),(person,0.43),(person,0.44),(person,0.4),(person,0.36),(person,0.32),(person,0.33),(person,0.32),(bicycle,0.77),(bicycle,0.38),(skateboard,0.86),(skateboard,0.35),想象出一个场景，并回答以下两个问题。
1. 请用一句话形容这个场景。
2. 请详细描述这个场景，并分析这段描述是否符合常理。
回答: 1. 许多人在公园里骑自行车和滑板。
2. 场景描述：在一个公园里，许多人骑自行车和滑板，其中一些人在花园里骑自行车，一些人在滑板公园里玩滑板。还有一些人在散步或者跑步，他们穿着运动服装。场景符合常理，因为公园是人们娱乐和锻炼的常见场所，自行车和滑板也是常见的娱乐设备。人们在公园里散步、跑步、骑自行车和滑板也是很常见的活动。
```

**example5**

![example5](assets/5.jpg)

![example5](assets/5_box.jpg)

```
提问:参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)：(bicycle,0.84),(car,0.77),(car,0.71),(car,0.72),(car,0.66),(car,0.45),(car,0.42),(car,0.36),(car,0.31),(truck,0.64),(traffic light,0.54),(traffic light,0.5),(traffic light,0.4),(traffic light,0.34),(traffic light,0.35),想象出一个场景，并回答以下两个问题。   
1. 请用一句话形容这个场景。
2. 请详细描述这个场景，并分析这段描述是否符合常理。
回答: 1. 在一个交通繁忙的路口，有汽车、卡车和自行车经过，同时有几个交通灯。
2. 场景描述：在一个交通繁忙的路口，有许多汽车和卡车在路口穿行，其中有一辆卡车停在路边，旁边有一辆自行车。此时交通灯为红灯，路口的另一侧有几辆汽车和自行车等待绿灯。路口上有几个交通灯，其中一个交通灯的灯泡坏了，只有三个灯泡亮着。 场景符合常理，因为在交通繁忙的路口，汽车、卡车和自行车的存在很常见，同时交通灯也是控制交通流量的常见设施。交通灯灯泡坏掉的情况也是常见的。
```

## Citation

**Segment Anything**

```latex
@article{kirillov2023segany,
  title={Segment Anything}, 
  author={Kirillov, Alexander and Mintun, Eric and Ravi, Nikhila and Mao, Hanzi and Rolland, Chloe and Gustafson, Laura and Xiao, Tete and Whitehead, Spencer and Berg, Alexander C. and Lo, Wan-Yen and Doll{\'a}r, Piotr and Girshick, Ross},
  journal={arXiv:2304.02643},
  year={2023}
}
```
**H-Deformable-DETR**

```latex
@article{jia2022detrs,
  title={DETRs with Hybrid Matching},
  author={Jia, Ding and Yuan, Yuhui and He, Haodi and Wu, Xiaopei and Yu, Haojun and Lin, Weihong and Sun, Lei and Zhang, Chao and Hu, Han},
  journal={arXiv preprint arXiv:2207.13080},
  year={2022}
}
```
**Swin Transformer**

```latex
@inproceedings{liu2021Swin,
  title={Swin Transformer: Hierarchical Vision Transformer using Shifted Windows},
  author={Liu, Ze and Lin, Yutong and Cao, Yue and Hu, Han and Wei, Yixuan and Zhang, Zheng and Lin, Stephen and Guo, Baining},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  year={2021}
}
```
**DINO**

```latex
@misc{zhang2022dino,
      title={DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection}, 
      author={Hao Zhang and Feng Li and Shilong Liu and Lei Zhang and Hang Su and Jun Zhu and Lionel M. Ni and Heung-Yeung Shum},
      year={2022},
      eprint={2203.03605},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
**FocalNet**

```latex
@misc{yang2022focalnet,  
  author = {Yang, Jianwei and Li, Chunyuan and Dai, Xiyang and Yuan, Lu and Gao, Jianfeng},
  title = {Focal Modulation Networks},
  publisher = {arXiv},
  year = {2022},
}
```

