# Just remember to run this file when iperf server is still running

import os
import json
import matplotlib.pyplot

(x_client, y_client, x_server, y_server) = ([], [], [], [])
with open(os.path.dirname(os.path.realpath(__file__)) + "/client.json") as client:
    client_data = json.load(client)
    client_packets = client_data["intervals"]
    for packet in client_packets:
        x_client.append(packet["streams"][0]["end"])
        y_client.append(packet["streams"][0]["bits_per_second"])
with open(os.path.dirname(os.path.realpath(__file__)) + "/server.json") as server:
    server_data = json.load(server)
    server_packets = server_data["intervals"]
    for packet in server_packets:
        x_server.append(packet["streams"][0]["end"])
        y_server.append(packet["streams"][0]["bits_per_second"])
matplotlib.pyplot.plot(x_client, y_client ,marker='o', color='b', label='Client')
matplotlib.pyplot.plot(x_server, y_server ,marker='o', color='g', label='Server')
matplotlib.pyplot.legend(loc = 'lower right')
matplotlib.pyplot.ylabel("Bits_Per_Second")
matplotlib.pyplot.xlabel("Time")
matplotlib.pyplot.show()