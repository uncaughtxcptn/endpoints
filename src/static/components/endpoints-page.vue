<template>
    <div class="endpoints-page">
        <div class="wrapper">
            <h2>Your Endpoints</h2>
            <p class="subtitle">* This list is stored only in this browser.</p>

            <template v-if="hasAvailableEndpoints">
                <router-link
                    class="endpoint-link"
                    v-for="endpoint in availableEndpoints"
                    :key="endpoint.hash"
                    :to="{ name: 'endpoint-page', params: { hash: endpoint.hash } }"
                >
                    <p>{{ baseUrl }}/<span>{{ endpoint.hash }}</span></p>
                    <time>{{ formatDate(endpoint.timestamp) }}</time>
                </router-link>
            </template>

            <p v-else class="empty">You currently don't have any endpoints.</p>
        </div>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';
    import { format } from 'date-fns';

    export default {
        computed: Object.assign({},
            mapState(['baseUrl', 'availableEndpoints']),
            mapGetters(['hasAvailableEndpoints'])
        ),

        methods: {
            formatDate(timestamp) {
                const date = new Date(timestamp);
                return format(date, 'MMM D, YYYY hh:mm:ss A');
            }
        }
    };
</script>

<style scoped>
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

    .empty {
        padding: 0.4rem 0;
        font-size: 1.3rem;
        color: var(--warning-color);
    }
</style>
