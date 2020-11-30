import requests


def sign_up():
    sign_up_url = "http://127.0.0.1:8956/Sign/Up"
    email = "go2ranuga@gmail.com"
    user_name = "user name"
    password = "password"
    result = requests.get(  # or post
        sign_up_url, {"Email": email, "Password": password, "User Name": user_name}
    )
    print(result.json())


def sign_in():
    sign_in_url = "http://127.0.0.1:8956/Sign/In"
    user_name_or_email = input("User Name or Email : ")
    password = input("Password : ")
    result = requests.get(  # or post
        sign_in_url, {"User Name or Email": user_name_or_email, "Password": password}
    )
    print(result.json())


def log_out():
    log_out_url = "http://127.0.0.1:8956/Log/Out"
    result = requests.get(log_out_url)  # or post
    print(result.json())


def send_email():
    send_email_url = "http://127.0.0.1:8956/Send/Email(s)"
    to_email = input("To Email : ")
    subject = input("Subject : ")
    body = input("Body : ")
    result = requests.get(  # or Post
        send_email_url, {"To Email": to_email, "Subject": subject, "Body": body}
    )
    print(result.json())

sign_up()