// 비동기 테스트

const fs = require('fs');
const util = require('util');
const buffer = require('buffer');
// import { writeFileSync } from 'node:fs';
// import { Buffer } from 'node:buffer';


console.log('aaaaa')
// util의 로그를 쓰면 적용된 시점을 같이 출력하므로 유용
util.log('bbbbb', __dirname)

fs.readFile(__dirname + '/test.json', 'utf-8', (err,data) => {
  if(err) return console.error(err);

  util.log("data >> ", data);
})

util.log("---------------------------");

const data = 'WriteTest.js';
const msgfile = __dirname + "/writetest.txt"
fs.writeFileSync(msgfile, data, (err) => {
  if (err) throw err;
  console.log('The file has been saved!');
});

let data_3 = fs.readFileSync(msgfile, 'utf-8');
util.log("data_3 >> ", data_3);

// Sync는 해당 코드가 실행될 때까지 다음으로 넘어가지 않음
let data_2 = fs.readFileSync(__dirname + '/test.json', 'utf-8');
util.log("data_2 >> ", data_2);

util.log("===========================");



