from app import login

def test_login_success():
    assert login("student", "password123") == True

def test_login_failure():
    assert login("student", "wrongpass") == False
