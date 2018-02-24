<template>
    <header class="app-header">
        <navigation-loader></navigation-loader>

        <div class="wrapper">
            <router-link :to="{ name: 'landing-page' }" class="logo">Endpoints</router-link>
            <base-button class="primary" @click="onClick" :loading="isPerformingAction">Create Endpoint</base-button>
            <router-link class="list-btn" :to="{ name: 'endpoints-page' }" v-if="hasAvailableEndpoints"></router-link>
        </div>
    </header>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    export default {
        computed: Object.assign({},
            mapState(['hash', 'isPerformingAction']),
            mapGetters(['hasAvailableEndpoints'])
        ),

        methods: {
            async onClick(e) {
                const response = await this.$store.dispatch('createEndpoint');
                const routeData = {
                    name: 'endpoint-page',
                    params: {
                        hash: response.hash
                    }
                };

                this.$ga.event('endpoints', 'create');

                if (this.hash) {
                    const route = this.$router.resolve(routeData);
                    window.open(route.href, '_blank');
                } else {
                    this.$router.push(routeData);
                }
            }
        },

        components: {
            'base-button': require('./base-button.vue').default,
            'navigation-loader': require('./navigation-loader.vue').default
        }
    };
</script>

<style scoped>
    .app-header {
        padding: 1.6rem 0;
        border-bottom: 1px solid var(--gray-1);
        background-color: #fff;
    }

    .navigation-loader {
        position: absolute;
        top: 0;
        left: 0;
    }

    .wrapper {
        display: flex;
        align-items: center;
    }

    .logo {
        margin-right: auto;
        font-size: 1.8rem;
        font-weight: 300;
        text-decoration: none;
    }

    .list-btn {
        width: 3.3rem;
        height: 3.3rem;
        padding: 0.5em 1em;
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        margin-left: 0.4rem;
        font-size: 1.3rem;
        text-transform: uppercase;
        background: url("~images/list.png") center center no-repeat;
        background-size: 50%;
        cursor: pointer;
    }
</style>
