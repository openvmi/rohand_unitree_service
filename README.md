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
cd rohand_unitree_service/cli
python3 rohand_node.py
```