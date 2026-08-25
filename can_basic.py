import can

bus = can.interface.Bus(channel='vcan0', interface='virtual')

message = can.Message(
    arbitration_id=0x123,
    data=[0x01, 0x02, 0x03, 0x04],
    is_extended_id=False
)

bus.send(message)
print(f"Mesaj trimis: ID={hex(message.arbitration_id)}, Data={list(message.data)}")

received = bus.recv(timeout=1)
if received:
    print(f"Mesaj primit: ID={hex(received.arbitration_id)}, Data={list(received.data)}")
