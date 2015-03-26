import os

def add_ssh_segment():

    if os.getenv('SSH_CLIENT'):
        shline.append(' %s ' % shline.network, Color.SSH_FG, Color.SSH_BG)

add_ssh_segment()
