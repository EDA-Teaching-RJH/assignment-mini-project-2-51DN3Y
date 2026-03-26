from training_log import TrainingLog, Session, RowingSession

def test_pace():
    '''
    Test that pace is calculated correctly.'''
    s = Session("01/01/2022", 10, "50:00", "Test session")
    assert s.get_pace() == 5.0

def test_add_session():
    '''
    Test adding a session to the training log.'''
    log = TrainingLog()
    s = Session("01/01/2022", 10, "50:00", "Test session")
    log.add_session(s)
    assert len(log.get_all_sessions()) == 1

def test_remove_session():
    '''
    Test removing a session from the training log.'''
    log = TrainingLog()
    s = Session("01/01/2022", 10, "50:00", "Test session")
    log.add_session(s)
    log.remove_session(0)
    assert len(log.get_all_sessions()) == 0

def test_invalid_session():
    '''
    Test that removing a session with an invalid index does not cause errors.'''
    log = TrainingLog()
    log.remove_session(5)
    assert len(log.get_all_sessions()) == 0

def test_zero_distance():
    '''
    Test that pace calculation handles zero distance without error.'''
    s = Session("01/01/2022", 0, "50:00", "Test")
    assert s.get_pace() is None

def test_rowing_session():
    '''
    Test that rowing sessions are created with the correct stroke rate.'''
    s = RowingSession("01/01/2022", 10, "50:00", "Test session", 25)
    assert "25" in str(s)
    assert "Stroke Rate" in str(s)
