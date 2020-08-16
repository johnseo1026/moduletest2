const express    = require('express');
const mysql      = require('mysql');
const dbconfig   = require('./config/database.js');
const connection = mysql.createConnection(dbconfig);
const bodyParser = require('body-parser');

const app = express();
app.set('port', process.env.PORT || 8000);
app.use(bodyParser.json());


app.get('/', (req, res) => {
    var ip = req.headers['x-forwarded-for'] || 
                req.connection.remoteAddress || 
                req.socket.remoteAddress ||
            (req.connection.socket ? req.connection.socket.remoteAddress : null);
    console.log(ip);
    res.send('Hello, New World! : ' + ip + "," + new Date());
});

app.get('/health', (req, res) => {
    res.status(200).send();
});

// # 이메일, 패스워드 확인
// app.get('/users/isexist/:email:passwd', (req, res) => {
    app.get('/users/isexist', (req, res) => {
    console.log("## post request:" + req.query.email);
    console.log("## post request1:" + req.query.passwd);
    var email = req.query.email;
    var passwd = req.query.passwd;
    connection.query('select `email` from `member` where `email`=? and `passwd`=?', 
	  [email, passwd], (error, rows) => { //(error, results, fields)
    if (error) throw error;
    console.log("rows: ", rows)
    res.json(rows);
    // res.json({ok:true});
    });
});

// 이메일 검증
app.get('/users/Confirm/:email', (req, res) => {
    var email = req.query.email;
    if(email){
        connection.query('select `email` from `member` where `email`=?',
        [email], (error, rows) => {
        if (error) throw error;
        console.log('User info is: ', rows);
        res.json(rows);
        });
    }
});
// 유저 등록
app.post('/users', (req, res) => {
    console.log("Param value: ",req.body.email)
    var email = req.body.email;
    var passwd = req.body.passwd;
    var name = req.body.name;
    var nickname = req.body.nickname;
    var phonenumber = req.body.phonenumber;
    var birthday = req.body.birthday;
    var address = req.body.address;
    connection.query('insert into `member` (`email`,`passwd`,`name`,`nickname`,`phonenumber`,`birthday`,`address`) values (?,?,?,?,?,?,?)',
    [email,passwd,name,nickname,phonenumber,birthday,address], (error, rows) => {
    if (error) throw error;
    // res.json({True:True});
    res.json(rows);
    });
});

// 유저 수정
app.put('/users/update/:email', (req, res) => {
    var email = req.query.email;
    var passwd = req.body.passwd;
    var nickname = req.body.nickname;
    var phonenumber = req.body.phonenumber;
    var address = req.body.address;
    connection.query('update `member` set `passwd`=?, `nickname`=?, `phonenumber`=?, `address`=? where `email`=?', 
    [passwd,nickname,phonenumber,address,email],(error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.json({number:1});
    });
});

// 유저 탈퇴
app.delete('/users/delete/:email', (req, res) => {
    var email = req.query.email;
    connection.query('delete from `member` where `email`=?',[email], (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.json({number:1});
  });
});

// 유저 정보 (가능)
app.get('/users/info/:email', (req, res) => {
    var email = req.query.email;
    connection.query('select * from `member` where `email`=?',[email], (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.json(rows);
  });
});

// 회원탈퇴 클럽멤버십 삭제
app.delete('/users/delete/clubMembership:email',(req,res) =>{
  var email = req.query.email
  connection.query('delete from `clubmembership` where `m_email`=?',[email],(error,rows) => {
  if(error) throw error;
  console.log('User info is: ', rows);
  res.json({'number':1})
  });
}); 

// 생성한 클럽 전체 탈퇴
app.delete('/users/delete/Allclub:email',(req,res) =>{
  var email = req.query.email
  connection.query('delete from `travelclub` where `c_email`=?',[email],(error,rows) => {
  if(error) throw error;
  console.log('User info is: ', rows);
  res.json({'number':1})
  });
}); 

// 로그아웃
app.get('/users/logout', (req,res) => {
    connection.release();
});

app.listen(app.get('port'), () => {
  console.log('Express server listening on port ' + app.get('port'));
});
