import Vue from 'vue';
import router from './router';
import store from './store';
import EndpointsApp from './components/endpoints-app.vue';
import './stylesheets/index.css';

// Fetch states that are required for every route. Each route could still
// define their own specific navigation guards.
router.beforeEach(async (to, from, next) => {
    await store.dispatch('fetchAvailableEndpoints');
    next();
});

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(EndpointsApp)
});
