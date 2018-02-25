const path = require('path');
const webpack = require('webpack');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

const isProdEnv = process.env.NODE_ENV === 'production';

const webpackConfig = {
    entry: path.resolve(__dirname, 'src/static/index.js'),
    output: {
        path: path.resolve(__dirname, 'src/static/build'),
        filename: 'index.js',
        chunkFilename: '[name].js',
        publicPath: '/static/build/'
    },
    devtool: isProdEnv ? 'source-map' : 'cheap-module-eval-source-map',
    module: {
        rules: [ {
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.css$/,
            use: ['style-loader', 'css-loader']
        }, {
            test: /\.png$/,
            loader: 'url-loader',
            options: {
                limit: 1024 * 10,
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

// Add extra configs when in production mode.
if (isProdEnv) {
    webpackConfig.plugins = [
        ...(webpackConfig.plugins || []),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify(process.env.NODE_ENV || 'development'),
                BASE_URL: JSON.stringify(process.env.BASE_URL || 'localhost:8080')
            }
        }),
        new UglifyJSPlugin({ sourceMap: true })
    ];
}

module.exports = webpackConfig;
