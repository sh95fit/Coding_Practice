// node 기본 제공 util
const util = require('util');
// 직접 많든 utils
const utils = require('../FirstNode/utils/utils');


let map = utils.makeMap('name', 'KIM');
util.log("map >>>>> ", map.get('name'))

return;

let str = "NodeJS";
let enc = utils.encrypt(str);
let dec = utils.decrypt(enc);
util.log("encrypt : ", enc);
util.log("decrypt : ", dec);
// util.log("encrypt : ", utils.encrypt(str, 'test'));

let enc_sha256 = utils.encryptSha2(str);
util.log("encrypt sha256 : ", enc_sha256);

return;

let url = 'https://naver.com';

utils.ogs_info(url, (err, ret) => {
  util.log(err, ret);
});














// TEST - 데이터를 아무것도 받아오지 못함

// // let url = "https://naver.com";
// let url = "https://naver.com";

// // ERR_UNHANDLED_REJECTION 처리를 위한 추가
// process.on('unhandledRejection', (err, promise) => {
//   console.log('Unhandled Rejection detect:', err.stack || err)
// })

// utils.ogs_info(url, (err, ret) => {
//   try {
//     util.log(err, ret);
//   } catch (e) {
//     util.isError(e);
//   }
// });