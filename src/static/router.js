import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [ {
    path: '/',
    component: () => import(/* webpackChunkName: 'landing-page' */ './components/landing-page.vue'),
    name: 'landing-page'
}, {
    path: '/:hash',
    component: () => import(/* webpackChunkName: 'endpoint-page' */ './components/endpoint-page.vue'),
    name: 'endpoint-page'
} ];

export default new VueRouter({
    routes,
    mode: 'history'
});
