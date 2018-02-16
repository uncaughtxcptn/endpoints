import Vue from 'vue';
import router from './router';
import store from './store';
import EndpointsApp from './components/endpoints-app.vue';
import './stylesheets/index.css';

// Fetch states that are required for every route. Each route could still
// define their own specific navigation guards.
router.afterEach((to, from) => {
    if (!store.getters.hasAvailableEndpoints) {
        store.dispatch('fetchAvailableEndpoints');
    }
});

// Show loading animation between navigations.
router.beforeEach((to, from, next) => {
    store.commit('setIsLoadingNavigation', true);
    next();
});

router.afterEach((to, from) => {
    store.commit('setIsLoadingNavigation', false);
});

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(EndpointsApp)
});
