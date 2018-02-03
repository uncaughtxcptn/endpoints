import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        baseUrl: process.env.BASE_URL || 'localhost:3000',
        hash: null
    },

    mutations: {
        setHash(state, hash) {
            state.hash = hash;
        },

        unsetHash(state) {
            state.hash = null;
        }
    }
});
