
class MemberDomain:
    def __init__(self,email,passwd,name,nickname,phonenumber,birthday,address):
        self.u_email = email
        self.u_passwd = passwd
        self.u_name = name
        self.u_nick_name = nickname
        self.u_phone_number = phonenumber
        self.u_birthday = birthday
        self.u_address = address
        

    def __eq__(self,email):
        if self.u_email == email:
            return True
        else:
            return False

class LoginMemberDomain:
    def __init__(self,email,passwd):
        self.email = email
        self.passwd = passwd
    
    def __eq__(self,email):
        if self.email == email:
            return True
        else:
            return False

class UpdateDomain:
    def __init__(self,email,passwd,nickname,phonenumber,address):
        self.email = email
        self.passwd = passwd
        self.nickname = nickname
        self.phonenumber = phonenumber
        self.address = address

class ClubDomain:
    def __init__(self,club_id,email,intro):
        self.club_id = club_id
        self.m_email = email
        self.intro = intro

    def __eq__(self,club_id):
        if self.club_id == club_id:
            return True
        else:
            return False

# class ClickDomain:
#     def __init__(self,c_num):
#         self.c_num = c_num
