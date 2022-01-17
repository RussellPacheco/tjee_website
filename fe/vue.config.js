// vue.config.js

module.exports = {
  outputDir: "/static/",
  devServer: {
    proxy: {
      "/": {
        target: "http://localhost:5000",
        secure: false,
        changeOrigin: true,
      },
    },
  },
};
