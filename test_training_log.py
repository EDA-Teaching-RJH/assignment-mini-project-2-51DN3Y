from training_log import TrainingLog, Session

def test_pace():
    s = Session("01/01/2022", 10, "50:00", "Test session")
    assert s.get_pace() == 5.0

def test_add_session():
    log = TrainingLog()
    s = Session("01/01/2022", 10, "50:00", "Test session")
    log.add_session(s)
    assert len(log.get_all_sessions()) == 1

def test_remove_session():
    log = TrainingLog()
    s = Session("01/01/2022", 10, "50:00", "Test session")
    log.add_session(s)
    log.remove_session(0)
    assert len(log.get_all_sessions()) == 0


