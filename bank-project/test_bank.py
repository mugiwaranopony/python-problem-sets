import pytest

import bank


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    """Use a temporary database so tests never change the real db.json."""
    test_db = tmp_path / "db.json"
    monkeypatch.setattr(bank, "DB_FILE", str(test_db))
    return test_db


def make_user(password="secret", balance=0.0):
    return {
        "password": password,
        "balance": balance,
        "transactions": [],
    }


def test_load_db_returns_empty_database_when_file_is_missing(isolated_db):
    assert bank.load_db() == {"users": {}}


def test_save_and_load_db(isolated_db):
    expected = {"users": {"alice": make_user(balance=100.0)}}

    bank.save_db(expected)

    assert bank.load_db() == expected


def test_read_amount_returns_rounded_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "10.567")

    assert bank.read_amount("Amount: $") == 10.57


@pytest.mark.parametrize("invalid_amount", ["hello", "0", "-25"])
def test_read_amount_rejects_invalid_values(monkeypatch, invalid_amount):
    monkeypatch.setattr("builtins.input", lambda prompt: invalid_amount)

    assert bank.read_amount("Amount: $") is None


def test_register_creates_new_user(isolated_db, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "alice")
    monkeypatch.setattr(bank, "getpass", lambda prompt: "secret")

    bank.register()
    user = bank.load_db()["users"]["alice"]

    assert user["password"] == "secret"
    assert user["balance"] == 0.0
    assert user["transactions"] == []


def test_register_rejects_duplicate_username(isolated_db, monkeypatch, capsys):
    original = {"users": {"alice": make_user()}}
    bank.save_db(original)
    monkeypatch.setattr("builtins.input", lambda prompt: "alice")

    bank.register()

    assert bank.load_db() == original
    assert "already taken" in capsys.readouterr().out


def test_login_returns_username_for_correct_password(isolated_db, monkeypatch):
    bank.save_db({"users": {"alice": make_user(password="secret")}})
    monkeypatch.setattr("builtins.input", lambda prompt: "alice")
    monkeypatch.setattr(bank, "getpass", lambda prompt: "secret")

    assert bank.login() == "alice"


def test_login_rejects_wrong_password(isolated_db, monkeypatch):
    bank.save_db({"users": {"alice": make_user(password="secret")}})
    monkeypatch.setattr("builtins.input", lambda prompt: "alice")
    monkeypatch.setattr(bank, "getpass", lambda prompt: "wrong-password")

    assert bank.login() is None


def test_deposit_updates_balance_and_history(isolated_db, monkeypatch):
    bank.save_db({"users": {"alice": make_user(balance=100.0)}})
    monkeypatch.setattr("builtins.input", lambda prompt: "50.25")

    bank.deposit("alice")
    user = bank.load_db()["users"]["alice"]

    assert user["balance"] == 150.25
    assert user["transactions"][0]["type"] == "deposit"
    assert user["transactions"][0]["amount"] == 50.25
    assert "at" in user["transactions"][0]


def test_withdraw_updates_balance_and_history(isolated_db, monkeypatch):
    bank.save_db({"users": {"alice": make_user(balance=100.0)}})
    monkeypatch.setattr("builtins.input", lambda prompt: "30")

    bank.withdraw("alice")
    user = bank.load_db()["users"]["alice"]

    assert user["balance"] == 70.0
    assert user["transactions"][0]["type"] == "withdraw"
    assert user["transactions"][0]["amount"] == 30.0


def test_withdraw_rejects_insufficient_funds(isolated_db, monkeypatch, capsys):
    bank.save_db({"users": {"alice": make_user(balance=20.0)}})
    monkeypatch.setattr("builtins.input", lambda prompt: "50")

    bank.withdraw("alice")
    user = bank.load_db()["users"]["alice"]

    assert user["balance"] == 20.0
    assert user["transactions"] == []
    assert "Insufficient funds" in capsys.readouterr().out


def test_transfer_updates_both_users_and_histories(isolated_db, monkeypatch):
    bank.save_db(
        {
            "users": {
                "alice": make_user(balance=100.0),
                "bob": make_user(balance=25.0),
            }
        }
    )
    answers = iter(["bob", "40"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    bank.transfer("alice")
    users = bank.load_db()["users"]

    assert users["alice"]["balance"] == 60.0
    assert users["bob"]["balance"] == 65.0
    assert users["alice"]["transactions"][0]["type"] == "transfer_out"
    assert users["alice"]["transactions"][0]["to"] == "bob"
    assert users["bob"]["transactions"][0]["type"] == "transfer_in"
    assert users["bob"]["transactions"][0]["from"] == "alice"