
def add_username_segment():
    import os
    if shline.args.shell == 'bash':
        user_prompt = ' \\u '
    elif shline.args.shell == 'zsh':
        user_prompt = ' %n '
    else:
        user_prompt = ' %s ' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    shline.append(user_prompt, Color.USERNAME_FG, bgcolor)

add_username_segment()
