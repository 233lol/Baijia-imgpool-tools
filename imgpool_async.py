import asyncio
import aiohttp
import json
import os
import time
import platform
async def async_upload(filepath):
    filename = os.path.basename(filepath)
    default_hdrs = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    cookies = {}
    url = 'https://rsbjh.baidu.com/builderinner/api/content/file/upload?is_waterlog=0'
    data = aiohttp.FormData()
    data.add_field('media',
               open(filepath, 'rb'),
               filename=filename,
               content_type='image')
    j = await async_request_retry(
        url,
        data=data,
        headers=default_hdrs,
        cookies=cookies
    )
    return filename,j['ret']['org_url']


async def async_request_retry(url, **kwargs):
    async with aiohttp.request("POST",url, **kwargs) as requ:
        result = await requ.json()
        return result

def get_filelist(filedir):
    filenames=os.listdir(filedir)
    if filedir[-1]!='/':
        filedir+='/'
    filepaths=[]
    for filename in filenames:
        if filename.lower().endswith(("jpg","png","jpeg","bmp","gif")):
            if os.path.getsize(filedir+filename)<=20000000:
                filepaths.append(filedir+filename)
            else:
                print("{}:size too large".format(filedir+filename))
    return filepaths

async def async_uploader_list(filelist):
    tasks = []
    for filepath in filelist:
        tasks.append(asyncio.ensure_future(async_upload(filepath)))
    result=await asyncio.gather(*tasks)
    return result
if __name__ == '__main__':
    print(get_filelist("./"))
    s=time.time()
    if platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    res=asyncio.run(async_uploader_list(get_filelist("./")))
    e=time.time()
    print(res)
    print(e-s)