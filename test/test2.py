import asyncio

from www import orm_ref
from www.models import User


async def test():
    # 创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm_ref.create_pool(loop=loop, port=3306, user='root', password='123', db='awesome')
    # 如果使用可协程，则每一层都要使用协程
    data = await User.findAll()
    # 需要关闭数据库连接
    await orm_ref.close_pool()
    for d in data:
        print(d)


# 获取EventLoop:
loop = asyncio.get_event_loop()

# 把协程丢到EventLoop中执行
loop.run_until_complete(test())
loop.close()
