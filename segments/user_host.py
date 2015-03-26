def add_user_host_segment():
    import os
    import socket

    if shline.args.shell == 'bash':
        user = '\\u'
        host = '\\h'
    elif shline.args.shell == 'zsh':
        user = '%n'
        host = '%m'
    else:
        user = '%s' % os.getenv('USER')
        host = '%s' % socket.gethostname().split('.')[0]

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    shline.append(' %s@%s ' % (user, host), Color.USERNAME_FG, bgcolor)

add_user_host_segment()

