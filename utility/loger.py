import inspect
import datetime


def log_action(request):
    with open('log_file.txt', 'a') as log:
        log.write(f'{datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")} '
                  f'{inspect.stack()[1][0].f_locals["self"].__class__.__name__} '
                  f'{inspect.stack()[1][3]} from user: {request.user}\n')
