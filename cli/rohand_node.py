import argparse
import time
from rohand_unitree_service import ROHandService
from unitree_sdk2py.core.channel import ChannelFactoryInitialize


def _make_parser():
    parser = argparse.ArgumentParser("ROHand service for unitree")
    parser.add_argument(
        "--nt",
        type=str,
        default=None,
        help="network interface"
    )
    parser.add_argument(
        "--r_hand_id",
        type=int,
        default=0x03,
        help="ROHand ID for right"
    )
    parser.add_argument(
        "--l_hand_id",
        type=int,
        default=0x02,
        help="ROHand id for left"
    )
    parser.add_argument(
        "--port",
        type=str,
        default="/dev/ttyUSB0",
        help="Port for 485 communication"
    )
    parser.add_argument(
        "--disable_r_hand",
        action="store_true",
        help="Right ROHand is not installed"
    )
    parser.add_argument(
        "--disable_l_hand",
        action="store_true",
        help="Left ROHand is not installed"
    )
    return parser

if __name__ == "__main__":
    args = _make_parser().parse_args()
    print(f"parameters:\n{vars(args)}")
    l_hand_installed = not args.disable_l_hand
    r_hand_installed = not args.disable_r_hand
    if args.nt is not None:
        ChannelFactoryInitialize(0, args.nt)
    else:
        ChannelFactoryInitialize(0)
    rohand_service = ROHandService(
        r_hand_id=args.r_hand_id,
        l_hand_id=args.l_hand_id,
        port = args.port,
        l_hand_installed = l_hand_installed,
        r_hand_installed = r_hand_installed
    )
    rohand_service.Init()
    while True:
        time.sleep(1)
        

    
