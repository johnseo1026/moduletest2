import tkinter
import tkinter.font as tkfont   
import tkinter.messagebox
import tkinter.ttk
from domain import MemberDomain
import controller
import model
import re

class ViewInit:
    def __init__(self,window):
        window.geometry("500x400")
        self.frame = tkinter.Frame(window, width=500,height=400)
        self.frame.pack()
        
        # self.frame1 = tkinter.Frame(window)
        # self.frame1.pack()
        # self.frame2 = tkinter.Frame(window)
        # self.frame2.pack()
        # self.frame3 = tkinter.Frame(window)
        # self.frame3.pack()
        

class MemberView:
    
    def __init__(self,window):
        self.view = ViewInit(window)
        
    # 메인 화면 큰제목
    def main_title(self):
        self.h1 = tkinter.Label(self.view.frame, text="Travel Club Manager", font="bold",height=7,bg="#FFE4C4", relief="solid",width=480 )
        self.h1.pack()

class SignInView:
    def __init__(self,window):
        self.view = ViewInit(window)
        
   
    # 로그인 버튼
    def sign_in_button(self,window):
        print("로그인") 
        signin = tkinter.Button(self.view.frame, text="로그인", command= lambda : self.input_login_info(window))
        signin.grid(row=1,column=0)

    # 로그인할 때 입력 정보
    def input_login_info(self,window):
        print("로그인할 때 입력 정보")
        self.toplevel = tkinter.Toplevel(window)
        self.toplevel.geometry("300x100")
        self.l_email = tkinter.Label(self.toplevel, text="이메일")
        self.e_email = tkinter.Entry(self.toplevel)
        self.l_passwd = tkinter.Label(self.toplevel, text="패스워드")
        self.e_passwd = tkinter.Entry(self.toplevel)
        self.ok_button = tkinter.Button(self.toplevel, text="확인", command=self.is_exist_view)
        self.l_email.grid(row=0,column=0)
        self.e_email.grid(row=0,column=1)
        self.l_passwd.grid(row=1,column=0)
        self.e_passwd.grid(row=1,column=1)
        self.ok_button.grid(row=2,column=1)
    
    # 로그인 정보 검증
    def is_exist_view(self):
        print("로그인 정보 검증")
        self.mc = controller.Member_Controller()
        # self.e = self.e_email.get()
        # self.p = self.e_passwd.get()
        self.mc.sign_in_info(self.e_email.get(),self.e_passwd.get())
        self.toplevel.destroy()
    
    # 로그인 성공
    def login_success(self):
        tkinter.messagebox.showinfo("로그인","로그인 성공") 
    # 로그인 실패
    def login_false(self):
        tkinter.messagebox.showwarning("로그인","입력하신 정보와 일치하는 회원이 없습니다. 다시 입력해주세요.") 
    
    

class SignUpView:
    def __init__(self,window):
        self.view = ViewInit(window)
    
    # 회원가입 버튼
    def sign_up_button(self,window):
        print("회원가입")
        signup = tkinter.Button(self.view.frame, text="회원가입", command= lambda : self.input_entity(window))
        signup.grid(row=1,column=1)

    # 회원가입할 때 입력 정보
    def input_entity(self,window):
        print("회원가입할 때 입력 정보")
        self.toplevel = tkinter.Toplevel(window)
        self.toplevel.geometry("600x200")
        self.l_email = tkinter.Label(self.toplevel, text="이메일: ")
        self.l_email.grid(row=0,column=0)
        self.e_email = tkinter.Entry(self.toplevel)
        self.e_email.grid(row=0,column=1)
        self.l_email1 = tkinter.Label(self.toplevel, text="@")
        self.l_email1.grid(row=0,column=2)
        self.e_email1 = tkinter.Entry(self.toplevel)
        self.e_email1.grid(row=0,column=3)

        self.l_passwd = tkinter.Label(self.toplevel, text="패스워드: ")
        self.l_passwd.grid(row=1,column=0)
        self.e_passwd = tkinter.Entry(self.toplevel)
        self.e_passwd.grid(row=1,column=1)

        self.l_name = tkinter.Label(self.toplevel, text="이름: ")
        self.l_name.grid(row=2,column=0)
        self.e_name = tkinter.Entry(self.toplevel)
        self.e_name.grid(row=2,column=1)

        self.l_nick_name = tkinter.Label(self.toplevel, text="닉네임: ")
        self.l_nick_name.grid(row=3,column=0)
        self.e_nick_name = tkinter.Entry(self.toplevel)
        self.e_nick_name.grid(row=3,column=1)

        self.l_phone_number = tkinter.Label(self.toplevel, text="전화번호: ")
        self.l_phone_number.grid(row=4,column=0)
        self.e_phone_number = tkinter.Entry(self.toplevel)
        self.e_phone_number.grid(row=4,column=1)
        self.l_phone_number1 = tkinter.Label(self.toplevel, text="-")
        self.l_phone_number1.grid(row=4,column=2)
        self.e_phone_number1 = tkinter.Entry(self.toplevel)
        self.e_phone_number1.grid(row=4,column=3)
        self.l_phone_number2 = tkinter.Label(self.toplevel,text="-")
        self.l_phone_number2.grid(row=4,column=4)
        self.e_phone_number2 = tkinter.Entry(self.toplevel)
        self.e_phone_number2.grid(row=4,column=5)

        self.l_birth_day = tkinter.Label(self.toplevel, text="생년월일: ")
        self.l_birth_day.grid(row=5,column=0)
        self.e_birth_day = tkinter.Entry(self.toplevel)
        self.e_birth_day.grid(row=5,column=1)
        self.l_birth_day1 = tkinter.Label(self.toplevel,text="-")
        self.l_birth_day1.grid(row=5,column=2)
        self.e_birth_day1 = tkinter.Entry(self.toplevel)
        self.e_birth_day1.grid(row=5,column=3)

        self.l_address = tkinter.Label(self.toplevel, text="거주지: ")
        self.l_address.grid(row=6,column=0)
        self.e_address = tkinter.Entry(self.toplevel)
        self.e_address.grid(row=6,column=1)

        self.ok_button = tkinter.Button(self.toplevel, text="확인",command = self.insert_ok, width=10)
        self.ok_button.grid(row=7,column=0)
        self.cancle_button = tkinter.Button(self.toplevel, text="취소", command= self.insert_cancle,width=10)
        self.cancle_button.grid(row=7,column=1, sticky="w")


    # 확인버튼
    def insert_ok(self):
        num = 0
         # 이메일 정규 표현식
        self.email_re = re.compile('^[a-zA-Z0-9+-_.]')
        self.email_match = self.email_re.match(self.e_email.get())
        self.email1_re = re.compile('[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')
        self.email1_match = self.email1_re.match(self.e_email1.get())

        # 전화번호 정규 표현식
        self.phone_re = re.compile('010')#'\\d{3}'
        self.phone_match = self.phone_re.match(self.e_phone_number.get())
        self.phone1_re = re.compile('\\d{4}')
        self.phone1_match = self.phone1_re.match(self.e_phone_number1.get())
        self.phone2_re = re.compile('\\d{4}')
        self.phone2_match = self.phone2_re.match(self.e_phone_number2.get())

        # 생일 정규 표현식
        self.birth_day_re = re.compile('\\d{6}')
        self.birth_day_match = self.birth_day_re.match(self.e_birth_day.get())
        self.birty_day1_re = re.compile('\\d{7}')
        self.birth_day1_match = self.birty_day1_re.match(self.e_birth_day1.get())

        if bool(self.email_match) and bool(self.email1_match):
            num += 1
            email_result = self.e_email.get()+'@'+self.e_email1.get()
            print(email_result)
        if bool(self.phone_match) and bool(self.phone1_match) and bool(self.phone2_match):
            num += 10
            phone_result = self.e_phone_number.get()+'-'+self.e_phone_number1.get()+'-'+self.e_phone_number2.get()
            print(phone_result)
        if bool(self.birth_day_match) and bool(self.birth_day1_match):
            num += 20
            birth_day_result = self.e_birth_day.get()+'-'+self.e_birth_day1.get()
            print(birth_day_result)
   
        print("확인버튼")
        if num == 31:
            self.mc = controller.Member_Controller()
            num = 0
            # self.mc.sign_up_info(self.e_email.get(),self.e_passwd.get(),self.e_name.get(),self.e_nick_name.get(),self.e_phone_number.get(),self.e_birth_day.get(),self.e_address.get())
            self.mc.sign_up_info(email_result,self.e_passwd.get(),self.e_name.get(),self.e_nick_name.get(),phone_result,birth_day_result,self.e_address.get())
        elif num == 1:
            tkinter.messagebox.showwarning("정규표현식","전화번호,생년월일과 나머지 정보를 다시 입력하세요.")
        elif num == 11:
            tkinter.messagebox.showwarning("정규표현식","생년월일과 나머지 정보를 입력하세요.")
        elif num == 21:
            tkinter.messagebox.showwarning("정규표현식","전화번호와 나머지 정보를 입력하세요.")
        elif num == 30:
            tkinter.messagebox.showwarning("정규표현식","이메일과 나머지 정보를 다시 입력하세요.")
        else:
            tkinter.messagebox.showwarning("정규표현식","정보를 모두  입력하세요.")


       
    # 취소버튼
    def insert_cancle(self):
        
        self.toplevel.destroy()
    
    # 회원가입 성공
    def sign_up_success(self):
        tkinter.messagebox.showinfo("회원가입","회원가입 성공")
        # self.toplevel.destroy()   

    # 회원가입 실패
    def sign_up_false(self):
        tkinter.messagebox.showwarning("회원가입","이미 존재하는 회원입니다.")
        # self.toplevel.destroy()

class UpdateMember:
    def __init__(self,window):
        self.view = ViewInit(window)
    
    # 마이페이지 버튼
    def mypage_button(self,window):
        self.update_button = tkinter.Button(self.view.frame,text="마이페이지", command=lambda : self.update_info(window))
        self.update_button.grid(row=1,column=2)

    # 로그아웃 버튼
    def log_out_button(self,window):
        self.logout_button = tkinter.Button(self.view.frame,text="로그아웃", command=self.log_out)
        self.logout_button.grid(row=1,column=3)

    # 로그아웃
    def log_out(self):
        cm = controller.Member_Controller()
        cmc = controller.Member_Controller.cookie_email
        if bool(cmc):
            cm.delete_cookie()
            tkinter.messagebox.showinfo("TravelClub","로그아웃 완료")
        else:
            tkinter.messagebox.showwarning("TravelClub","로그인이 되어있지 않습니다.")

        

    # 마이페이지 정보
    def update_info(self,window):
        cm = controller.Member_Controller()
        cmc = controller.Member_Controller.cookie_email
        if bool(cmc):
            result = cm.detail_member_info()
            print("result",result)
            self.toplevel = tkinter.Toplevel(window)
            self.toplevel.geometry("300x250")
            self.l_email = tkinter.Label(self.toplevel, text="이메일: ")
            self.e_email = tkinter.Entry(self.toplevel)
            self.l_passwd = tkinter.Label(self.toplevel, text="패스워드: ")
            self.e_passwd = tkinter.Entry(self.toplevel)
            self.l_name = tkinter.Label(self.toplevel, text="이름: ")
            self.e_name = tkinter.Entry(self.toplevel)
            self.l_nick_name = tkinter.Label(self.toplevel, text="닉네임: ")
            self.e_nick_name = tkinter.Entry(self.toplevel)
            self.l_phone_number = tkinter.Label(self.toplevel, text="전화번호: ")
            self.e_phone_number = tkinter.Entry(self.toplevel)
            self.l_birth_day = tkinter.Label(self.toplevel, text="생년월일: ")
            self.e_birth_day = tkinter.Entry(self.toplevel)
            self.l_address = tkinter.Label(self.toplevel, text="거주지: ")
            self.e_address = tkinter.Entry(self.toplevel)
            self.l_clubid = tkinter.Label(self.toplevel, text="가입한 클럽: ")
            self.e_clubid = tkinter.Entry(self.toplevel)
            
            self.ok_button = tkinter.Button(self.toplevel, text="수정", command = self.my_update_button ,width=10)
            self.cancle_button = tkinter.Button(self.toplevel, text="취소", command=self.cancle_func ,width=10)
            
            self.l_email.grid(row=0,column=0)
            self.e_email.grid(row=0,column=1)
            self.l_passwd.grid(row=1,column=0)
            self.e_passwd.grid(row=1,column=1)
            self.l_name.grid(row=2,column=0)
            self.e_name.grid(row=2,column=1)
            self.l_nick_name.grid(row=3,column=0)
            self.e_nick_name.grid(row=3,column=1)
            self.l_phone_number.grid(row=4,column=0)
            self.e_phone_number.grid(row=4,column=1)
            self.l_birth_day.grid(row=5,column=0)
            self.e_birth_day.grid(row=5,column=1)
            self.l_address.grid(row=6,column=0)
            self.e_address.grid(row=6,column=1)
            self.l_clubid.grid(row=7,column=0)
            self.e_clubid.grid(row=7,column=1)

            self.ok_button.grid(row=8,column=0, sticky="w")
            self.cancle_button.grid(row=8,column=1, sticky="w")


            self.e_email.insert(0,result.u_email)
            self.e_email.configure(state="readonly")
            self.e_passwd.insert(0,result.u_passwd)
            self.e_name.insert(0,result.u_name)
            self.e_name.configure(state="readonly")
            self.e_nick_name.insert(0,result.u_nick_name)
            self.e_phone_number.insert(0,result.u_phone_number)
            self.e_birth_day.insert(0,result.u_birthday)
            self.e_birth_day.configure(state="readonly")
            self.e_address.insert(0,result.u_address)
            self.e_clubid.configure(state="readonly")
            # if not bool(result.u_clubid):
            #     self.e_clubid.configure(state="readonly")
            # else:
            #     self.e_clubid.insert(0,result.u_clubid)
            #     self.e_clubid.configure(state="readonly")
        else:
            self.login_plz()

    # 로그인 하세요
    def login_plz(self):
        tkinter.messagebox.showwarning("TravelClub","로그인 해주세요")

    # 마이페이지 수정 버튼
    def my_update_button(self):
        cm = controller.Member_Controller()
        cm.update_info_con(self.e_email.get(),self.e_passwd.get(),self.e_nick_name.get(),self.e_phone_number.get(),self.e_address.get())
    # 마이페이지 취소 버튼 
    def cancle_func(self):
        self.toplevel.destroy()

    # 마이페이지 수정 완료
    def my_update_message(self):
         tkinter.messagebox.showinfo("마이페이지","수정이 완료되었습니다.")

    login_plz
class DeleteMember:
    def __init__(self,window):
        self.view = ViewInit(window)

    # 회원 탈퇴 버튼
    def delete_member_button(self,window):
        self.member_delete_button_message = tkinter.Button(self.view.frame,text="회원탈퇴" , command=lambda : self.delete_member(window))
        self.member_delete_button_message.grid(row=1,column=4)
        
    # 회원 탈퇴 폼
    def delete_member(self,window):
        print("회원 탈퇴 폼 접근")
        cm = controller.Member_Controller()
        cmc = cm.cookie_email
        print("회원탈퇴폼 cmc",cmc)
        # toplevel = tkinter.Toplevel(window)
        if bool(cmc):
            toplevel = tkinter.Toplevel(window)
            self.delete_label = tkinter.Label(toplevel, text= "확인 버튼을 누르시면 계정이 생성한 클럽도 같이 삭제 됩니다. 정말 탈퇴하시겠습니까?")
            self.delete_button = tkinter.Button(toplevel, text="확인", command=self.delete_yn)
            self.delete_cancle_button = tkinter.Button(toplevel, text="취소", command=lambda : self.delete_cancle(toplevel))
            self.delete_label.pack()
            self.delete_button.pack()
            self.delete_cancle_button.pack()
        else:
            self.login_plz()

        # self.delete_button = tkinter.messagebox.askyesno("회원탈퇴","확인 버튼을 누르시면 계정이 생성한 클럽도 같이 삭제 됩니다. 정말 탈퇴하시겠습니까?")
        # if self.delete_button == "yes":
        #     if bool(cmc["email"]):
        #         print("회원탈퇴폼 if문")
        #         cm.delete_info_controller()
        #     else:
        #         self.login_plz()
        # else:
        #     pass
            # self.login_plz()
    # 회원탈퇴 확인 처리
    def delete_yn(self):
        cm = controller.Member_Controller()
        result = cm.delete_info_controller()
        if result == 1:
            self.drop_club_message()
        else:
            self.drop_club_fale_message()
    
    # 회원탈퇴 취소 버튼
    def delete_cancle(self,toplevel):
        toplevel.destroy()

    # 로그인 하세요
    def login_plz(self):
        tkinter.messagebox.showwarning("TravelClub","로그인 해주세요")

    # 회원탈퇴 메시지
    def drop_club_message(self):
        tkinter.messagebox.showinfo("TravelClub","회원탈퇴 완료.")
    
    # 회원탈퇴 실패 메시지
    def drop_club_fale_message(self):
        tkinter.messagebox.showinfo("TravelClub","회원탈퇴 실패.")


class ClubView:
    
    def __init__(self,window):
        self.view = ViewInit(window)

    # 클럽 버튼
    def club_button(self,window):
        print("클럽 버튼")
        club_list_button = tkinter.Button(self.view.frame, text="클럽", command=lambda : self.club_button_list(tkinter.Toplevel(window)))
        club_list_button.grid(row=1,column=5)

    # 클럽 버튼 리스트
    def club_button_list(self,window):
        # 클럽 가입 버튼
        self.club_join_button(window)
        # 클럽 생성 버튼
        self.club_create_button(window)
        # 클럽 수정 버튼
        self.club_update_button(window)
        # 클럽 삭제 버튼
        self.club_delete_button(window)
        # 클럽 리스트 조회 버튼
        self.club_search_list_button(window)
        # 클럽 탈퇴 버튼
        self.club_secession_button(window)
        # 클럽 회원 정보
        self.my_club_user_button(window)

    # 클럽 가입 버튼
    def club_join_button(self,window):
        print("클럽 가입")
        self.join_button = tkinter.Button(window,width=39, text="클럽 가입", command= lambda : self.club__join_form(window))
        self.join_button.pack()


    # 클럽 가입 폼
    def club__join_form(self,window):
        cm = controller.Member_Controller()
        cmc = controller.Member_Controller.cookie_email
        if bool(cmc):
            toplevel = tkinter.Toplevel(window)
            result = cm.club_join_form_controller()
            print("클럽가입폼 result",result)

            self.club_input = tkinter.Entry(toplevel)
            self.club_sign_btn = tkinter.Button(toplevel,text="가입",command=self.club_join, width=10)

            self.club_input.grid(row=0,column=0)
            self.club_sign_btn.grid(row=0,column=1 ,sticky="w")
            self.treeview_join = tkinter.ttk.Treeview(toplevel,columns=["클럽","소개"],displaycolumns=["클럽","소개"])
            self.treeview_join.column('#0',stretch="NO", width=0)
            self.treeview_join.heading("#0",text="index",anchor="center")
            self.treeview_join.column('#1',width=100)
            self.treeview_join.heading("#1",text="클럽",anchor="center")
            self.treeview_join.column('#2',width=100)
            self.treeview_join.heading("#2",text="소개",anchor="center")
            self.treeview_join.grid(row=1,column=0)
            
            for index in range(len(result)):
                self.treeview_join.insert('',index,values=[result[index]["clubid"],result[index]["intro"]])
        else:
            self.login_plz()

    # 클럽 가입
    def club_join(self):
        cm = controller.Member_Controller()
        cm.club_join_controller(self.club_input.get())

    # 클럽 가입 메시지
    def club_join_message(self):
        tkinter.messagebox.showinfo("TravelClub","클럽에 가입되었습니다.")
    # 클럽 에러 메시지
    def club_join_fale_message(self):
        tkinter.messagebox.showwarning("TravelClub","클럽에 가입 실패하였습니다.")
    # 클럽 에러 메시지
    def club_join_fale1_message(self):
        tkinter.messagebox.showwarning("TravelClub","이미 가입된 클럽이 있습니다.")    
    # 클럽 생성 버튼
    def club_create_button(self,window):
        print("클럽 생성")
        create_button = tkinter.Button(window,width=39, text="클럽 생성", command= lambda : self.club_create_info(window))
        create_button.pack()

    # 클럽 수정 버튼
    def club_update_button(self,window):
        print("클럽 수정")
        signin = tkinter.Button(window,width=39, text="클럽 수정", command= lambda : self.club_update_info(window))
        signin.pack()

    # 클럽 삭제 버튼
    def club_delete_button(self,window):
        print("클럽 삭제")
        signin = tkinter.Button(window,width=39, text="클럽 삭제", command= lambda : self.club_delete_info(window))
        signin.pack()

    # 클럽 생성 폼
    def club_create_info(self,window):
        cmc = controller.Member_Controller.cookie_email
        print("cmc",cmc)
        if bool(cmc):
            self.toplevel = tkinter.Toplevel(window)
            self.l_clubid = tkinter.Label(self.toplevel, text="클럽명: ")
            self.e_clubid = tkinter.Entry(self.toplevel)
            self.l_club_intro = tkinter.Label(self.toplevel, text="소개: ")
            self.e_club_intro = tkinter.Entry(self.toplevel)

            self.ok_button = tkinter.Button(self.toplevel, text="확인", command = self.club_create, width=10)
            self.cancle_button = tkinter.Button(self.toplevel, text="취소", command=self.cancle_func, width=10)

            self.l_clubid.grid(row=0,column=0)
            self.e_clubid.grid(row=0,column=1)
            self.l_club_intro.grid(row=1,column=0)
            self.e_club_intro.grid(row=1,column=1)
            self.ok_button.grid(row=0,column=2)
            self.cancle_button.grid(row=1,column=2, sticky="w")
        else:
            self.login_plz()
    
    # 로그인 하세요
    def login_plz(self):
        tkinter.messagebox.showwarning("TravelClub","로그인 해주세요")


    # 클럽 생성
    def club_create(self):
        cm  = controller.Member_Controller()
        cm.create_club(self.e_clubid.get(),self.e_club_intro.get())

    # 클럽 취소 버튼
    def cancle_func(self):
        self.toplevel.destroy()


    # 클럽 생성 완료 메시지
    def club_create_message(self):
        tkinter.messagebox.showinfo("클럽 생성","생성이 완료되었습니다.")
        

    # 클럽 생성 실패 메시지
    def club_create_fale_message(self):
        tkinter.messagebox.showwarning("클럽 생성","클럽이 존재합니다. 다시 입력해주세요.")


    # 클럽 리스트 조회 버튼
    def club_search_list_button(self,window):
        print("클럽 리스트 조회 버튼")
        self.club_list_btton = tkinter.Button(window,width=39, text="클럽조회", command= lambda : self.club_search_list(window))
        # self.signin.bind("<Button-1>", self.click_signin)
        self.club_list_btton.pack()
    
    # 클럽 조회 리스트
    def club_search_list(self,window):
        self.toplevel = tkinter.Toplevel(window)
        # toplevel.attributes("-topmost","true")
        self.club_list_entry = tkinter.Entry(self.toplevel)
        self.treeview_list = tkinter.ttk.Treeview(self.toplevel,columns=["clubid","intro"],displaycolumns=["clubid","intro"], padding=0)
        self.treeview_list.column('#0',stretch="NO",width=0)
        self.treeview_list.heading("#0",text="index", anchor="center")
        self.treeview_list.column('#1',width=100)
        self.treeview_list.heading("#1",text="클럽명", anchor="center")
        self.treeview_list.column('#2',width=100)
        self.treeview_list.heading("#2",text="소개", anchor="center")

        # self.club_listbox = tkinter.Listbox(toplevel)
        self.club_search_btn = tkinter.Button(self.toplevel,width=10,text="조회", command=lambda : self.club_search(self.club_list_entry.get()))
        self.club_cancle_btn = tkinter.Button(self.toplevel,width=10, text="닫기", command=self.toplevel.destroy)
        self.treeview_list.pack()
        self.club_list_entry.pack()
        # self.club_listbox.pack()
        self.club_search_btn.pack()
        self.club_cancle_btn.pack()
        

    # 클럽 조회
    def club_search(self,input_clubid):
        cm = controller.Member_Controller()
        if bool(input_clubid):
            result = cm.club_search_list(input_clubid)
            print("리스트 result",result)
            if bool(result):
                for i in self.treeview_list.get_children():
                    self.treeview_list.delete(i)
                for index in range(len(result)):
                    print("클럽 조회 View")
                    self.treeview_list.insert('',index,values=[result[index]["clubid"],result[index]["intro"]])
            else:
                tkinter.messagebox.showwarning("TravelClub","입력하신 클럽이 존재하지 않습니다.")
        else:
            result2 = cm.club_search_list_controller()
            print("리스트 result2",result2)
            for i in self.treeview_list.get_children():
                self.treeview_list.delete(i)
            for index in range(len(result2)):
                self.treeview_list.insert('',index,values=[result2[index]["clubid"],result2[index]["intro"]])	
        #     if bool(result):
        #         for index in range(len(result)):
        #             print("클럽조회 view")
        #             self.club_listbox.delete(index,self.club_listbox.size())
        #             self.club_listbox.insert(index,result[index])
        #     else:
        #         tkinter.messagebox.showwarning("TravelClub","입력하신 클럽이 존재하지 않습니다.")
        # else:
        #     result2 = cm.club_search_list_controller()
        #     for index in range(len(result2)):
        #         print("클럽조회2 view",index)
        #         self.club_listbox.delete(index)
        #         self.club_listbox.insert(index,result2[index])
        # self.club_listbox.configure(state="readonly")    


    # 클럽 수정
    def club_update_info(self,window):
        cm = controller.Member_Controller()
        cmc = cm.cookie_email
        if bool(cmc):
            print("cmc",cmc)
            result = cm.club_detail_controller()
            print("클럽수정 result",result[0]["clubid"])
            self.toplevel = tkinter.Toplevel(window)
            self.toplevel.geometry("500x400")
            self.l_clubid = tkinter.Label(self.toplevel, text="클럽명: ")
            self.l_clubid.grid(row=0,column=0)
            self.e_clubid = tkinter.Entry(self.toplevel)
            self.e_clubid.grid(row=0,column=1)
            self.l_clubid_up = tkinter.Label(self.toplevel, text="변경할 클럽명: ")
            self.l_clubid_up.grid(row=1,column=0)
            self.e_clubid_up = tkinter.Entry(self.toplevel)
            self.e_clubid_up.grid(row=1,column=1)
            self.l_club_admin = tkinter.Label(self.toplevel, text="관리자: ")
            self.l_club_admin.grid(row=2,column=0)
            self.e_club_admin = tkinter.Entry(self.toplevel)
            self.e_club_admin.grid(row=2,column=1)
            self.l_club_intro = tkinter.Label(self.toplevel, text="소개: ")
            self.l_club_intro.grid(row=3,column=0)
            self.e_club_intro = tkinter.Entry(self.toplevel)
            self.e_club_intro.grid(row=3,column=1)
            self.ok_button = tkinter.Button(self.toplevel, text="수정",width=10, command =lambda : self.club_update(self.e_clubid.get(),self.e_clubid_up.get(),self.e_club_admin.get(),self.e_club_intro.get()))
            self.ok_button.grid(row=4,column=0)
            self.cancle_button = tkinter.Button(self.toplevel, text="취소",width=10, command= self.cancle_func)
            self.cancle_button.grid(row=4,column=1, sticky="w")
            self.e_club_admin.insert(0,result[0]["c_email"])
            self.e_club_admin.configure(state="readonly")
            self.treeview_up = tkinter.ttk.Treeview(self.toplevel,columns=["클럽","관리자","소개"],displaycolumns=["클럽","관리자","소개"])
            self.treeview_up.column('#0', width=0, stretch="NO")
            self.treeview_up.heading("#0", text="index", anchor="center")
            self.treeview_up.column('#1', width=100)
            self.treeview_up.heading("#1", text="클럽", anchor="center")
            self.treeview_up.column('#2', width=100)
            self.treeview_up.heading("#2", text="관리자", anchor="center")
            self.treeview_up.column('#3', width=100)
            self.treeview_up.heading("#3", text="소개", anchor="center")
            self.treeview_up.grid(row=5,column=1, pady=10)
            for index in range(len(result)):
                self.treeview_up.insert('',index,values=[result[index]["clubid"],result[index]["c_email"],result[index]["intro"]])
        else:
            self.login_plz()

    # 클럽 수정 진행
    def club_update(self,clubid,club_up,admin,intro):
        cm = controller.Member_Controller()

        if bool(clubid) and bool(club_up):
            cm.club_update_controller(clubid,club_up,admin,intro)
        else:
            tkinter.messagebox.showwarning("클럽 수정","값을 입력해 주세요")

    # 클럽 수정 완료 메시지
    def club_update_message(self):
        tkinter.messagebox.showinfo("클럽 수정","수정이 완료되었습니다.")
        

    # 클럽 수정 실패 메시지
    def club_update_cancle_message(self):
        tkinter.messagebox.showwarning("클럽 수정","클럽이 존재합니다. 다른 클럽을 입력하세요.")
    
    # 클럽 수정 클럽 존재하지 않음 메시지
    def club_do_not_exist(self):
        tkinter.messagebox.showwarning("클럽 수정","입력하신 클럽이 존재하지 않습니다. 다시 입력하세요.")
    
    # 클럽 삭제 폼
    def club_delete_info(self,window):
        cm = controller.Member_Controller()
        cmc = cm.cookie_email
        if bool(cmc):
            self.toplevel = tkinter.Toplevel(window)
            result = cm.club_select_all_controller(cmc["email"])
            print("클럽 삭제 폼 RESULT", result)
            self.l_clubid = tkinter.Label(self.toplevel,text="클럽명")
            self.e_clubid = tkinter.Entry(self.toplevel)
            # self.e_club_list = tkinter.Listbox(self.toplevel)
            self.delete_button = tkinter.Button(self.toplevel, text="삭제", command = self.club_delete)
            self.cancle_button = tkinter.Button(self.toplevel, text="취소", command = self.cancle_func)

            self.l_clubid.grid(row=0,column=0)
            self.e_clubid.grid(row=0,column=1)
            # self.e_club_list.grid(row=1,column=0)
            self.delete_button.grid(row=0,column=2)
            self.cancle_button.grid(row=0,column=3, sticky="w")

            self.treeview_del = tkinter.ttk.Treeview(self.toplevel,columns=["클럽"],displaycolumns=["클럽"])
            self.treeview_del.column('#0', width=0, stretch="NO")
            self.treeview_del.heading("#0", text="index", anchor="center")
            self.treeview_del.column('#1', width=100)
            self.treeview_del.heading("#1", text="클럽", anchor="center")
            self.treeview_del.grid(row=2,column=1)
            for index in range(len(result)):
                # self.e_club_list.insert(index,result[index])
                self.treeview_del.insert('',index,values=[result[index]])

        else:
            self.login_plz()
        

    # 클럽 삭제
    def club_delete(self):
        cm = controller.Member_Controller()
        cm.club_delete_controller(self.e_clubid.get())

    # 클럽 삭제 완료 메시지
    def club_delete_message(self):
        tkinter.messagebox.showinfo("클럽 삭제","삭제가 완료되었습니다.")
        

    # 클럽 삭제 실패 메시지
    def club_delete_cancle_message(self):
        tkinter.messagebox.showwarning("클럽 삭제","클럽이 존재합니다. 다른 클럽을 입력하세요.")

    # 클럽 탈퇴 버튼
    def club_secession_button(self,window):
        self.signin = tkinter.Button(window,width=39, text="클럽 탈퇴", command= lambda : self.club_secession_form(window))
        self.signin.pack()

    # 클럽 탈퇴 폼
    def club_secession_form(self,window):
        cm = controller.Member_Controller()
        cmc = cm.cookie_email
        if bool(cmc):
            self.toplevel = tkinter.Toplevel(window)
            result = cm.join_club_list()
            print("클럽 탈퇴 폼 RESULT", result)
            self.l_clubid = tkinter.Label(self.toplevel,text="클럽명: ")
            self.e_clubid = tkinter.Entry(self.toplevel)
            self.e_club_list = tkinter.Listbox(self.toplevel)
            self.delete_button = tkinter.Button(self.toplevel, text="탈퇴", command = lambda : self.club_secession(self.e_clubid.get(),cmc["email"]))
            self.cancle_button = tkinter.Button(self.toplevel, text="취소", command = self.cancle_func)

            self.l_clubid.pack()
            self.e_clubid.pack()
            self.e_club_list.pack()
            self.delete_button.pack()
            self.cancle_button.pack()
            for index in range(len(result)):
                self.e_club_list.insert(index,result[index]["clubid"])
            pass
        else:
            self.login_plz()

        # cm = controller.Member_Controller()
        # cmc = cm.cookie_email
        # if bool(cmc):
        #     self.toplevel = tkinter.Toplevel(window)
        #     self.toplevel.geometry("400x300")
        #     result = cm.join_club_list()
        #     print("클럽 탈퇴 폼 RESULT", result)
        #     self.l_clubid = tkinter.Label(self.toplevel,text="클럽명: ")
        #     self.l_clubid.grid(row=0,column=0)
        #     self.e_clubid = tkinter.Entry(self.toplevel)
        #     self.e_clubid.grid(row=0,column=1)
        #     self.delete_button = tkinter.Button(self.toplevel,width=10 ,text="탈퇴", command = lambda : self.club_secession(self.e_clubid.get(),cmc["email"]))
        #     self.delete_button.grid(row=0,column=2, padx=5)
        #     self.cancle_button = tkinter.Button(self.toplevel,width=10 ,text="취소", command = self.cancle_func)
        #     self.cancle_button.grid(row=0,column=3,sticky="w") 
        #     self.treeview_del = tkinter.ttk.Treeview(self.toplevel,columns=["클럽","관리자","소개"],displaycolumns=["클럽","관리자","소개"])
        #     self.treeview_del.column('#0',stretch="NO", width=0)
        #     self.treeview_del.heading("#0",text="index", anchor="center")
        #     self.treeview_del.column('#1',width=100)
        #     self.treeview_del.heading("#1",text="클럽", anchor="center")
        #     self.treeview_del.column('#2',width=120)
        #     self.treeview_del.heading("#2",text="관리자", anchor="center")
        #     self.treeview_del.column('#3',width=100)
        #     self.treeview_del.heading("#3",text="소개", anchor="center")
        #     self.treeview_del.grid(row=2,column=0,padx=10, pady=20, rowspan=50)

        #     for index in range(len(result)):
        #         self.treeview_del.insert('',index,values=[result[index]["clubid"],result[index]["c_email"],result[index]["intro"]])
        # else:
        #     self.login_plz()
    
    
    # 클럽 탈퇴
    def club_secession(self,clubid,email):
        if bool(clubid):
            cm = controller.Member_Controller()
            cm.club_secession(clubid,email)
        else:
            self.valeu_message()

    # 탈퇴 완료 메시지
    def club_secession_message(self):
        tkinter.messagebox.showinfo("TravelClub","탈퇴를 완료했습니다.")
        
    # 탈퇴 실패 메시지
    def club_secession_fale_message(self):
        tkinter.messagebox.showwarning("TravelClub","정보를 정확히 입력하세요")
    
    # 값 입력 메시지
    def valeu_message(self):
        tkinter.messagebox.showwarning("TravelClub","값을 입력하세요")
    
    # 내 클럽 회원 정보 버튼
    def my_club_user_button(self,window):
        self.signin = tkinter.Button(window,width=39, text="회원 리스트", command= lambda : self.my_club_user_info(window))
        self.signin.pack()

    # 내 클럽 회원 정보
    def my_club_user_info(self,window):
        cmc = controller.Member_Controller.cookie_email
        self.toplevel = tkinter.Toplevel(window)
        if bool(cmc):
            search_labal = tkinter.Label(self.toplevel, text="클럽명")
            search_entry = tkinter.Entry(self.toplevel)
            search_button = tkinter.Button(self.toplevel,text="조회",comman=lambda : self.my_club_user_list(search_entry.get(),cmc["email"],window))
            self.treeview = tkinter.ttk.Treeview(self.toplevel,columns=["name","email","phonenumber"],displaycolumns=["name","email","phonenumber"], padding=0)
            self.treeview.column('#0',stretch="NO" ,width=0)
            self.treeview.heading("#0",text="index" , anchor="center")
            self.treeview.column('#1',width=100)
            self.treeview.heading("#1",text="이름", anchor="center")
            self.treeview.column('#2',width=100)
            self.treeview.heading("#2",text="전화번호", anchor="center")
            self.treeview.column('#3',width=100)
            self.treeview.heading("#3",text="이메일", anchor="center")
            self.treeview.pack()
            search_labal.pack()
            search_entry.pack()
            search_button.pack()
        else:
            self.login_plz()

    # 내 클럽 회원 리스트
    def my_club_user_list(self,clubid,email,window):
        cm = controller.Member_Controller()
        if bool(clubid):
            user_list = cm.club_user_select(clubid,email)
            # result = cm.club_search_list(clubid)
            print("리스트 result",user_list)
            print(self.treeview.get_children())
            if bool(user_list):
                # print("클럽조회 view {0}".format(range(len(user_list)))
                for i in self.treeview.get_children():
                        self.treeview.delete(i)
                for index in range(len(user_list)):
                    # self.club_listbox.delete(index,self.club_listbox.size())
                    # self.treeview.delete(str(index))
                    self.treeview.insert('',index,values=[user_list[index]["name"],user_list[index]["phonenumber"],user_list[index]["email"]])
        else:
            tkinter.messagebox.showwarning("TravelClub","검색란에 클럽을 입력하세요.")

    # 클럽 회원 리스트 에러 메세지
    def my_club_user_list_message(self):
        tkinter.messagebox.showinfo("Travel Club Manager","클럽명을 확인해주세요.")

    # 클럽 회원 없음 메세지
    def my_club_user_none(self):
        tkinter.messagebox.showwarning("TravelClub","유저가 없습니다.")