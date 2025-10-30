from .core import ROHandCtrl, ROHandCtrlMode
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from ohand.constants import *
from ohand.interface.uart import *
from ohand.OHandSerialAPI import OHandSerialAPI
import threading

__all__ = [
    "ROHandService"
]

class ROHandService:
    def __init__(self,r_hand_id=0x01, 
                 l_hand_id=0x02,
                 port="/dev/ttyUSB0",
                 l_hand_installed = True,
                 r_hand_installed=True):
        self._r_hand_id = r_hand_id
        self._l_hand_id = l_hand_id
        self._port = port
        self._l_hand_ctrl_topic = 'rt/rohand/l/ctrl'
        self._r_hand_ctrl_topic = 'rt/rohand/r/ctrl'
        self._l_hand_installed = l_hand_installed
        self._r_hand_installed = r_hand_installed
        self._interface_instance = Serial_Init(port_name=self._port, baudrate=115200)
        self._ohand_instane = OHandSerialAPI(self._interface_instance,
                                             HAND_PROTOCOL_UART,
                                             0x01,
                                             send_data_impl,
                                             recv_data_impl)
        self._lock = threading.Lock()
    
    def Init(self):
        if self._l_hand_installed:
            self._l_hand_subscriber = ChannelSubscriber(self._l_hand_ctrl_topic,ROHandCtrl)
            self._l_hand_subscriber.Init(self._l_hand_ctrl_handler, 10)

        if self._r_hand_ctrl_handler:
            self._r_hand_subscriber = ChannelSubscriber(self._r_hand_ctrl_topic, ROHandCtrl)
            self._r_hand_subscriber.Init(self._r_hand_ctrl_handler, 10)

    def _l_hand_ctrl_handler(self, msg: ROHandCtrl):
        self.rohandCtrlHandler(self._l_hand_id, msg)

    def _r_hand_ctrl_handler(self,msg: ROHandCtrl):
        self.rohandCtrlHandler(self._r_hand_id, msg)

    def rohandCtrlHandler(self, hand_id, msg: ROHandCtrl):
        err = HAND_RESP_SUCCESS
        with self._lock:
            if msg.mode == ROHandCtrlMode.HAND_MODE_ANGLE:
                err = self._ohand_instane.HAND_SetFingerAngle(hand_id,
                                                              msg.finger_id,
                                                              msg.target_value,
                                                              msg.speed,
                                                              [])
            elif msg.mode == ROHandCtrlMode.HAND_MODE_POSITION:
                err = self._ohand_instane.HAND_SetFingerPos(hand_id,
                                                            msg.finger_id,
                                                            msg.target_value,
                                                            msg.speed,
                                                            [])
            if err != HAND_RESP_SUCCESS:
                print(f"rohandCtrl {hand_id} return error:{err}")