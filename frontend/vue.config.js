const path = require('path')

module.exports = {
  transpileDependencies: ['vuetify'],
  // dev: {
  //   proxyTable: {
  //     '/api' : {
  //       target: 'http://localhost:8000',
  //       changeOrigin: true,
  //       pathRewrite: {  // 開発サーバーでもDjangoのAPIにアクセスできるように設定
  //         '^/api': 'api'
  //       }
  //     }
  //   },
  //   // デフォルトのSourceMapは相対パスを参照しているらしく、この環境ではバグになる。
  //   cssSourceMap: false,
  // },
  // build: { // コンパイルされたファイルをDjangoの所定位置へ
  //   // Template for index.html
  //   index: path.resolve(__dirname, '../templates/index.html'),

  //   // Paths
  //   assetsRoot: path.resolve(__dirname, '../static'),
  //   assetsSubDirectory: 'build',
  //   assetsPublicPath: '/static/',
  // }
}
