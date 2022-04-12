## baija-imgpool-tools
## 简介: 

- 百家号图床api上传程序
- 通过协程并发批量上传图片
## 注意事项:

- 合理使用, 请勿滥用, 如有后果概不负责

#### 环境需求:

python >= 3.7

#### 第三方库:

aiohttp

#### 使用方法:

    python ./imgpool_cil.py 命令 图片路径

    -h: 获得帮助
    -d: 输入为文件夹
    -s: 输入为单个图片
    输出为命令行打印和程序文件夹下的output.txt
