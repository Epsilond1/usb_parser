import usb.core


def get_usb_devices():
    return usb.core.show_devices()


def ping():
    return {'status': 'OK'}
