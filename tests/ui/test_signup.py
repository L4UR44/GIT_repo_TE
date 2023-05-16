import pytest
from src.user import User

@pytest.fixture
def specific_sign_up_user_fixture():
    yield 42


def test_signup_initial(specific_sign_up_user_fixture):
    assert specific_sign_up_user_fixture == 42


# @pytest.fixture(scope="session")  # (scope="session|package|module|class|function")
# def user_fixture():



def test_signup_final_negative(user_fixture):
    # print("NEG TEST CASE STEPS EXEC")

    assert user_fixture.get('name') == "aaaaaaautomation_test_removein_30_days_non_existing_user" 


def test_signup_final_positive(user_fixture):
    # print("POS TEST CASE STEPS EXEC")

    assert user_fixture.get('name') == User.username 


# def test_signup_final():
#     user_name = "automation_test_removein_ 30_days_non_existing_user"
#     user = dict(name=user_name) # user.create()

#     print(f"User {user_name} created")
 
#     assert user.get('name') == user_name  # if there will be no name it will give None
#     # assert user['name'] == user_name    # if there will be no name it will give error (excetion unknown key)
#     # assert user.get('name') == "jshhuasfh"  # po fail assercie sprawdzenie nie pojdzie dalej

#     user = None   # user.remove()

#     print(f"User {user_name} remove")