import Vue from 'vue';
import Vuex from 'vuex';
import { objectToFormData } from './lib/utils';
import * as endpointsDb from './lib/endpoints-db';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        baseUrl: window.location.host || 'localhost:8080',
        hash: null,
        isLive: false,
        requestLogs: [],
        bufferedRequestLogs: [],
        availableEndpoints: [],
        isLoadingNavigation: false,
        autoResponse: {
            statusCode: null,
            headers: [
                { name: 'Content-Type', value: '' }
            ],
            responseCode: null
        },
        isPerformingAction: false
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

        setAutoResponse(state, autoResponse) {
            state.autoResponse = autoResponse;
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
        },

        insertAvailableEndpoint(state, endpoint) {
            state.availableEndpoints = [endpoint, ...state.availableEndpoints];
        },

        setIsLoadingNavigation(state, isLoadingNavigation) {
            state.isLoadingNavigation = isLoadingNavigation;
        },

        setIsPerformingAction(state, isPerformingAction) {
            state.isPerformingAction = isPerformingAction;
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

        async fetchAutoResponse(context) {
            const endpoint = `/${context.state.hash}/auto-response`;
            const response = await fetch(endpoint).then(response => response.json());
            context.commit('setAutoResponse', response);
        },

        async fetchRequestLogs(context) {
            const logsEndpoint = `/${context.state.hash}/logs`;
            let requestLogs = await fetch(logsEndpoint).then(response => response.json());
            requestLogs = requestLogs.map(requestLog =>
                Object.assign({}, requestLog, { isExpanded: false }));
            context.commit('setRequestLogs', requestLogs);
        },

        async fetchAvailableEndpoints(context) {
            const endpoints = await endpointsDb.getAll();
            context.commit('setAvailableEndpoints', endpoints);
        },

        async createEndpoint(context) {
            context.commit('setIsPerformingAction', true);

            const response = await fetch('/endpoints').then(response => response.json());
            const endpoint = await endpointsDb.put(response);
            context.commit('insertAvailableEndpoint', endpoint);

            context.commit('setIsPerformingAction', false);
            return response;
        },

        async setAutoResponse(context, data) {
            context.commit('setIsPerformingAction', true);

            data.responseBody = data.responseBody || '';
            const endpoint = `/${context.state.hash}/response`;
            const response = await fetch(endpoint, {
                method: 'POST',
                body: objectToFormData(data)
            }).then(response => response.json());
            context.commit('setAutoResponse', data);

            context.commit('setIsPerformingAction', false);
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
