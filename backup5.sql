create database club default character set 'utf8';
use club;
drop table member;
drop table clubmembership;
drop table travelclub;

create table member(
	email varchar(50) primary key,
	passwd varchar(15) not null,
	name varchar(30) not null,
	nickname varchar(30) not null,
	phonenumber varchar(13) not null,
	birthday varchar(14) not null,
	address varchar(100) not null
);

create table travelclub(
	clubid varchar(50) primary key,
	c_email varchar(50) not null,
	intro varchar(1000)
);
create table clubmembership(
	clubid varchar(50) not null,
	m_email varchar(50) not null,
	m_name varchar(30) not null
);

alter table travelclub add constraint fn_email_update foreign key(c_email) references member(email) on update cascade on delete cascade;
alter table clubmembership add constraint fn_clubid_update foreign key(clubid) references travelclub(clubid) on update cascade on delete cascade;
alter table clubmembership add constraint fn_m_email foreign key(m_email) references member(email) on update cascade on delete cascade;

-- alter table travelclub drop foreign key fn_email_update;

/* member */
insert into member values('Irelia@naver.com','1q2w3e','Irelia','Irelia','010-2011-0001','090625-2000000','서울특별시 중구');
insert into member values('Nami@naver.com','1q2w3e','Nami','Nami','010-2011-0002','090625-2000001','경기도 광주시 ');
insert into member values('Evelynn@naver.com','1q2w3e','Evelynn','Evelynn','010-2011-0003','090625-2000002','경기도 성남시');
insert into member values('LeBlanc@naver.com','1q2w3e','LeBlanc','LeBlanc','010-2011-0004','090625-2000003','인천광역시 중구 ');
insert into member values('Riven@naver.com','1q2w3e','Riven','Riven','010-2011-0005','090625-2000004','전라남도 무안군');
insert into member values('MissFortune@naver.com','1q2w3e','MissFortune','MissFortune','010-2011-0006','090625-2000005','강원도 춘천시');
insert into member values('Quinn@naver.com','1q2w3e','Quinn','Quinn','010-2011-0007','090625-2000006','서울특별시 동작구');
insert into member values('Ashe@naver.com','1q2w3e','Ashe','Ashe','010-2011-0008','090625-2000007','경기도 수원시');
/* travelclub */
insert into travelclub values('Irelia','Irelia@naver.com','Irelia');
insert into travelclub values('Nami','Nami@naver.com','Nami');
insert into travelclub values('Evelynn','Evelynn@naver.com','Evelynn');
insert into travelclub values('Riven','Riven@naver.com','Riven');
insert into travelclub values('MissFortune','MissFortune@naver.com','MissFortune');
insert into travelclub values('Quinn','Quinn@naver.com','Quinn');
insert into travelclub values('Ashe','Ashe@naver.com','Ashe');
insert into travelclub values('LeBlanc','LeBlanc@naver.com','LeBlanc');

/*clubmembership*/ 
insert into clubmembership values('Nami','Irelia@naver.com','Irelia');
insert into clubmembership values('Nami','Evelynn@naver.com','Evelynn');
insert into clubmembership values('Nami','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('Nami','Riven@naver.com','Riven');
insert into clubmembership values('Nami','MissFortune@naver.com','MissFortune');
insert into clubmembership values('Nami','Quinn@naver.com','Quinn');
insert into clubmembership values('Nami','Ashe@naver.com','Ashe');

insert into clubmembership values('Evelynn','Nami@naver.com','Nami');
insert into clubmembership values('Evelynn','Irelia@naver.com','Irelia');
insert into clubmembership values('Evelynn','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('Evelynn','Riven@naver.com','Riven');
insert into clubmembership values('Evelynn','MissFortune@naver.com','MissFortune');
insert into clubmembership values('Evelynn','Quinn@naver.com','Quinn');
insert into clubmembership values('Evelynn','Ashe@naver.com','Ashe');

insert into clubmembership values('LeBlanc','Nami@naver.com','Nami');
insert into clubmembership values('LeBlanc','Evelynn@naver.com','Evelynn');
insert into clubmembership values('LeBlanc','Irelia@naver.com','Irelia');
insert into clubmembership values('LeBlanc','Riven@naver.com','Riven');
insert into clubmembership values('LeBlanc','MissFortune@naver.com','MissFortune');
insert into clubmembership values('LeBlanc','Quinn@naver.com','Quinn');
insert into clubmembership values('LeBlanc','Ashe@naver.com','Ashe');

insert into clubmembership values('Riven','Nami@naver.com','Nami');
insert into clubmembership values('Riven','Evelynn@naver.com','Evelynn');
insert into clubmembership values('Riven','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('Riven','Irelia@naver.com','Irelia');
insert into clubmembership values('Riven','MissFortune@naver.com','MissFortune');
insert into clubmembership values('Riven','Quinn@naver.com','Quinn');
insert into clubmembership values('Riven','Ashe@naver.com','Ashe');

insert into clubmembership values('MissFortune','Nami@naver.com','Nami');
insert into clubmembership values('MissFortune','Evelynn@naver.com','Evelynn');
insert into clubmembership values('MissFortune','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('MissFortune','Riven@naver.com','Riven');
insert into clubmembership values('MissFortune','Irelia@naver.com','Irelia');
insert into clubmembership values('MissFortune','Quinn@naver.com','Quinn');
insert into clubmembership values('MissFortune','Ashe@naver.com','Ashe');

insert into clubmembership values('Quinn','Nami@naver.com','Nami');
insert into clubmembership values('Quinn','Evelynn@naver.com','Evelynn');
insert into clubmembership values('Quinn','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('Quinn','Riven@naver.com','Riven');
insert into clubmembership values('Quinn','MissFortune@naver.com','MissFortune');
insert into clubmembership values('Quinn','Irelia@naver.com','Irelia');
insert into clubmembership values('Quinn','Ashe@naver.com','Ashe');

insert into clubmembership values('Ashe','Nami@naver.com','Nami');
insert into clubmembership values('Ashe','Evelynn@naver.com','Evelynn');
insert into clubmembership values('Ashe','LeBlanc@naver.com','LeBlanc');
insert into clubmembership values('Ashe','Riven@naver.com','Riven');
insert into clubmembership values('Ashe','MissFortune@naver.com','MissFortune');
insert into clubmembership values('Ashe','Quinn@naver.com','Quinn');
insert into clubmembership values('Ashe','Irelia@naver.com','Irelia');

commit;
select * from member;
delete from member where name = 'Garan';
select * from travelclub;
select * from clubmembership;



