#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os

f = os.popen(r"ls /Users/jigang.duan/workspace/blog/laughing-octo-train/mysql/mysql-actions-36/html | grep .html", "r")
html_dirs_str = f.read()
f.close()

html_dirs = html_dirs_str.split('\n')
html_dirs = [x.split('.html')[0] for x in html_dirs if x != '']
html_dirs = [(i, html_dirs[i]) for i in range(len(html_dirs))]

seq = ["\r\n* [%s](books/mysql-actions-36/chapter-%d/README.md)" % (item, i+1) for (i, item) in html_dirs]

fo = open("../SUMMARY.md", "a")
fo.writelines( seq )
fo.close()
