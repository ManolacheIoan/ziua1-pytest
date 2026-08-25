import can
import pytest

@pytest.fixture
def can_buses():
    bus_sender = can.interface.Bus(channel='vcan0', interface='virtual')
    bus_receiver = can.interface.Bus(channel='vcan0', interface='virtual')
    yield bus_sender, bus_receiver
    bus_sender.shutdown()
    bus_receiver.shutdown()

def test_send_and_receive_message(can_buses):
    bus_sender, bus_receiver = can_buses
    
    message = can.Message(
        arbitration_id=0x123,
        data=[0x01, 0x02, 0x03, 0x04],
        is_extended_id=False
    )
    bus_sender.send(message)
    
    received = bus_receiver.recv(timeout=1)
    
    assert received is not None
    assert received.arbitration_id == 0x123
    assert list(received.data) == [0x01, 0x02, 0x03, 0x04]

def test_message_id_is_correct(can_buses):
    bus_sender, bus_receiver = can_buses
    
    message = can.Message(arbitration_id=0x200, data=[0xFF], is_extended_id=False)
    bus_sender.send(message)
    
    received = bus_receiver.recv(timeout=1)
    assert received.arbitration_id == 0x200
