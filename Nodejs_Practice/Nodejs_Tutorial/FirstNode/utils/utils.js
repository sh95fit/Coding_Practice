const ogs = require('open-graph-scraper'),
      HashMap = require('hashmap'),
      Crypto = require('crypto-js'),
      SHA256 = ("crypto-js/sha256");

const EKey = "nodejs";

module.exports = {

  // ogs_info(url, fn) {
  //   return ogs({url: url}, (err, ret) => {
  //     fn(err, ret);
  //   });
  // }

  ogs_info(url, fn) {
    return ogs({url: url}).then((data) => {
      const {error, result, response} = data;
      fn(error,result);
    });
  },


// 양방향 암호화 (암호화, 복호화 가능!)
// 암호화
  encrypt (data, key) {
    return Crypto.AES.encrypt(data, key || EKey).toString();
  },

// 복호화
  decrypt(data, key) {
    return Crypto.AES.decrypt(data, key || EKey).toString(Crypto.enc.Utf8);
  },

// 단방향 암호화
  encryptSha2(data, key) {
    if (!data) return null;
    key = key || EKey;

    try {
      return Crypto.SHA256(data + key).toString();
    } catch (Err) {

    }
  },

  makeMap(key, value) {
    const map = new HashMap();
    map.set(key, value);
    console.log("TTT >> ", map.get(key));
    return map;
  }

};