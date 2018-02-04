import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        baseUrl: process.env.BASE_URL || 'localhost:3000',
        hash: null,
        requestLogs: []
    },

    mutations: {
        setHash(state, hash) {
            state.hash = hash;
        },

        unsetHash(state) {
            state.hash = null;
        },

        setRequestLogs(state, requestLogs) {
            state.requestLogs = requestLogs;
        },

        unsetRequestLogs(state) {
            state.requestLogs = [];
        }
    },

    actions: {
        fetchRequestLogs(context) {
            // TODO: Request logs should be fetched from the backend.
            const requestLogs = [ {
                timestamp: Date.now(),
                request: `
                    GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1
                    Host: localhost:3000
                    Accept: application/json`,
                response: `
                    HTTP/1.1 200 OK
                    Content-Type: application/json
                    Content-Length: 100
                    Cache-Control: public, max-age=10000
                    ETag: w/ak3i2hsh8idk3os392

                    {"title": "Hello World"}`
            }, {
                timestamp: Date.now(),
                request: `
                    GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1
                    Host: localhost:3000
                    Accept: application/json`
            }, {
                timestamp: Date.now(),
                request: `
                    GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1
                    Host: localhost:3000
                    Accept: application/json`,
                response: `
                    HTTP/1.1 200 OK
                    Content-Type: application/json
                    Content-Length: 100
                    Cache-Control: public, max-age=10000
                    ETag: w/ak3i2hsh8idk3os392

                    {"title": "Hello World"}`
            }, {
                timestamp: Date.now(),
                request: `
                    GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1
                    Host: localhost:3000
                    Accept: application/json`,
                response: 'HTTP/1.1 500 Internal Server Error'
            } ];
            context.commit('setRequestLogs', requestLogs);
        }
    }
});
