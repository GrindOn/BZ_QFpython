#!/usr/bin/python3
# coding: utf-8
import random

from . import user_agents


def get_ua():
    # 随机提取一个user-agent
    return random.choice(user_agents)