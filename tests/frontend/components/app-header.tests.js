import { shallowMount, createLocalVue, RouterLinkStub } from '@vue/test-utils';
import Vuex from 'vuex';
import AppHeader from '@/components/app-header.vue';
import BaseButton from '@/components/base-button.vue';

const localVue = createLocalVue();
localVue.use(Vuex);

describe('AppHeader', () => {
    let state;
    let getters;
    let actions;
    let store;
    let stubs = {
        RouterLink: RouterLinkStub
    };

    const mountComponent = (options = {}) => {
        return shallowMount(AppHeader, { localVue, store, stubs, ...options });
    };

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
        const wrapper = mountComponent();
        expect(wrapper.isVueInstance()).toBe(true);
    });

    test('matches snapshot', () => {
        const wrapper = mountComponent();
        expect(wrapper.element).toMatchSnapshot();
    });

    test('hides link to list page when there are no available endpoints', () => {
        const wrapper = mountComponent();
        const link = wrapper.find('.list-btn');
        expect(link.exists()).toBe(false);
    });

    test('displays link to list page when there are available endpoints', () => {
        getters.hasAvailableEndpoints = () => true;
        store = new Vuex.Store({ state, getters, actions });

        const wrapper = mountComponent();
        const link = wrapper.find('.list-btn');
        expect(link.exists()).toBe(true);
        expect(link.props('to')).toEqual({ name: 'endpoints-page' });
    });

    test('displays create button in normal state while not performing an action', () => {
        const wrapper = mountComponent();
        const button = wrapper.find(BaseButton);
        expect(button.props('loading')).toBeFalsy();
    });

    test('displays create button in loading state while performing an action', () => {
        state.isPerformingAction = true;
        store = new Vuex.Store({ state, getters, actions });

        const wrapper = mountComponent();
        const button = wrapper.find(BaseButton);
        expect(button.props('loading')).toBe(true);
    });
});
