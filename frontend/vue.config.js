module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: "http://192.168.1.236:8000",
  },
};
