def add_hostname_segment():
    if shline.args.shell == 'bash':
        host_prompt = ' \\h '
    elif shline.args.shell == 'zsh':
        host_prompt = ' %m '
    else:
        import socket
        host_prompt = ' %s ' % socket.gethostname().split('.')[0]

    shline.append(host_prompt, Color.HOSTNAME_FG, Color.HOSTNAME_BG)


add_hostname_segment()
