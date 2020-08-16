from resAPI import MemberStore
import domain
class Member_Model:

    def __init__(self):
        self.ms = MemberStore()

    # 이메일, 패스워드 확인
    def login_clear(self,email,passwd):
        result = self.ms.login_ok(email,passwd)
        if not bool(result):
            return 1
        else:
            return 0

    # 이메일 유효성 검사
    def email_Validation_model(self,email):
        return self.ms.email_Validation(email)

    # 멤버 등록
    def insert_member_model(self,entity):
        print("멤버등록",entity)
        return self.ms.insert_member(entity)

    # 멤버 정보
    def member_select_one(self,email):
        return self.ms.select_one_member(email)
        
    # 로그인 멤버 확인
    def get_select_one_model(self,email,passwd):
        return self.ms.login_ok(email,passwd)

    # 멤버 정보 수정
    def update_member_info(self,email,passwd,nickname,phonenumber,address):
        return self.ms.update_member(email,passwd,nickname,phonenumber,address)
    
    # 멤버 탈퇴
    def delete_member_model(self,email):
        return self.ms.delete_member(email)

    # 클럽 생성
    def create_club_model(self,entity):
        print("클럽생성 entity는 ?", entity.club_id)
        self.ms.create_club(entity)

    # 클럽 조회
    def select_club_model(self,email):
        return self.ms.get_club_select_one(email)
    
    # 클럽수정 검증
    def get_club_admin_select_one_model(self,clubid,email):
        return self.ms.get_club_admin_select_one(clubid,email)
        
    # 내가만든 전체 클럽 조회
    def select_all_club_model(self,email):
        return self.ms.get_club_select_all(email)
    
    # 전체 클럽 조회
    def select_all_club(self):
        return self.ms.get_all_club_select()
    
    # 내가 생성한 클럽 제외한 클럽 조회 
    def my_club_except_model(self,email):
        return self.ms.my_club_except(email)
    # 내가 가입한 클럽 조회
    def join_club_select_all(self,email):
        return self.ms.get_all_club_join(email)

    # 클럽 수정
    def update_club_model(self,entity,clubid_up):
        return self.ms.update_club(entity,clubid_up)

    # 클럽 삭제
    def delete_club_model(self,clubid):
        return self.ms.drop_club(clubid)

    # 클럽 탈퇴
    def delete_join_mode(self,clubid,email):
        return self.ms.delete_join_club_store(clubid,email)

    # 회원탈퇴 클럽멤버십 삭제 
    def drop_clubmembership_model(self,email):
        return self.ms.delete_all_club_membership(email)

    # 생성한 클럽 전체 탈퇴
    def drop_travelclub_model(self,email):
        return self.ms.drop_club_all(email)

    # 클럽 가입
    def club_join_model(self,clubid,email,name):
        return self.ms.join_club(clubid,email,name)

    # 클럽 가입 여부
    def club_join_confirm_model(self,clubid,email):
        return self.ms.join_club_Confirm(clubid,email)

    # 문자열로 클럽 조회
    def club_search_list_model(self,input_clubid):
        return self.ms.get_search_list(input_clubid)
    
    # 클럽 아이디 입력후 내 클럽 확인
    def my_club_search_list_model(self,clubid,email):
        return self.ms.my_club_search_list_sotre(clubid,email)
    
    # 내 클럽 회원 조회
    def my_club_user_list_model(self,clubid):
        return self.ms.club_user_list(clubid)