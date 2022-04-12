import imgpool_async
import os
import asyncio
import platform
if __name__ == '__main__':
    if platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        commnd=os.sys.argv[1]
    except:
        print("-h: 获得帮助")
        print("-d: 输入为文件夹")
        print("-s: 输入为单个图片")
        exit()
    if commnd=="-h":
        print("-h: 获得帮助")
        print("-d: 输入为文件夹")
        print("-s: 输入为单个图片")
    elif commnd=="-s":
        path=os.sys.argv[2]
        res=asyncio.run(imgpool_async.async_upload(path))
        out=open("output.txt","a")
        out.write("{}  {}\n".format(res[0],res[1]))
        print("{}  {}".format(res[0],res[1]))
    elif commnd=="-d":
        path=os.sys.argv[2]
        res=asyncio.run(imgpool_async.async_uploader_list(imgpool_async.get_filelist(path)))
        out=open("output.txt","a")
        for iter in res:
            out.write("{}  {}\n".format(iter[0],iter[1]))
            print("{}  {}".format(iter[0],iter[1]))
    else:
        print("-h: 获得帮助")
        print("-d: 输入为文件夹")
        print("-s: 输入为单个图片")