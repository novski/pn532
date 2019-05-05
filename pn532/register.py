#
# register.py contains a set of registers addresses mapping
#

PN532_DEFAULT_ADDRESS = 0x24

PN532_PREAMBLE   = 0x00
PN532_STARTCODE1 = 0x00
PN532_STARTCODE2 = 0xFF
PN532_POSTAMBLE  = 0x00

PN532_HOSTTOPN532 = 0xD4

PN532_COMMAND_SAMCONFIGURATION = 0x14
PN532_COMMAND_INLISTPASSIVETARGET = 0x4A
