import requests

user_error_message = "Username does not exist"
password_error_message = "Password is not correct for the given username."

users_list = ["name1", "name2", "name3", "name4", "name5","admin"]
pass_list = ["pass1", "pass2", "pass3", "pass4", "pass5","admin"]

if vuln:  # Password Enumeration
    if user and request_data.get('password') != user.password:
        return Response(error_message_helper("Password is not correct for the given username. Week2 Completed"), 200, mimetype="application/json")
    elif not user:  # User enumeration
        return Response(error_message_helper("Username does not exist"), 200, mimetype="application/json")
else:
    if (user and request_data.get('password') != user.password) or (not user):
        return Response(error_message_helper("Username or Password Incorrect!"), 200, mimetype="application/json")
