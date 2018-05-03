from www.models import User


def get():
    data = User.findAll()
    while data.next():
        yield data
if __name__ == '__main__':
    get()
    get()