# tests/test_user_repository.py
import pytest
from unittest.mock import MagicMock

# >>> HIER anpassen:
# z.B. from crud import UserRepository
from crud import UserRepository
from models import User


# Mini-User-Dummy (reicht für diese Tests; muss keine echte SQLAlchemy-Klasse sein)
# class DummyUser:
#     def __init__(self, username=None, password=None):
#         self.username = username
#         self.password = password


@pytest.fixture
def session():  # Fake-Session  test_methode(session)
    return MagicMock()   # kann über Parameter verwendet werden: def test_create_raises_if_username_exists(repo, session):


@pytest.fixture
def repo(session):  # test_methode(repo)
    return UserRepository(session)   # kann über Parameter verwendet werden


# -------------------------
# Tests für create()
# -------------------------

def test_create_raises_if_user_is_none(repo):
    with pytest.raises(ValueError, match="user darf nicht None sein"):
        repo.create(None)


def test_create_raises_if_username_missing(repo):
    user = User(username="", password="123")
    with pytest.raises(ValueError, match="username ist Pflicht"):
        repo.create(user)


def test_create_raises_if_password_missing(repo):
    user = User(username="max", password="")
    with pytest.raises(ValueError, match="password ist Pflicht"):
        repo.create(user)


def test_create_raises_if_username_exists(repo, session):
    # Session query-chain: session.query(User).filter(...).first() -> existing user
    q = session.query.return_value
    f = q.filter.return_value
    f.first.return_value = User(username="max", password="hashed")

    user = User(username="max", password="12345")
    with pytest.raises(ValueError, match="username existiert bereits"):
        repo.create(user)

    session.add.assert_not_called() # Es wurde kein Objekt zum Session-Context hinzugefügt (also kein “insert vorbereiten”).
    session.commit.assert_not_called()# Es wurde kein Commit gemacht (also keine Transaktion wirklich gespeichert).
    session.refresh.assert_not_called()# s wurde kein Refresh gemacht

# positiv
def test_create_hashes_password_and_persists(repo, session, monkeypatch):
    # Kein existing user
    q = session.query.return_value
    f = q.filter.return_value
    f.first.return_value = None

    # hash_password mocken (wichtig: Patch-PFAD muss das Modul sein, in dem UserRepository hash_password importiert!)
    def fake_hash(pw):
        return "HASHED_" + pw
    #monkeypatch.setattr(<ziel>, <ersatz>) -> "crud.hash_password", fake_hash
    monkeypatch.setattr("crud.hash_password", fake_hash)

    user = User(username="max", password="12345")
    created = repo.create(user)

    assert created is user
    assert user.password == "HASHED_12345" # original: hash_password(user.password)

    session.add.assert_called_once_with(user) #  self.session.add(user)
    session.commit.assert_called_once()#     self.session.commit()
    session.refresh.assert_called_once_with(user)#  self.session.refresh(user)


# -------------------------
# Tests für get_user_by_credentails()
# -------------------------


def test_get_user_by_credentials_returns_none_if_user_not_found(repo, session):
    # Die drei Zeilen bauen dir eine Fake-Query-Kette auf, damit dein Repository denkt, 
    # es hätte eine echte SQLAlchemy-Session vor sich.
    # bedeutet so etwas:user = self.session.query(User).filter(User.username == username).first()
    q = session.query.return_value #self.session.query(User)
    f = q.filter.return_value #filter(User.username == username)
    f.first.return_value = None #.first()
    assert repo.get_user_by_credentails("max", "12345") is None

def test_get_user_by_credentials_returns_user_if_password_ok(repo, session, monkeypatch):
    db_user = User(username="max", password="HASHED_12345")
    q = session.query.return_value
    f = q.filter.return_value
    f.first.return_value = db_user

    #monkeypatch.setattr(<ziel>, <ersatz>)
    #  lambda plain, hashed: True
    # Eine anonyme Funktion, die zwei Parameter annimmt (so wie verify_password(plain, hashed)), 
    # aber immer True liefert – egal welches Passwort.
    # das gleiche, wie:
    # def always_true(plain, hashed):
    #     return True

    monkeypatch.setattr("crud.verify_password", lambda plain, hashed: True)

    assert repo.get_user_by_credentails("max", "12345") is db_user