# -*- coding: utf-8 -*-
# pylint: disable=

import os
import re

import jieba

def scan_azure_doc():
    base_path = 'C:/Users/greggu/repos/azure-docs.zh-cn/articles/container-registry'
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    for path, dirs, files in os.walk(base_path):
        for file in files:
            if file[-2:] == 'md':
                file_path = os.path.join(path, file)
                with open(file_path, mode='r', encoding='utf-8') as f:
                    content = '\r\n'.join(f.readlines())
                    seg_list = jieba.cut(content)
                    seg_list = [x for x in seg_list if re.match(pattern, x)]
                    print("Full Mode: " + "/ ".join(seg_list))

if __name__ == "__main__":
    scan_azure_doc()