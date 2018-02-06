<template>
    <div class="endpoint-page">
        <app-header></app-header>

        <div class="wrapper">
            <endpoint-header></endpoint-header>
            <pending-counter :count="bufferedRequestLogsCount" @click="flushRequestLogs"></pending-counter>

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
    import { mapState, mapGetters } from 'vuex';
    import store from '../store';

    export default {
        computed: Object.assign({},
            mapState(['requestLogs']),
            mapGetters(['bufferedRequestLogsCount'])
        ),

        methods: {
            flushRequestLogs() {
                this.$store.commit('flushRequestLogs');
            }
        },

        components: {
            'app-header': require('./app-header.vue').default,
            'endpoint-header': require('./endpoint-header.vue').default,
            'pending-counter': require('./pending-counter.vue').default,
            'request-log': require('./request-log.vue').default
        },

        mounted() {
            this.$store.dispatch('fetchRequestLogs');

            setInterval(() => {
                this.$store.commit('insertRequestLog', this.requestLogs[this.requestLogs.length - 1]);
            }, 1000);
        },

        beforeRouteEnter(to, from, next) {
            store.commit('setHash', to.params.hash);
            next();
        },

        beforeRouteLeave(to, from, next) {
            store.commit('unsetHash');
            store.commit('unsetRequestLogs');
            next();
        }
    };
</script>

<style scoped>
    .wrapper {
        padding: 5rem 0;
    }

    .endpoint-header {
        margin-bottom: 5rem;
    }

    .request-log:not(:first-of-type) {
        margin-top: 0.8rem;
    }

    .request-log:not(:last-of-type) {
        margin-bottom: 0.8rem;
    }
</style>
