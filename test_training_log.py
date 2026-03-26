from training_log import TrainingLog, Session

def test_pace():
    s = Session("01/01/2022", 10, "50:00", "Test session")
    assert s.get_pace() == 5.0

