import pymysql.cursors
from domain import MemberDomain as dm

class MemberStore:
    con = None
    def __init__(self):
        MemberStore.con = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='aiadmin',
                                    password='password',
                                    db='club',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor) 

    # 연결 끊기
    def close(self):
        MemberStore.con.close()

    # 이메일, 패스워드 확인
    def login_ok(self,email,passwd):
        try:
            with MemberStore.con.cursor() as cursor:
                if bool(email) and bool(passwd):
                    sql = "select `email` from `member` where `email`=%s and `passwd`=%s"
                    cursor.execute(sql,(email,passwd))
                    result = cursor.fetchone()
        finally:
            pass
        return result
    
    # 이메일 검증
    def email_Validation(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                if bool(email):
                    print("이메일검증 sql문 위",email)
                    sql = "select `email` from `member` where `email`=%s"
                    cursor.execute(sql,email)
                    result = cursor.fetchone()
                print("이메일검증 result",result)
                return result
        finally:
            pass
        
    # # 패스워드 확인
    # def passwd_ok(self,u_passwd):
    #     try:
    #         with dm.con.cursor() as cursor:
    #             sql = "select `passwd` from `member` where `passwd`=%s"
    #             cursor.execute(sql)
    #             result = cursor.fetchone()
    #     finally:
    #         pass
    #     return result

    # 유저 등록
    def insert_member(self,entity):
        try:
            with MemberStore.con.cursor() as cursor:
                print("store",entity.u_email)
                sql = "insert into `member` (`email`,`passwd`,`name`,`nickname`,`phonenumber`,`birthday`,`address`) values (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (entity.u_email, entity.u_passwd, entity.u_name, entity.u_nick_name, entity.u_phone_number, entity.u_birthday, entity.u_address))
                MemberStore.con.commit()
                return True
        finally:
            pass
    # 유저 수정
    def update_member(self,email,passwd,nickname,phonenumber,address):
        print("유저 수정",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "update `member` set `passwd`=%s, `nickname`=%s, `phonenumber`=%s, `address`=%s where `email`=%s"
                cursor.execute(sql, (passwd, nickname, phonenumber, address, email))
                MemberStore.con.commit()
        finally:
            pass
        return 1
    # 유저 탈퇴
    def delete_member(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `member` where `email`=%s"
                cursor.execute(sql,email)
                MemberStore.con.commit()
        finally:
            pass
        return 1

    # 유저 정보
    def select_one_member(self,email):
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `member` where `email`=%s"
                cursor.execute(sql,(email))
                result = cursor.fetchone()
        finally:
            pass
        return result
    

    # 클럽 생성
    def create_club(self,entity):
        print("클럽생성은?",entity.club_id)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "insert into `travelclub` values (%s,%s,%s)"
                cursor.execute(sql,(entity.club_id,entity.m_email,entity.intro))
                MemberStore.con.commit()
        finally:
            pass
        
    # 내 클럽
    def get_club_select_one(self,email):
        print("클럽 조회?",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where `c_email`=%s "
                cursor.execute(sql,email)
                result = cursor.fetchone()
                print("클럽조회 STORE",result)
        finally:
            pass
        return result
    
    # 클럽수정 검증
    def get_club_admin_select_one(self,clubid,email):
        print("클럽 수정 검증")
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where `clubid`=%s and `c_email`=%s"
                cursor.execute(sql,(clubid,email))
                result = cursor.fetchall()
                print("클럽 수정 검증 result",result)
        finally:
            pass
        return result

    # 내가 만든 전체 클럽
    def get_club_select_all(self,email):
        print("내가 만든 전체 클럽 STORE",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where `c_email`=%s"
                cursor.execute(sql,email)
                result = cursor.fetchall()
                print("내가만든 전체 클럽 RESULT",result)
        finally:
            pass
        return result

    # 멤버가 생성한 전체 클럽 조회
    def get_all_club_select(self):
        print("전체 클럽 조회")
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub`"
                cursor.execute(sql)
                result = cursor.fetchall()
                
        finally:
            pass
        return result
    

    # 가입한 클럽 전체 조회
    def get_all_club_join(self,email):
        print("가입 클럽 전체 조회",email)
        try:
            with MemberStore.con.cursor() as cursor:
                # sql = "select * from `clubmembership` where `m_email`=%s"
                sql = """
                select * from travelclub t 
                where t.clubid in (select c2.clubid from clubmembership c2 where `m_email` = %s)
                """
                cursor.execute(sql, email)
                result = cursor.fetchall()
                print("가입 클럽 전체 조회",result)
        finally:
            pass
        return result
    
    # 가입한 클럽 삭제
    def delete_join_club_store(self,clubid,email):
        print("가입한 클럽 삭제",clubid)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `clubmembership` where `clubid`=%s and `m_email`=%s"
                cursor.execute(sql,(clubid,email))
                MemberStore.con.commit()
        finally:
            pass
        return True

    # 문자열이 포함된 클럽 조회
    def get_search_list(self,input_clubid):
        print("문자열이 포함된 클럽 조회")
        print("문자열이 포함된 클럽 조회 input_clubid", input_clubid)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where `clubid` like %s"
                cursor.execute(sql,('%'+input_clubid+'%',))
                result = cursor.fetchall()
                print("문자열이 포함된 클럽 조회 result", result)
        finally:
            pass
        return result
    # 클럽 수정
    def update_club(self,entity,clubid_up):
        print("클럽 수정 Store",entity.club_id)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "update `travelclub` set `clubid`=%s, `intro`=%s where `clubid`=%s and `c_email`=%s"
                cursor.execute(sql,(clubid_up,entity.intro,entity.club_id,entity.m_email))
                MemberStore.con.commit()
                return 1
        finally:
            pass
        
    # 클럽 삭제
    def drop_club(self,clubid):
        print("클럽삭제 Store",clubid)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `travelclub` where `clubid`=%s"
                cursor.execute(sql,clubid)
                MemberStore.con.commit()
        finally:
            pass
        return 1

    # 클럽 가입
    def join_club(self,clubid,email,name):
        print("클럽 가입 Store",clubid)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "insert into `clubmembership` (`clubid`,`m_email`,`m_name`) values(%s,%s,%s)"
                cursor.execute(sql,(clubid,email,name))
                MemberStore.con.commit()
        finally:
            pass
        return True
    
    # 클럽 가입 여부
    def join_club_Confirm(self,clubid,email):
        print("클럽가입여부 Store",clubid)
        print("클럽가입여부 Store",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `clubmembership` where `clubid`=%s and `m_email`=%s"
                cursor.execute(sql,(clubid,email))
                result = cursor.fetchall()
                print("클럽가입여부 result",result)
        finally:
            pass
        return result
    # 클럽 전체 삭제
    def drop_club_all(self,email):
        print("클럽 전체 삭제",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `travelclub` where `c_email`=%s"
                cursor.execute(sql,email)
                MemberStore.con.commit()
        finally:
            pass
        return 1

    # 클럽 멤버쉽 전체 탈퇴
    def delete_all_club_membership(self,email):
        print("클럽 탈퇴 sotre",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "delete from `clubmembership` where `m_email`=%s"
                cursor.execute(sql, email)
                MemberStore.con.commit()
        finally:
            pass
        return 1

    # 내 클럽 아이디로 내 클럽 조회
    def my_club_search_list_sotre(self,clubid,email):
        print("내 클럽 아이디로 내 클럽 조회",clubid)
        print("내 클럽 아이디로 내 클럽 조회",email)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where `clubid`=%s and `c_email`=%s"
                cursor.execute(sql,(clubid,email))
                result = cursor.fetchall()
                print("내 클럽 아이디로 내 클럽 조회",result)
        finally:
            pass
        return result

    # 내가 생성한 클럽 제외한 목록 뿌리기
    def my_club_except(self,email):
        print("내가 생성한 클럽 제외한 목록 뿌리기")
        try:
            with MemberStore.con.cursor() as cursor:
                sql = "select * from `travelclub` where not `c_email` = %s"
                cursor.execute(sql, email)
                result = cursor.fetchall()
                print("내가 생성한 클럽 재회한 목록 뿌리기 result",result)
        finally:
            pass
        return result

    # 내 클럽 가입 회원
    def club_user_list(self,clubid):
        print("내 클럽 가입 회원",clubid)
        try:
            with MemberStore.con.cursor() as cursor:
                sql = """
                select `name`,`email`,`phonenumber` from member m, 
                (select c.m_email from `travelclub` t, `clubmembership` c where t.clubid = c.clubid and t.clubid like %s and c.clubid like %s) p 
                where m.email = p.m_email"""
                cursor.execute(sql,('%'+clubid+'%','%'+clubid+'%',))
                result = cursor.fetchall()
        finally:
            pass
        return result
    
    # # 문자열이 포함된 내가 만든 클럽
    # def my_club_list(self,clubid,email):
    #     print("문자열 포함된 내가 만든 클럽",email)
    #     try:
    #         with MemberStore.con.cursor() as cursor:
    #             sql = "select * from `travelclub` where `clubid` like %s and `c_email`=%s"
    #             cursor.execute(sql,('%'+clubid+'%',email))
    #             result = cursor.fetchall()
    #             print("문자열 포함된 내가만든 클럽 result",result)
    #     finally:
    #         pass
    #     return result