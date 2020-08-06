# Dense Video Captioning
Code for SYSU submission to [ActivityNet Challenge 2020](http://activity-net.org/challenges/2020/index.html) (Task2: Dense Video Captioning). Our approach follows a two-stage pipeline: first, we extract a set of temporal event proposals;
then we propose a multi-event captioning model to capture the event-level temporal relationships and effectively fuse
the multi-modal information. 

We won the 2nd place and the technical paper is available at [here](https://arxiv.org/abs/2006.11693v1).


# Environment
1. python 3.6.2
2. cuda 10.0, other versions may work
3. [pytorch 1.2.0](https://pytorch.org/get-started/locally/), other versions may work
4. other modules, run `pip install -r requirement.txt`

# Prerequisites
- ActivityNet video features. We use TSN features following this [repo](https://github.com/salesforce/densecap). You can follow the "Data Preparation" section to download feature files, then decompress and move them into `./data/resnet_bn`.
- Build vocabulary file. Run `python misc/build_vocab.py`.

- (Optional) You can also test our code based on C3D feature. Download C3D feature files (`sub_activitynet_v1-3.c3d_float32.hdf5`) from [here](http://activity-net.org/challenges/2016/download.html#c3d). Convert the h5 file into npy files and place them into `./data/c3d`.

# Usage
- Training
```bash
# first, train the model with cross-entropy loss 
cfg_file_path=cfgs/tsrm_cmg_hrnn.yml
python train.py --cfg_path $cfg_file_path

# Afterward, train the model with reinforcement learning on enlarged training set
cfg_file_path=cfgs/tsrm_cmg_hrnn_RL.yml
python train.py --cfg_path $cfg_file_path
```
training logs and generated captions are in this folder `./save`.

- Evaluation
```bash
# evaluation with ground-truth proposals
result_folder=tsrm_cmg_hrnn_RL
gt_tap_json=data/captiondata/val_1_for_tap.json
python eval_RL.py --eval_folder $result_folder --load_tap_json $gt_tap_json

# evaluation with learnt proposals
lnt_tap_json=data/generated_proposals/tsn_dbg_esgn_valset_num4717.json
python eval_RL.py --eval_folder $result_folder --load_tap_json $lnt_json_path
```

- Testing
```bash
python eval_RL.py --eval_folder tsrm_cmg_hrnn_RL \
 --load_tap_json data/generated_proposals/tsn_dbg_esgn_testset_num5044.json\
 --eval_caption_file data/captiondata/fake_test_anno.json
```

- baseline models
We also provide the config files of some baseline models. Please see this folder `./cfgs` for details. 


# Performance & Pretrained Models
coming soon


# Citation
If you find this repo helpful to your research, please consider citing:
```
@article{wang2020dense,
  title={Dense-Captioning Events in Videos: SYSU Submission to ActivityNet Challenge 2020},
  author={Wang, Teng and Zheng, Huicheng and Yu, Mingjing},
  journal={arXiv preprint arXiv:2006.11693},
  year={2020}
}
```

# References
- Awesome [ImageCaptioning.pytorch](https://github.com/ruotianluo/ImageCaptioning.pytorch) project.
- [Official implementation](https://github.com/XgDuan/WSDEC) of "Weakly Supervised Dense Event Captioning in Videos".