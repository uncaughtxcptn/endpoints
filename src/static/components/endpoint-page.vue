<template>
    <div class="endpoint-page">
        <app-header></app-header>

        <div class="wrapper">
            <endpoint-header></endpoint-header>
        </div>
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import store from '../store';

    export default {
        components: {
            'app-header': require('./app-header.vue').default,
            'endpoint-header': require('./endpoint-header.vue').default
        },

        beforeRouteEnter(to, from, next) {
            store.commit('setHash', to.params.hash);
            next();
        },

        beforeRouteLeave(to, from, next) {
            store.commit('unsetHash');
            next();
        }
    };
</script>

<style scoped>
    .wrapper {
        padding: 5rem 0;
    }
</style>
