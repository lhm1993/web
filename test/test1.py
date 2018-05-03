from www import orm_ref
from www.models import User
import asyncio
import sys

async def test():

    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm_ref.create_pool(loop=loop, port=3306, user='root', password='123', db='awesome')

    #没有设置默认值的一个都不能少
    u = User(name='dflhuang23', email='dflhuang@qq.com3', passwd='012323', image='about:blank2', id='3372')

    await u.save()
    data = User.findAll()
    with open("./tt", "w") as fd:
        fd.write(str(data))


# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)