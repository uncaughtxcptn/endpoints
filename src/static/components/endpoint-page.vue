<template>
    <div class="endpoint-page">
        <app-header></app-header>
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import store from '../store';

    export default {
        components: {
            'app-header': require('./app-header.vue').default
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
