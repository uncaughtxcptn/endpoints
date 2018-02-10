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

        <app-footer></app-footer>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';
    import store from '../store';

    export default {
        computed: Object.assign({},
            mapState(['hash', 'requestLogs']),
            mapGetters(['bufferedRequestLogsCount'])
        ),

        methods: {
            flushRequestLogs() {
                this.$store.commit('flushRequestLogs');
            }
        },

        components: {
            'app-header': require('./app-header.vue').default,
            'app-footer': require('./app-footer.vue').default,
            'endpoint-header': require('./endpoint-header.vue').default,
            'pending-counter': require('./pending-counter.vue').default,
            'request-log': require('./request-log.vue').default
        },

        mounted() {
            this.$store.dispatch('fetchRequestLogs');

            const wsUrl = `ws://${location.host}/${this.hash}/ws`;
            const ws = new WebSocket(wsUrl);

            ws.addEventListener('message', e => {
                const message = JSON.parse(e.data);
                if (message.type === 'access-log') {
                    this.$store.commit('insertRequestLog', message.data);
                }
            });
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
    .endpoint-page {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }

    .app-footer {
        margin-top: auto;
    }

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
