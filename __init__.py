print("\nfkserver:OK!\n")

import sys, os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)))
from .fk_server import  Cancelled

NODE_CLASS_MAPPINGS = {}
WEB_DIRECTORY = "web"

__all__ = ["NODE_CLASS_MAPPINGS"]
IP_VERSION = "1.0"