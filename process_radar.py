#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author:  xibin.yue   
date:  2016/11/25
descrption: 
"""
import os
import sys
import datetime
import cv2
import numpy as np
from config import *


def _read_data(data_path):
    _station_list = os.listdir(data_path)
    _sample_path_list = []
    for _station in _station_list:
        print _station
        _station_path = os.path.join(data_path, _station)
        _file_list = os.listdir(_station_path)
        _file_list.sort()
        _path_list_temp = []
        _file_times = map(lambda x: datetime.datetime.strptime(x[:-4], '%Y%m%d%H%M'), _file_list)
        for _i_file in range(len(_file_list)):
            _file = _file_list[_i_file]
            print _file
            _file_path = os.path.join(_station_path, _file)
            if len(_path_list_temp) <= 1:
                _path_list_temp.append(_file_path)
            elif len(_path_list_temp) < 20:
                print (_file_times[_i_file] - _file_times[_i_file - 1]).total_seconds()
                if (_file_times[_i_file] - _file_times[_i_file - 1]).total_seconds() == 360:
                    _path_list_temp.append(_file_path)
                else:
                    _path_list_temp = []

            if len(_path_list_temp) == 20:
                _sample_path_list.append(_path_list_temp)
                _path_list_temp = []

    _data_477 = []
    _data_509 = []
    for _path_list in _sample_path_list:
        pics = []
        for _file_path in _path_list:
            pics.append(cv2.imread(_file_path, 0))
        if pics[0].shape[0] == 477:
            _data_477.append(np.array(pics))
        elif pics[0].shape[0] == 509:
            _data_509.append(np.array(pics))
        else:
            raise
            print 'shape should be 477 or 509,', pics[0].shape[0], 'found.'
        print len(_data_477)
        print len(_data_509)
    _data_477 = np.array(_data_477)
    _data_509 = np.array(_data_509)
    crop_s_477 = (477 - CROP_SIZE) / 2
    crop_s_509 = (509 - CROP_SIZE) / 2
    print 'shape:', _data_477.shape
    print 'shape:', _data_509.shape
    _data_477_crop = _data_477[:, :, crop_s_477: crop_s_477 + CROP_SIZE, crop_s_477: crop_s_477 + CROP_SIZE]
    _data_509_crop = _data_509[:, :, crop_s_509: crop_s_509 + CROP_SIZE, crop_s_509: crop_s_509 + CROP_SIZE]
    del _data_477
    del _data_509
    _data_crop = np.concatenate([_data_477_crop, _data_509_crop], axis=0)

    print _data_crop.shape
    del _data_477_crop
    del _data_509_crop
    index = range(_data_crop.shape[0])
    np.random.shuffle(index)
    _train_data = _data_crop[index[:int(len(index) * TRAIN_RATIO)]]
    _test_data = _data_crop[index[int(len(index) * TRAIN_RATIO):]]
    print _train_data.shape
    print _test_data.shape
    return _train_data, _test_data
