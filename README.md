# markdown-image-upload.workflow
Alfred 3, shortcut key upload picture to GitHub and generate markdown picture grammar to clipboard

## 安装

1. 双击安装 [markdown-image-upload.workflow](https://raw.githubusercontent.com/MrJiao/markdown-image-upload-workflow/master/markdown-image-upload.alfredworkflow)

2. 下载python依赖

   ```bash
   sudo 
   python -m pip install --upgrade pip
   pip install multiprocessing
   pip install Pillow
   pip install requests
   ```

3. 进入workflows

   ![img](https://raw.githubusercontent.com/MrJiao/markdown/master/img/1566444954936.jpg)

4. 修改配置

   ![img](https://raw.githubusercontent.com/MrJiao/markdown/master/img/1566444996605.jpg)

## 使用
1. 把图片剪切到粘贴板中
2. 按commond + shift + p 就可以上传图片，并获得markdown语法图片地址到粘贴板
3. 直接commond + v 粘贴就可以了
