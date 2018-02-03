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
            const requestLogs = [
                { method: 'GET', timestamp: Date.now() },
                { method: 'GET', timestamp: Date.now() },
                { method: 'GET', timestamp: Date.now() },
                { method: 'GET', timestamp: Date.now() },
                { method: 'GET', timestamp: Date.now() }
            ];
            context.commit('setRequestLogs', requestLogs);
        }
    }
});
