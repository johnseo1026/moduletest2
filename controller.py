import tkinter
# from model import Member_Model
from resAPI import MemberStore
from view import MemberView, SignInView, SignUpView, UpdateMember, ClubView, DeleteMember
import domain
import controller
import re

class Member_Controller:
    window = tkinter.Tk()
    cookie_email = ""
    def __init__(self):  
        self.member_view = MemberView(Member_Controller.window)
        self.member_model = MemberStore()
        self.siv = SignInView(Member_Controller.window)
        self.suv = SignUpView(Member_Controller.window)
        self.um = UpdateMember(Member_Controller.window)
        self.cv = ClubView(Member_Controller.window)
        self.dm = DeleteMember(Member_Controller.window)
        
    # 프로그램 실행

    def run(self):
        print("프로그램 실행")
        self.window.title("클럽 관리 프로그램")
        self.window.geometry("300x250-800+100")    
        self.window.resizable(False, False)
        self.member_view.main_title()
        # 로그인 버튼
        self.siv.sign_in_button(self.window)
        # 회원가입 버튼
        self.suv.sign_up_button(self.window)
         # 마이페이지 버튼
        self.um.mypage_button(self.window)
        # 로그아웃 버튼
        self.um.log_out_button(self.window)
        # 회원 탈퇴 버튼
        self.dm.delete_member_button(self.window)
        # 클럽 메뉴 버튼
        self.cv.club_button(self.window)

        # # 클럽 가입 버튼
        # self.cv.club_join_button(self.window)
        # # 클럽 생성 버튼
        # self.cv.club_create_button(self.window)
        # # 클럽 수정 버튼
        # self.cv.club_update_button(self.window)
        # # 클럽 삭제 버튼
        # self.cv.club_delete_button(self.window)
        # # 클럽 리스트 조회 버튼
        # self.cv.club_search_list_button(self.window)
        # # 클럽 탈퇴 버튼
        # self.cv.club_secession_button(self.window)
        
    
    # 프로그램 종료
    def close_window(self):
        self.window.mainloop()
    
    # 쿠키 값 없애기
    def delete_cookie(self):
        controller.Member_Controller.cookie_email = None
        self.member_model.close()

    # 회원가입 정보 받아오고 가입 및 오류
    def sign_up_info(self,email,passwd,name,nickname,phonenumber,birthday,address):
        print("회원가입 정보 받아오고 가입 및 오류")
        d = domain.MemberDomain(email,passwd,name,nickname,phonenumber,birthday,address)
        print("d의정보",d.u_email,d.u_passwd,d.u_nick_name,d.u_phone_number,d.u_birthday,d.u_address)
        mm = self.member_model.email_Validation(d.u_email)
        print("mm의 결과",mm)
        if not bool(mm):
            result = self.member_model.insert_member(d)
            if bool(result):
                self.suv.sign_up_success()
        else:
            self.suv.sign_up_false()
    
    # 로그인 정보 받아오기
    def sign_in_info(self,email,passwd):
        print("로그인 정보 받아오기")
        d = domain.LoginMemberDomain(email,passwd)
        self.mm = self.member_model.login_ok(d.email,d.passwd)
        if self.mm == 0:
            self.siv.login_success()
            self.result = self.member_model.login_ok(d.email,d.passwd)
            print("result",self.result)
            Member_Controller.cookie_email = self.result
            print("cookieemail", Member_Controller.cookie_email)
        else:
            self.siv.login_false()

    # 멤버 상세 정보 받아오기
    def detail_member_info(self):
        # self.d = domain.MemberDomain(email,passwd,name,nickname,phonenumber,birthday,address)
        cm = Member_Controller.cookie_email  
        print("cm",cm.get("email"))
        if bool(cm.get("email")):
            result = self.member_model.select_one_member(cm.get("email"))
            print("result",result)
            d = domain.MemberDomain(result["email"],result["passwd"],result["name"],result["nickname"],result["phonenumber"],result["birthday"],result["address"])
            # self.um.my_update_detail_info(self.d.u_email,self.d.u_passwd,self.d.u_name,self.d.u_nick_name,self.d.u_phone_number,self.d.u_birthday,self.d.u_address,self.d.u_clubid)
            return d
        else:
            pass
        
    # 회원 정보 수정
    def update_info_con(self,email,passwd,nickname,phonenumber,address):
        d = domain.UpdateDomain(email,passwd,nickname,phonenumber,address)
        print("update Domain", d.email)
        result = self.member_model.update_member(d.email,d.passwd,d.nickname,d.phonenumber,d.address)
        print("회원정보수정Controller",result)
        if result == 1:
            self.um.my_update_message()
        else:
            pass

    def delete_info_controller(self):
        cm = Member_Controller.cookie_email
    # 회원 탈퇴
    def delete_info_controller(self):
        cm = Member_Controller.cookie_email
        cm_var = cm["email"]
        print("회원탈퇴 CONTROLLER", cm_var)
        if bool(cm_var):
            # 가입한 클럽 삭제(클럽멤버십)
            result = self.member_model.drop_clubmembership_model(cm_var)
            if result == 1:
                # 생성한 클럽 삭제
                result = self.member_model.drop_travelclub_model(cm_var)
                print("회원탈퇴 result",result)
                if result == 1:
                    # 멤버 삭제
                    result = self.member_model.delete_member_model(cm_var)
                    if result == 1:
                        pass
                        # self.dm.drop_club_message()
                    else:
                        pass
                else:
                    pass
            else:
                pass
            return 1
        else:
            pass

#     # 클럽 생성 정보 받고 처리
#     def create_club(self,clubid,intro):
#         cm = Member_Controller.cookie_email  
#         print("클럽 정보 받아오고 등록 및 오류")
#         print("cm",cm["email"])
#         if bool(cm["email"]):
#             result = self.member_model.member_select_one(cm["email"])
#             d = domain.ClubDomain(clubid,result["email"],intro)
#             print("d는 접근",d.club_id,d.m_email,d.intro)
#             get_club_info = self.member_model.select_club_model(clubid)
#             print("get_club_info 오나",get_club_info)
#             if not bool(get_club_info):
#                 print("not bool 진입")
#                 self.member_model.create_club_model(d)
#                 self.cv.club_create_message()
#             else:
#                 self.cv.club_create_fale_message()
#         else:
#             pass
    
#     # 클럽 수정 화면
#     def club_detail_controller(self):
#         cmc = Member_Controller.cookie_email  
#         print("클럽 수정")
#         if bool(cmc["email"]):
#             # 클럽 정보 
#             result = self.member_model.select_all_club_model(cmc["email"])
#             print("클럽상세 result",result)
#             return result
#         else:
#             pass
    
#     # 클럽 수정
#     def club_update_controller(self,clubid,clubid_up,clubadmin,intro):
#         cm = controller.Member_Controller()
#         cmc= cm.cookie_email
#         club_select = self.member_model.get_club_admin_select_one_model(clubid,cmc["email"])
#         if bool(club_select):
#             d = domain.ClubDomain(clubid,clubadmin,intro)
#             print("update clubid", d.club_id, clubid_up)
#             result = self.member_model.update_club_model(d,clubid_up)
#             if result == 1:
                
#                 self.cv.club_update_message()
#             else:
#                 self.cv.club_update_cancle_message()
#         else:
#             self.cv.club_do_not_exist()

#     # 클럽 조회
#     def club_select_all_controller(self,email):
#         print("클럽조회",email)
#         result = self.member_model.select_all_club_model(email)
#         print("클럽조회 result",result)
#         club_list = []
#         for index, value in enumerate(result):
#             club_list.append(value["clubid"])
#         print("클럽 조회 CLUB_LIST",club_list)
#         return club_list

#     # 클럽 삭제
#     def club_delete_controller(self,clubid):
#         print("클럽삭제 Controller",clubid)
#         result = self.member_model.delete_club_model(clubid)
#         if result == 1:
#             self.cv.club_delete_message()
#         else:
#             self.cv.club_delete_cancle_message()
        

#     # 클럽 가입 폼 열기
#     def club_join_form_controller(self):
#         # 존재하는 클럽 조회
#         cmc = controller.Member_Controller.cookie_email
#         if bool(cmc):
#             # 모든 클럽 가져오기
#             result = self.member_model.my_club_except_model(cmc["email"])
#             print("클럽가입폼 Controller",result)
#             club_list = []
#             for index, value in enumerate(result):
#                 club_list.append(value)
#             return club_list
#         else:
#             pass
    
#     # 클럽 가입
#     def club_join_controller(self,clubid):
#         cmc = controller.Member_Controller.cookie_email
#         # 유저 확인
#         result = self.member_model.member_select_one(cmc["email"])
#         print("클럽 가입")
#         join_club_result = self.member_model.club_join_confirm_model(clubid,result["email"])
#         print("가입한 클럽 내역 뽑아오기",join_club_result)
#         if not bool(join_club_result):
#             print("클럽가입 Bool")
#             result_info = self.member_model.club_join_model(clubid,cmc["email"],result["name"])
#             if result_info:
#                 self.cv.club_join_message()
#             else:
#                 self.cv.club_join_fale_message()
#         else:
#             self.cv.club_join_fale1_message()

#     # 내가 가입한 클럽 조회
#     def join_club_list(self):
#         print("내가 가입한 클럽 조회 진입")
#         cmc = controller.Member_Controller.cookie_email
#         result = self.member_model.join_club_select_all(cmc["email"])
#         print("내가 가입한 클럽 조회 후")
#         if bool(result):
#             club_list = []
#             for index, value in enumerate(result):
#                 club_list.append(value)
#             return club_list
#         else:
#             self.cv.club_secession_fale_message()

    
#      # 클럽 탈퇴
#     def club_secession(self,clubid,email):
#         cmc = controller.Member_Controller.cookie_email
#         if self.member_model.delete_join_mode(clubid,email):
#             self.cv.club_secession_message()
#         else:
#             self.cv.club_secession_fale_message()
    

#     # 입력값으로 클럽 리스트 가져오기
#     def club_search_list(self,input_clubid):
#         print("입력값으로 클럽 리스트 가져오기 input_clubid",input_clubid)
#         result = self.member_model.club_search_list_model(input_clubid)
#         print("클럽리스트 Controller",result)
#         club_list = []
#         if bool(result):
#             for index, value in enumerate(result):
#                 club_list.append(value)
#             return club_list
#         else:
#             print("클럽리스트 못가져옴")
        
#     # 클럽 조회버튼 리스트 출력
#     def club_search_list_controller(self):
#         # 존재하는 클럽 조회
#         result = self.member_model.select_all_club()
#         print("클럽 조회버튼 리스트 출력 Controller",result)
#         club_list = []
#         for index, value in enumerate(result):
#             print("클럽 조회버튼 리스트 출력 enumerate")
#             club_list.append(value)
#         print("클럽 조회 CLUB_LIST",club_list)
#         return club_list

#    # 내 클럽 회원 리스트
#     def club_user_select(self,clubid,email):
#         print("내 클럽 회원 리스트")
#         result = self.member_model.my_club_search_list_model(clubid,email)
#         print("내 클럽 회원 리스트 클럽 조회",result)
#         if bool(result):
#             club_list = []
#             print("내 클럽 회원 리스트 클럽 조회 CLUB_LIST",club_list)
#             user_list = self.member_model.my_club_user_list_model(clubid)
#             if bool(user_list):
#                 for index, value in enumerate(user_list):
#                     club_list.append(value)
#                 return club_list
#             else:
#                 self.cv.my_club_user_none()
#         else:
#             self.cv.my_club_user_list_message()





    
        
