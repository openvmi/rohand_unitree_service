import time
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from rohand_unitree_service.core import ROHandCtrl, ROHandCtrlMode

def subscriber_hander(msg: ROHandCtrl):
    print(f"recv:{msg.serialize()}")

def main():
    ChannelFactoryInitialize(0)
    subscriber = ChannelSubscriber("rt/mock_rohand/ctrl", ROHandCtrl)
    subscriber.Init(subscriber_hander, 10)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    print("-->start hello_dds_subscriber")
    main()