import Vue from 'vue';
import Vuex from 'vuex';
import { objectToFormData } from './lib/utils';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        baseUrl: process.env.BASE_URL || 'localhost:8080',
        hash: null,
        isLive: false,
        requestLogs: [],
        bufferedRequestLogs: [],
        availableEndpoints: []
    },

    getters: {
        bufferedRequestLogsCount(state) {
            return state.bufferedRequestLogs.length;
        },

        hasAvailableEndpoints(state) {
            return state.availableEndpoints.length > 0;
        }
    },

    mutations: {
        setHash(state, hash) {
            state.hash = hash;
        },

        unsetHash(state) {
            state.hash = null;
        },

        setLiveStatus(state, isLive) {
            state.isLive = isLive;
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

        insertRequestLog(state, requestLog) {
            state.bufferedRequestLogs = [
                Object.assign({}, requestLog, { isExpanded: false }),
                ...state.bufferedRequestLogs
            ];
        },

        flushRequestLogs(state) {
            state.requestLogs = [...state.bufferedRequestLogs, ...state.requestLogs];
            state.bufferedRequestLogs = [];
        },

        unsetRequestLogs(state) {
            state.requestLogs = [];
        },

        setAvailableEndpoints(state, availableEndpoints) {
            state.availableEndpoints = availableEndpoints;
        }
    },

    actions: {
        async fetchLiveStatus(context) {
            const endpoint = `/${context.state.hash}/live`;
            const response = await fetch(endpoint).then(response => response.json());
            context.commit('setLiveStatus', response.live);
        },

        async updateLiveStatus(context, isLive) {
            const endpoint = `/${context.state.hash}/live`;
            const response = await fetch(endpoint, {
                method: 'POST',
                body: objectToFormData({ live: isLive ? 1 : 0 })
            });
            context.commit('setLiveStatus', isLive);
        },

        async fetchRequestLogs(context) {
            const logsEndpoint = `/${context.state.hash}/logs`;
            let requestLogs = await fetch(logsEndpoint).then(response => response.json());
            requestLogs = requestLogs.map(requestLog =>
                Object.assign({}, requestLog, { isExpanded: false }));
            context.commit('setRequestLogs', requestLogs);
        },

        async fetchAvailableEndpoints(context) {
            context.commit('setAvailableEndpoints', [
                { hash: '34eaa84b-c1c3-49c1-ad4c-6f12e5412f24', timestamp: Date.now() },
                { hash: '34eaa84b-c1c3-49c1-ad4c-6f12e5412f24', timestamp: Date.now() },
                { hash: '34eaa84b-c1c3-49c1-ad4c-6f12e5412f24', timestamp: Date.now() }
            ]);
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
