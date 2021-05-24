import pyshark
capture = pyshark.LiveCapture(interface='lo')
capture.sniff(timeout=5)
print('salam')
for packet in capture.sniff_continuously(packet_count=5):
    print(f'Just arrived:{packet}')