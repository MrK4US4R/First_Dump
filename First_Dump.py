import platform
b = platform.architecture()[0]
if b == '64bit':
    import MIX_DUMP
elif b == '32bit':
    print("NOT SUPPORTED BRO YOUR PHONE 32 BIT")
