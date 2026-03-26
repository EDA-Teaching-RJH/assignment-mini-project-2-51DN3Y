from training_log import TrainingLog, Session, RowingSession

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

def test_invalid_session():
    log = TrainingLog()
    log.remove_session(5)
    assert len(log.get_all_sessions()) == 0

def test_zero_distance():
    s = Session("01/01/2022", 0, "50:00", "Test")
    assert s.get_pace() is None

def test_rowing_session():
    s = RowingSession("01/01/2022", 10, "50:00", "Test session", 25)
    assert "22" in str(s)
    assert "Stroke Rate" in str(s)
