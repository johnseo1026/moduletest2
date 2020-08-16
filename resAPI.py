import requests
import urllib
import json


class MemberStore:



    def __init__(self):
        # self.url = 'http://ec2_url/' # url은 nodejs를 작성한 ec2로 해야함
        # self.url = 'Module2-ec2-LB-628908149.us-west-2.elb.amazonaws.com:8000'
        self.headers = {'Content-Type': 'application/json; chearset=utf-8'}
        self.url = 'http://ec2-18-237-217-34.us-west-2.compute.amazonaws.com:8000'
        # URL NODEJS로 된것 받아서 수정해야함

    # 이메일, 패스워드 확인
    def login_ok(self,email, passwd):
        print("이메일, 패스워드 확인")
        if bool(email) and bool(passwd):
            # api_result = requests.get(self.url + "/users/isexist/" + email +"/" + passwd)
            api_result = requests.get(url=self.url + '/users/isexist', params={'email':email,'passwd':passwd}, headers = self.headers)
            print("이메일, 패스워드 확인의 api_result 값: ",api_result)
            result = api_result.json()
            print("login_ok: ",result)
        if not bool(result):
            return 1
        else:
            return 0
            # fetchaone으로 가져옴 -> 예상 return email
            
    # 이메일 검증
    def email_Validation(self,email):
        if bool(email):
            api_result = requests.get(self.url + "/users/Confirm/" + email, headers = self.headers)
            api_result = api_result.json()
        print("email_Validation: ",api_result)
        return api_result 
        # fetchaone으로 가져옴 -> 예상 return email

    # 유저 등록
    def insert_member(self,entity):
        body = {'email':entity.u_email, 'passwd':entity.u_passwd,'name':entity.u_name,
                'nickname':entity.u_nick_name,'phonenumber': entity.u_phone_number,
                'birthday':entity.u_birthday,'address':entity.u_address}
        res = requests.post(self.url, data=json.dumps(body), headers = self.headers)
        res = res.json()
        print("insert_member: ",res)
        if bool(res):
            return True

    # 유저 수정
    def update_member(self,email,passwd,nickname,phonenumber,address):
        body = {'passwd':passwd, 'nickname': nickname, 
                'phonenumber':phonenumber,"address":address}
        api_result = requests.put(self.url +"/users/update/"+email, data=json.dumps(body), headers = self.headers)
        print("update_member: ",api_result)
        return api_result["number"]

    # 유저 탈퇴
    def delete_member(self,email):
        if bool(email):
            api_result = requests.delete(self.url + "/users/delete/" + email, headers = self.headers)
        print("delete_member: ",api_result)
        return api_result["number"]

    # 유저 정보
    def select_one_member(self,email):
        if bool(email):
            api_result = requests.get(self.url + "/users/info/" + email, headers = self.headers)
        print("select_one_member: ",api_result)
        return api_result

    # 회원탈퇴 클럽멤버십 삭제
    def delete_all_club_membership(self,email):
        api_result = requests.delete(self.url + "/users/delete/clubMembership" + email, headers = self.headers)
        print("회원탈퇴 클럽멤버십 삭제: ", api_result)
        return api_result["number"]
    
    # 생성한 클럽 전체 탈퇴
    def drop_club_all(self,email):
        api_result = requests.delete(self.url + "/users/delete/Allclub" + email, headers = self.headers)
        print("생성한 클럽 전체 탈퇴: ",api_result)
        return api_result["number"]

    # 연결 끊기
    def close(self):
        requests.get(self.url + "/logout", headers = self.headers)
        
        