import Vue from 'vue';
import router from './router';
import store from './store';
import EndpointsApp from './components/endpoints-app.vue';
import './stylesheets/index.css';

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(EndpointsApp)
});
