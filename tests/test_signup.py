def test_signup_initial(): # with errors
    user = dict(name="non_existing_user")
    
    assert user.name == "non_existing_user"

    user = None


def test_signup_final():
    user_name = "automation_test_removein_ 30_days_non_existing_user"
    user = dict(name=user_name) # user.create()

    print(f"User {user_name} create")
 
    assert user.get('name') == user_name  # if there will be no name it will give None
    # assert user['name'] == user_name    # if there will be no name it will give error (excetion unknown key)
    # assert user.get('name') == "jshhuasfh"  # po fail assercie sprawdzenie nie pojdzie dalej

    user = None   # user.remove()

    print(f"User {user_name} remove")

