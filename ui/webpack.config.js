const debug =  process.env.NODE_ENV !== "production";
const webpack = require('webpack');
const path = require('path');

module.exports = {
  module: {
    rules: [{
      test: /\.jsx?$/,
      exclude: /(node_modules|bower_components)/,
      use: [{
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-react', '@babel/preset-env']
        }
      }]
    },
    {
      test: /\.css$/i,
      use: ["style-loader", "css-loader"]
    }]
  },
  context: path.join(__dirname, "src"),
  entry: {
      common: './common/index.js'
  },
  output: {
    path: __dirname + "/src/",
    filename: '[name].component.js'
  }
};
