try:
    import configparser
except ImportError:
    import ConfigParser as configparser

Import('env')
from base64 import b64decode

config = configparser.ConfigParser()
config.read("platformio.ini")
host = config.get("env:anet-v1.0", "remoteupload_host")
port = config.get("env:anet-v1.0", "remoteupload_port")
proto = config.get("env:anet-v1.0", "remoteupload_protocol")

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
