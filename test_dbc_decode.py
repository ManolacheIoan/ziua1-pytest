import cantools
import pytest

db = cantools.database.load_file('vehicle.dbc')


def test_decode_speed_message():
    message_def = db.get_message_by_name('SPEED_MSG')
    
    raw_data = message_def.encode({'Speed': 120.5})
    
    decoded = message_def.decode(raw_data)
    
    assert decoded['Speed'] == 120.5


def test_decode_temperature_message():
    message_def = db.get_message_by_name('TEMP_MSG')
    
    raw_data = message_def.encode({'EngineTemp': 90})
    
    decoded = message_def.decode(raw_data)
    
    assert decoded['EngineTemp'] == 90


def test_message_ids_match_dbc():
    speed_msg = db.get_message_by_name('SPEED_MSG')
    temp_msg = db.get_message_by_name('TEMP_MSG')
    
    assert speed_msg.frame_id == 291
    assert temp_msg.frame_id == 292
