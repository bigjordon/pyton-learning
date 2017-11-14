import functools
import inspect

def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        print(func_args)
        if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


@check_is_admin
def get_food(username, food='chocolate'):
    return "{0} get food: {1}".format(username, food)


def main():
    print(get_food('admin'))

if __name__ == '__main__':
    main()
