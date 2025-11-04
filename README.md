# rohand_unitree_service

ROHAND Service designed for Unitree robots

## Installation

* Installing from source

```sh
#Linux
#Clone the source code
git clone https://github.com/openvmi/rohand_unitree_service.git
cd rohand_unitree_service
#Init the submodule
git submodule init
git submodule update

#Install the unitree_sdk2
python3 -m pip install -e ./src/unitree_sdk2_python/

#Install the ohand_serial_sdk_python
python3 -m pip install -e ./src/ohand_serial_sdk_python/

#Install the rohand_unitree_service
python3 -m pip install -e .
```

* Run the rohand subscriber

```sh
# usage: ROHand service for unitree [-h] [--nt NT] [--r_hand_id R_HAND_ID] [--l_hand_id L_HAND_ID] [--port PORT]
#                                   [--disable_r_hand] [--disable_l_hand]

# options:
#   -h, --help            show this help message and exit
#   --nt NT               network interface
#   --r_hand_id R_HAND_ID
#                         ROHand ID for right
#   --l_hand_id L_HAND_ID
#                         ROHand id for left
#   --port PORT           Port for 485 communication
#   --disable_r_hand      Right ROHand is not installed
#   --disable_l_hand      Left ROHand is not installed
cd rohand_unitree_service/cli
python3 rohand_node.py
```

* Run the rohand publisher

```sh
# usage: ROHand service for unitree [-h] [--nt NT] [--disable_r_hand] [--disable_l_hand]

# options:
#   -h, --help        show this help message and exit
#   --nt NT           network interface
#   --disable_r_hand  Right ROHand is installed
#   --disable_l_hand  Left ROHand is installed
cd rohand_unitree_service/cli
python3 rohand_publish.py
```