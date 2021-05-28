import pyshark
import os

time_of_sniffing = int(input("Time to sniff: "))
capture = pyshark.LiveCapture(interface='lo', bpf_filter= 'port 4040')
print("Sniffing...")
capture.sniff(timeout = time_of_sniffing)
print('Sniff Completed')
number_of_resend = 0
total_length = 0

i = 0
while i < len(capture):
    protocol = capture[i].transport_layer
    try:
        if capture[i].tcp.analysis_retransmission:
            number_of_resend += 1
    except:
        pass
    total_length += int(capture[i].length)
    i += 1

throughput = total_length / time_of_sniffing
print(f"Total packets: {i}")
print(f"Throughput: {throughput} bits/sec")
print(f"Resent packets: {number_of_resend}")
os._exit(1)