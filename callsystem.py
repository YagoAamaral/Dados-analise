import ctypes


lib = ctypes.CDLL('./libsysinfo.so')


lib.get_system_info()
