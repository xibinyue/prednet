#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author:  xibin.yue   
date:  2016/11/25
descrption: 
"""
import os

DATA_PATH = '/home/meteo/xibin.yue/nowcast_dl/ext_data'
IMAGE_PATH = os.path.join(DATA_PATH, 'denoise_dl_newtrain')
TRAIN_FILE_PATH = os.path.join(DATA_PATH, 'train')
VALID_FILE_PATH = os.path.join(DATA_PATH, 'validation')
CROP_SIZE = 384
TRAIN_RATIO = 0.7
SEQ_LENGTH = 10
