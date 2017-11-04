Import("env")
import os

address = env.Dump("UPLOAD_PORT").replace('\'', '')

def ssh_upload(target, source, env):
    print "Attempting to upload firmware via SSH to %s" % address
    firmware = str(target[0])
    