import { shallowMount, createLocalVue } from '@vue/test-utils';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import AppHeader from '@/components/app-header.vue';

const localVue = createLocalVue();
localVue.use(Vuex);
localVue.use(VueRouter);

describe('AppHeader', () => {
    let state;
    let getters;
    let actions;
    let store;

    beforeEach(() => {
        state = {
            hash: 'abc123',
            isPerformingActions: false
        };
        getters = {
            hasAvailableEndpoints: () => false
        };
        actions = {
            createEndpoint: jest.fn()
        };
        store = new Vuex.Store({ state, getters, actions });
    });

    test('is a Vue instance', () => {
        const wrapper = shallowMount(AppHeader, { store, localVue });
        expect(wrapper.isVueInstance()).toBeTruthy();
    });

    test('matches snapshot', () => {
        const wrapper = shallowMount(AppHeader, { store, localVue });
        expect(wrapper.element).toMatchSnapshot();
    });
});
