const mysql = require('mysql');

const connection = mysql.createConnection({
  host : '152.70.90.174',
  user : 'ksh',
  password : 'ksh',
  database : 'node_db'
});

connection.connect();

//  트랜젝션을 묶어줌
connection.beginTransaction(err2 => {
  connection.query('update User set lastlogin=now() where uid=?', ['test'], function (error, results, fields) {
    if (error) throw error;
    console.log('Update : ', results.affectedRows);

    // Update 쿼리를 우선 실행한 후 Select 쿼리를 실행해야 하는 경우 콜백 함수로 커넥션 안에서 조치
    connection.query('select * from User where uid=?', ['test'], function (error, results, fields) {
      if (error) throw error;
      console.log('The First User is : ', results[0]);
    });

    // 1회 커넥션 이후 바로 end 처리되어 select가 실행되지 않는 경우를 막기 위해 end 위치를 내부로 이동 필요
    connection.end();
  });
});


// 밖에 있는 경우 병렬로 처리되어 쿼리 속도에 따라 처리 순서가 달라진다
// connection.query('select * from User where uid=?', ['test'], function (error, results, fields) {
//   if (error) throw error;
//   console.log('The First User is : ', results[0]);
// });

// 커넥션을 반드시 끊어줘야 한다!
// connection.end();