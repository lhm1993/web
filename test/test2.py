from www.models import User
import www.orm_ref
import asyncio


def get():
    data = User.findAll()
    for d in data:
        print(d)

if __name__ == '__main__':
    get()