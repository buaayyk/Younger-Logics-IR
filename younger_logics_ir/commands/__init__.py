#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2024-11-27 15:51:12
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2024-12-11 14:59:33
# Copyright (c) 2024 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


from younger.commons.logging import set_logger, use_logger

from younger_logics_ir import __thename__


def equip_logger(logging_filepath):
    set_logger(__thename__, mode='both', level='INFO', logging_filepath=logging_filepath)
    use_logger(__thename__)

