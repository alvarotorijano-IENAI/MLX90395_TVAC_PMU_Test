import os
Import("env")

def after_upload(source, target, env):
    os.system("platformio device monitor | tee -a log.txt")

env.AddPostAction("upload", after_upload)