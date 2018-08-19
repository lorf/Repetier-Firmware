Import('env')
from base64 import b64decode

host = b64decode(ARGUMENTS.get("REMOTEUPLOAD_HOST"))
port = b64decode(ARGUMENTS.get("REMOTEUPLOAD_PORT"))

env.Replace(
    COPYFILESCMD='scp $BUILD_DIR/firmware.bin ' + host + ':/tmp/',
    REMOTEUPLOADCMD='echo "sudo systemctl stop octoprint && sudo sh -c \\"stty 1200 </dev/' + port + '\\" && sudo bossac --info --port ' + port + ' --erase --write --verify --reset -U false --boot /tmp/firmware.bin && rm -f /tmp/firmware.bin && sudo systemctl start octoprint" | ssh ' + host + ' sh',
)

remoteupload = env.Alias(
    "remoteupload", "$BUILD_DIR/firmware.bin",
    [
        env.VerboseAction("$COPYFILESCMD", "Copying files to remote " + host),
        env.VerboseAction("$REMOTEUPLOADCMD", "Uploading via remote " + port + "@" + host),
    ])
AlwaysBuild(remoteupload)

#print env.Dump()
#print ARGUMENTS
