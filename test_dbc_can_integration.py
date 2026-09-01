import can
import cantools
import pytest

db = cantools.database.load_file('vehicle.dbc')


@pytest.fixture
def can_buses():
    bus_sender = can.interface.Bus(channel='vcan0', interface='virtual')
    bus_receiver = can.interface.Bus(channel='vcan0', interface='virtual')
    yield bus_sender, bus_receiver
    bus_sender.shutdown()
    bus_receiver.shutdown()


def test_send_real_speed_message(can_buses):
    bus_sender, bus_receiver = can_buses
    
    speed_msg_def = db.get_message_by_name('SPEED_MSG')
    encoded_data = speed_msg_def.encode({'Speed': 85.3})
    
    can_message = can.Message(
        arbitration_id=speed_msg_def.frame_id,
        data=encoded_data,
        is_extended_id=False
    )
    bus_sender.send(can_message)
    
    received = bus_receiver.recv(timeout=1)
    decoded = speed_msg_def.decode(received.data)
    
    assert decoded['Speed'] == pytest.approx(85.3)
