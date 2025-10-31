import time
import argparse
from unitree_sdk2py.core.channel import ChannelPublisher, ChannelFactoryInitialize
from rohand_unitree_service.core import ROHandCtrl, ROHandCtrlMode


def _make_parser():
    parser = argparse.ArgumentParser("ROHand service for unitree")
    parser.add_argument(
        "--nt",
        type=str,
        default=None,
        help="network interface"
    )
    parser.add_argument(
        "--disable_r_hand",
        action="store_true",
        help="Right ROHand is installed"
    )
    parser.add_argument(
        "--disable_l_hand",
        action="store_true",
        help="Left ROHand is installed"
    )
    return parser

def main():
    args = _make_parser().parse_args()
    l_hand_ctrl_topic = 'rt/rohand/l/ctrl'
    r_hand_ctrl_topic = 'rt/rohand/r/ctrl'
    r_hand_installed = not args.disable_r_hand
    l_hand_installed = not args.disable_l_hand
    ChannelFactoryInitialize(0)
    l_publisher = ChannelPublisher(l_hand_ctrl_topic, ROHandCtrl)
    l_publisher.Init()
    r_publisher = ChannelPublisher(r_hand_ctrl_topic, ROHandCtrl)
    r_publisher.Init()

    while True:
        if r_hand_installed is True:
            for i in range(6):
                print(f"write: r_hand finger_Id:{i}, position: 65535")
                msg = ROHandCtrl(i, 65535, 255, ROHandCtrlMode.HAND_MODE_POSITION)
                r_publisher.Write(msg)
                time.sleep(1)

                print(f"write: r_hand finger_Id:{i}, position: 0")
                msg = ROHandCtrl(i, 0, 255, ROHandCtrlMode.HAND_MODE_POSITION)
                r_publisher.Write(msg)
                time.sleep(1)
        
        if l_hand_installed is True:
            for i in range(6):
                print(f"write: l_hand finger_Id:{i}, position:65535")
                msg = ROHandCtrl(i, 65535, 255, ROHandCtrlMode.HAND_MODE_POSITION)
                l_publisher.Write(msg)
                time.sleep(1)

                print(f"write: l_hand finger_Id:{i}, position:0")
                msg = ROHandCtrl(i, 0, 255, ROHandCtrlMode.HAND_MODE_POSITION)
                l_publisher.Write(msg)
                time.sleep(1)
        
        time.sleep(3)
        

if __name__ == "__main__":
    main()
