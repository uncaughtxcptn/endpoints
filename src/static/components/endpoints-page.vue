<template>
    <div class="endpoints-page">
        <app-header></app-header>

        <div class="wrapper">
            <h2>Your Endpoints</h2>
            <p class="subtitle">* These endpoints are only stored in this browser.</p>

            <router-link
                class="endpoint-link"
                v-for="endpoint in availableEndpoints"
                :key="endpoint.hash"
                :to="{ name: 'endpoint-page', params: { hash: endpoint.hash } }"
            >
                <p>{{ baseUrl }}/<span>{{ endpoint.hash }}</span></p>
                <time>{{ formatDate(endpoint.timestamp) }}</time>
            </router-link>
        </div>

        <app-footer></app-footer>
    </div>
</template>

<script>
    import { mapState } from 'vuex';
    import { format } from 'date-fns';

    export default {
        computed: mapState(['baseUrl', 'availableEndpoints']),

        methods: {
            formatDate(timestamp) {
                const date = new Date(timestamp);
                return format(date, 'MMM D, YYYY hh:mm:ss A');
            }
        },

        components: {
            'app-header': require('./app-header.vue').default,
            'app-footer': require('./app-footer.vue').default
        }
    };
</script>

<style scoped>
    .endpoints-page {
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

    h2 {
        margin: 0;
        font-size: 1.8rem;
        font-weight: 300;
        color: var(--gray-3);
    }

    .subtitle {
        margin-bottom: 5rem;
        font-size: 1.2rem;
        color: var(--gray-3);
    }

    .endpoint-link {
        display: flex;
        justify-content: space-between;
        padding: 0.4rem 0.8rem;
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        margin: 0.8rem 0;
        font-size: 1.2rem;
        text-decoration: none;
    }
</style>
