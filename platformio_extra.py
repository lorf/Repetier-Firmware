Import('env')
from base64 import b64decode

host = b64decode(ARGUMENTS.get("REMOTEUPLOAD_HOST"))
port = b64decode(ARGUMENTS.get("REMOTEUPLOAD_PORT"))
proto = b64decode(ARGUMENTS.get("REMOTEUPLOAD_PROTOCOL"))

env.Replace(
    COPYFILESCMD='scp $BUILD_DIR/firmware.hex ' + host + ':/tmp/',
    REMOTEUPLOADCMD='echo "sudo /usr/sbin/service octoprint stop && avrdude -p $BOARD_MCU -c ' + proto + ' -P ' + port + ' -Uflash:w:/tmp/firmware.hex:i && rm -f /tmp/firmware.hex && sudo /usr/sbin/service octoprint start" | ssh ' + host + ' sh',
)

remoteupload = env.Alias(
    "remoteupload", "$BUILD_DIR/firmware.hex",
    [
        env.VerboseAction("$COPYFILESCMD", "Copying files to remote " + host),
        env.VerboseAction("$REMOTEUPLOADCMD", "Uploading via remote " + port + "@" + host),
    ])
AlwaysBuild(remoteupload)

#print env.Dump()
#print ARGUMENTS
