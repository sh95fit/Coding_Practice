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
- node.js를 이용해서 웹 프레임워크를 만듦

*/

// npm 실습 - figlet 활용하기
var figlet = require('figlet');

figlet('Huns Project', function(err, data) {
    if (err) {
        console.log('Something went wrong...');
        console.dir(err);
        return;
    }
    console.log(data)
});

