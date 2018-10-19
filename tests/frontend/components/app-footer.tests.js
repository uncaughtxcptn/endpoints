import { mount } from '@vue/test-utils';
import AppFooter from '@/components/app-footer.vue';

describe('AppFooter', () => {
    const wrapper = mount(AppFooter);

    test('is a Vue instance', () => {
        expect(wrapper.isVueInstance()).toBeTruthy();
    });

    test('matches snapshot', () => {
        expect(wrapper.element).toMatchSnapshot();
    });
});
