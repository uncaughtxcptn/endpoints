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

        updateRequestLog(state, { id, updateData }) {
            const index = state.requestLogs.findIndex(requestLog => requestLog.id === id);
            const requestLog = state.requestLogs[index];
            const requestLogKeys = Object.keys(requestLog);
            const baseData = requestLogKeys.reduce((data, key) => {
                data[key] = requestLog[key];
                return data;
            }, {});
            Vue.set(state.requestLogs, index, Object.assign(baseData, updateData));
        },

        unsetRequestLogs(state) {
            state.requestLogs = [];
        }
    },

    actions: {
        async fetchRequestLogs(context) {
            const logsEndpoint = `/${context.state.hash}/logs`;
            const requestLogs = await fetch(logsEndpoint).then(response => response.json());
            context.commit('setRequestLogs', requestLogs);
        },

        setResponse(context, { id, response }) {
            // TODO: Response should be sent to the backend.
            let responseString = `
                HTTP/1.1 ${response.statusCode} OK
                ${response.headers.map(h => h.name + ':' + h.value).join('\n')}`;
            if (response.responseBody) {
                responseString += '\n\n' + response.responseBody;
            }
            context.commit('updateRequestLog', {
                id,
                updateData: { response: responseString }
            });
        }
    }
});
