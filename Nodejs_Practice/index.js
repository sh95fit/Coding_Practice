/* Node.js 테스트*/
/*
Node.js란?
- 웹 브라우저상에서만 동작하던 Javascript를 웹 서버상에서 활용할 수 있도록 해주는 런타임 환경
- 즉 Chrome V8 JavaScript 엔진으로 빌드된 JavaScript 런타임
- But, Node.js는 서버사이드스크립트가 아닌 프로그램이다!
- 기능 단위 모듈이 다양하기 때문에 활용성이 크다

npm (node package manager)
- 필요한 툴들을 검색해 다운로드해서 활용할 수 있도록 해주는 도구
- 사용법 : npm install 모듈명


Express 모듈
- node.js를 이용해서 웹 프레임워크를 모듈

주요 포트 리스트
FTP : 20, 21 (TCP)
SSH : 22 (TCP)
Telnet : 23 (TCP)
SMTP : 25 (TCP)
DNS : 53 (TCP/UDP)
DHCP : 67 (UDP)
HTTP : 80 (TCP)
HTTPS : 443 (TCP)

*/

// npm 실습 - figlet 활용하기
// var figlet = require('figlet');

// figlet('Huns Project', function(err, data) {
//     if (err) {
//         console.log('Something went wrong...');
//         console.dir(err);
//         return;
//     }
//     console.log(data)
// });

// express 웹 동작 테스트
// const express = require('express')
// const app = express()
// const port = 3000

// app.get('/', (req, res) => {       // app.[HTTP 메소드]('[라우팅]', [콜백함수])    + 콜백함수 형태 : () => {} /콜백함수란 HTTP 메소드 함수가 끝난 뒤에 실행할 함수를 의미!
//     res.send('Hello World!')
// })

// app.get('/dog', (req, res) => {
//     res.send('<h1>강아지<h1>')        // HTML 코드도 요청으로 보낼 수 있다!
// })

// app.get('/cat', (req, res) => {
//     res.json({'sound' : '야옹'})    // json 형태로 보냄(키:값)
// })

// // 변수 (params)를 이용한 요청-응답
// app.get('/user/:id', (req, res) => {
//     const q = req.params  
//     console.log(q.id)

//     res.send(q.id)
// })


// // query를 이용한 요청-응답
// app.get("/user/:id", (req, res) => {
//     const p = req.query
//     console.log(p)

//     res.send(p.id)
// })


// app.listen(port, () => {
//     console.log(`Example app listening on port ${port}`)
// })


// 간단한 API 서버 만들기
const express = require('express')
var cors = require('cors')
const app = express()
const port = 3000

app.use(cors())

app.get('/', (req, res) => {       
    res.send('Hello World!')
})

app.get('/sound/:name', (req, res) => {
    const { name } = req.params
    
    if(name == "dog") {
        res.json({'sound' : '멍멍'})
    } else if(name == 'cat') {
        res.json({'sound' : '야옹'})
    } else if(name == 'pig') {
        res.json({'sound' : '꿀꿀'})
    } else {
        res.json({'sound' : '알수없음'})
    }
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})