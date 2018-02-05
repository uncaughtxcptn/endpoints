const path = require('path');

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
    resolve: {
        alias: {
            images: path.resolve(__dirname, 'src/static/images')
        }
    }
};
