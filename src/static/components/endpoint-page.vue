<template>
    <div class="endpoint-page">
        <div class="wrapper">
            <endpoint-header></endpoint-header>
            <pending-counter :count="bufferedRequestLogsCount" @click="flushRequestLogs"></pending-counter>

            <div class="request-logs">
                <request-log
                    v-for="requestLog in requestLogs"
                    :key="requestLog.id"
                    :data="requestLog">
                </request-log>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState, mapGetters, mapMutations } from 'vuex';
    import store from '../store';

    export default {
        computed: Object.assign({},
            mapState(['hash', 'requestLogs']),
            mapGetters(['bufferedRequestLogsCount'])
        ),

        methods: mapMutations(['flushRequestLogs']),

        components: {
            'endpoint-header': require('./endpoint-header.vue').default,
            'pending-counter': require('./pending-counter.vue').default,
            'request-log': require('./request-log.vue').default
        },

        mounted() {
            this.$store.dispatch('fetchRequestLogs');

            const wsProtocol = window.location.protocol === 'https:' ? 'wss' : 'ws';
            const wsUrl = `${wsProtocol}://${window.location.host}/${this.hash}/ws`;
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
            Promise.all([
                store.dispatch('fetchLiveStatus'),
                store.dispatch('fetchAutoResponse')
            ]).then(() => next());
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
