#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import shutil

mds_path = '../mds/'
mds = os.listdir(mds_path)
# mds = [(i, mds[i]) for i in range(len(mds))]
mds = [(md[:2], md) for md in mds]

for (i, file) in mds:
  src = os.path.join(mds_path, file)
  dst_path = os.path.join(mds_path, 'chapter-%s' % i)
  dst = os.path.join(dst_path, 'README.md')

  os.mkdir(dst_path)
  shutil.move(src, dst)
  print(src, '-->', dst)

# print(mds)
