import time
from unitree_sdk2py.core.channel import ChannelPublisher, ChannelFactoryInitialize
from rohand_unitree_service.core import ROHandCtrl, ROHandCtrlMode

def main():
    ChannelFactoryInitialize(0)
    publisher = ChannelPublisher("rt/mock_rohand/ctrl", ROHandCtrl)
    publisher.Init()
    target_value = 0x00
    while True:
        msg = ROHandCtrl(0x01, target_value, 0xff, ROHandCtrlMode.HAND_MODE_POSITION)
        publisher.Write(msg)
        time.sleep(5)
        target_value = (target_value + 1) % 65535


if __name__ == "__main__":
    print("--> start hello_dds_publisher")
    main()