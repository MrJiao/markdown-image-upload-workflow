# -*- coding: utf-8 -*-
import base64
import os
import time
from PIL import Image
from hashlib import sha1
import requests

params = {"token": "",  # github 第三方客户端授权token
          # 用户
          "user": "",
          # 项目名称
          "project": "",
          # 文件路径
          "path": "img",
          # 提交备注
          "message": "img commit",
          # 缩小比例, 2为缩小一半
          "scale": 1.7
          }


def saveImageFromClipboard(file_folder_path, file_name):
    file_path = file_folder_path + '/' + file_name
    data = os.system('/usr/local/bin/pngpaste ' + file_path)
    if data != 0:
        raise Exception("从粘贴板获取图片失败")
    return file_path


def readFile2Base64(file_path):
    with open(file_path, 'rb') as f:
        return str(base64.b64encode(f.read()))


def shrink(file_path):
    im = Image.open(file_path)
    w, h = im.size
    im.thumbnail((w // params['scale'], h // params['scale']))
    return im.save(file_path, 'jpeg')


def getSha1(file_path):
    sha1Obj = sha1()
    with open(file_path, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()


def sendImage(params, content, sha, file_name):
    headers = {"content-type": "application/json", "Authorization": "token " + params['token']}
    r1 = requests.put(
        "https://api.github.com/repos/" + params['user'] + "/" + params['project'] + "/contents/" + params[
            'path'] + "/" + file_name,
        json={
            "message": params['message'],
            "content": content,
            "sha": sha
        }, headers=headers)


def getFileName():
    t = time.time()
    return str(int(round(t * 1000))) + '.jpg'


def printImagePath(name):
    print "![img](https://raw.githubusercontent.com/" + params['user'] + "/" + params['project'] + "/master/" + params[
        'path'] + "/" + name + ")"


save_dir = os.path.expandvars('$HOME').rstrip()
name = getFileName()
try:
    file = saveImageFromClipboard(save_dir, name)
    shrink(file)
    base64_str = readFile2Base64(file)
    sha1Obj = getSha1(file)
    sendImage(params, base64_str, sha1Obj, name)
    printImagePath(name)
except Exception as e:
    print("执行错误"),
    print(e),
finally:
    path = save_dir + '/' + name
    if os.path.exists(path):
        os.remove(path)
