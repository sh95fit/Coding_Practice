const mysql = require("mysql"),
      util = require("util"),
      Promise = require("bluebird");

Promise.promisifyAll(mysql);
Promise.promisifyAll(require("mysql/lib/Connection").prototype);
Promise.promisifyAll(require("mysql/lib/Pool").prototype);

const DB_INFO = {
  host : '152.70.90.174',
  user : 'ksh',
  password : 'ksh',
  database : 'node_db',
  multipleStatements: true,
  connectionLimit: 5,
  waitForConnections: false
};

module.exports = class {
  constructor(dbinfo) {
    dbinfo = dbinfo || DB_INFO;
    this.pool = mysql.createPool(dbinfo);
  }

  connect() {
    return this.pool.getConnectionAsync().disposer(conn => {
      return conn.release();
    });
  }

  end() {
    this.pool.end( function(err) {
      util.log(">>>>>>>>>>>>>>>>>> End of Pool !!");
      if (err)
        util.log("Error pool ending!!");
    });
  }
};