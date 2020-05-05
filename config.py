""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'meshio.net'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'linville5'
WIFI_PASS = 'thr3adtr4il'

# for EU868
#LORA_FREQUENCY = 868100000
#LORA_GW_DR = "SF7BW125" # DR_5
#LORA_NODE_DR = 5

# for US915
LORA_FREQUENCY = 904300000
LORA_GW_DR = "SF10BW125"            # Gateway DataRate DR_3
LORA_NODE_DR = 2                    # Node DataRate
