<template>
    <div class="endpoint-page">
        <app-header></app-header>

        <div class="wrapper">
            <endpoint-header></endpoint-header>

            <div class="request-logs">
                <request-log
                    v-for="(requestLog, index) in requestLogs"
                    :key="index"
                    :data="requestLog">
                </request-log>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import store from '../store';

    export default {
        computed: mapState(['requestLogs']),

        components: {
            'app-header': require('./app-header.vue').default,
            'endpoint-header': require('./endpoint-header.vue').default,
            'request-log': require('./request-log.vue').default
        },

        mounted() {
            this.$store.dispatch('fetchRequestLogs');
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

    .request-logs {
        margin-top: 5rem;
    }

    .request-log:not(:first-of-type) {
        margin-top: 0.8rem;
    }

    .request-log:not(:last-of-type) {
        margin-top: 0.8rem;
    }
</style>
