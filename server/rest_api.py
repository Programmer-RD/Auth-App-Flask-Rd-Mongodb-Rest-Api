from server import *
from flask_restful import reqparse
from server.db.auth import *

sign_in_rest_api_info = reqparse.RequestParser()
sign_in_rest_api_info.add_argument(
    name="User Name or Email",
    required=True,
    help="Please Pass The User Name or The Email.",
    type=str,
)
sign_in_rest_api_info.add_argument(
    name="Password", required=True, help="Please Pass The Password.", type=str
)


def sign_in_rest_api(info):
    try:
        si = Sign_In(
            user_name_or_email=info["User Name or Email"], password=info["Password"]
        )
        result = si.check()
        if result[0]:
            session["Auth"] = True
        return [result]
    except:
        return ["An error occured ! "]


class Sign_In_Route_Api(Resource):
    def get(self):
        try:
            if "User Name" in session and "Password" in session:
                return {
                    "result": sign_in_rest_api(
                        info={
                            "User Name or Email": session["User Name"],
                            "Password": session["Password"],
                        }
                    )
                }
            if "Auth" in session:
                return {"result": [True, "You are already loged in ! "]}
            info = sign_in_rest_api_info.parse_args()
            result = sign_in_rest_api(info=info)
            return [result]
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            if "User Name" in session and "Password" in session:
                return {
                    "result": sign_in_rest_api(
                        info={
                            "User Name or Email": session["User Name"],
                            "Password": session["Password"],
                        }
                    )
                }
            if "Auth" in session:
                return {"result": [True, "You are already loged in ! "]}
            info = sign_in_rest_api_info.parse_args()
            result = sign_in_rest_api(info=info)
            return [result]
        except:
            return ["An error occured ! "]


sign_up_rest_api_info = reqparse.RequestParser()
sign_up_rest_api_info.add_argument(
    name="User Name",
    required=True,
    help="Please Pass The User Name",
    type=str,
)
sign_up_rest_api_info.add_argument(
    name="Email", required=True, help="Please Pass The Email.", type=str
)
sign_up_rest_api_info.add_argument(
    name="Password", required=True, help="Please Pass The Password.", type=str
)


def sign_up_rest_api(info):
    try:
        su = Sign_Up(
            user_name=info["User Name"], password=info["Password"], email=info["Email"]
        )
        result = su.add_to_db()
        if result[0]:
            session["User Name"] = info["User Name"]
            session["Password"] = info["Password"]
            return redirect("/Sign/In")
        return [result]
    except:
        return ["An error occured ! "]


class Sign_Up_Route_Api(Resource):
    def get(self):
        try:
            info = sign_up_rest_api_info.parse_args()
            result = sign_up_rest_api(info=info)
            return {"result": result}
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            info = sign_up_rest_api_info.parse_args()
            result = sign_up_rest_api(info=info)
            return {"result": result}
        except:
            return ["An error occured ! "]


send_email_rest_api_info = reqparse.RequestParser()
send_email_rest_api_info.add_argument(
    name="To Email", required=True, help="Please Pass The To Email.", type=str
)
send_email_rest_api_info.add_argument(
    name="Subject", required=True, help="Please Pass The Subject.", type=str
)
send_email_rest_api_info.add_argument(
    name="Message", required=True, help="Please Pass The Message.", type=str
)


def send_email_rest_api(info):
    try:
        sm = send_mail(
            to_email=info["To Email"], subject=info["Subject"], body=info["Message"]
        )
        return [sm]
    except:
        return ["An error occured ! "]


class Send_Email_Rest_Api(Resource):
    def get(self):
        try:
            if "Auth" in session:
                info = send_email_rest_api_info.parse_args()
                return {"result": send_email_rest_api(info=info)}
            return {
                "result": "Please Login(Sign In) or Pass Your User Name or Email and Your Email Please."
            }
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            if "Auth" in session:
                info = send_email_rest_api_info.parse_args()
                return {"result": send_email_rest_api(info=info)}
            return {
                "result": "Please Login(Sign In) or Pass Your User Name or Email and Your Email Please."
            }
        except:
            return ["An error occured ! "]


def log_out_rest_api():
    try:
        session.pop("Auth", None)
    except:
        return ["An error occured ! "]


class Log_Out_Rest_Api(Resource):
    def get(self):
        try:
            if "Auth" in session:
                log_out_rest_api()
                return {"result": [True, "Loged Out Successfully ! "]}
            return {"result": "First Login ! "}
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            if "Auth" in session:
                log_out_rest_api()
                return {"result": [True, "Loged Out Successfully ! "]}
            return {"result": "First Login ! "}
        except:
            return ["An error occured ! "]


class Help(Resource):
    def get(self):
        try:
            return {
                "result": "/Sign/Up => parms = {'User Name':'Your User Name','Password':'Your Password','Email':'Your Email'} \n /Sign/In => parms = {'User Name or Email':'Your User Name or Email','Password':'Your Password'} \n /Send/Email(s) => First you need to sign in then you can send a get request to the /Send/Email(s) | parmas = {'To Email':'To Email','Subject','Subject':'Subject of the Email','Message':'Message of the Email'} if you pass {'User Name or Email':'Your User name or email','Password':'Your Password'} you can also send a email \n if you have any problem please send a email to go2ranuga@gmail.com \n Thank you \n Requests Accepted == 'GET' and 'POST' requests"
            }
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            return {
                "result": "/Sign/Up => parms = {'User Name':'Your User Name','Password':'Your Password','Email':'Your Email'} \n /Sign/In => parms = {'User Name or Email':'Your User Name or Email','Password':'Your Password'} \n /Send/Email(s) => First you need to sign in then you can send a get request to the /Send/Email(s) | parmas = {'To Email':'To Email','Subject','Subject':'Subject of the Email','Message':'Message of the Email'} if you pass {'User Name or Email':'Your User name or email','Password':'Your Password'} you can also send a email \n if you have any problem please send a email to go2ranuga@gmail.com \n /Log/Out to Log out \n Thank you \n Requests Accepted == 'GET' and 'POST' requests"
            }
        except:
            return ["An error occured ! "]


api.add_resource(Help, "/H")
api.add_resource(Send_Email_Rest_Api, "/Send/Email(s)")
api.add_resource(Sign_In_Route_Api, "/Sign/In")
api.add_resource(Sign_Up_Route_Api, "/Sign/Up")
api.add_resource(Log_Out_Rest_Api, "/Log/Out")
