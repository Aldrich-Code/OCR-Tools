# OCR-Tools
一款图片转文字实用工具。
# 如何使用
### 首先
你需要安装以下库：
  ·easyocr
  ·pyperclip
  ·windnd
 剩下的都是python自带的了
 ### 其次
 你需要下载EasyOCR的语言模型文件，请依次下载原型模型<https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip>，中文模型<https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/chinese_sim.zip>，英文模型<https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/english_g2.zip>，下载他们并解压至“C://Users//你的用户名//.EasyOCR”文件夹中。
 ### 最后
 双击ocr.py，将图片文件拖入窗口，按提示即可。
 
 # 提示
 1.如果您的GPU支持CUDA，处理的速度会更快哦！
 2.文件名不能包含中文，否则会报错。
