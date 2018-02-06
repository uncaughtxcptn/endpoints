const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: path.resolve(__dirname, 'src/static/index.js'),
    output: {
        path: path.resolve(__dirname, 'src/static/build'),
        filename: 'index.js',
        chunkFilename: '[name].js',
        publicPath: '/static/build/'
    },
    module: {
        rules: [ {
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        }, {
            test: /\.png$/,
            loader: 'file-loader',
            options: {
                name: '[name].[ext]'
            }
        } ]
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify(process.env.NODE_ENV || 'development'),
                BASE_URL: JSON.stringify(process.env.BASE_URL || 'localhost:8080')
            }
        })
    ],
    resolve: {
        alias: {
            images: path.resolve(__dirname, 'src/static/images')
        }
    }
};
