var path = require('path');

module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        config: path.resolve(`src/configs/${process.env.NODE_ENV}.ts`),
      }
    }
  }
};
