<template>
    <header class="app-header">
        <div class="wrapper">
            <router-link :to="{ name: 'landing-page' }" class="logo">Endpoints</router-link>
            <button class="button create-btn" @click="onClick">Create Endpoint</button>
            <router-link class="button list-btn" :to="{ name: 'endpoints-page' }" v-if="hasAvailableEndpoints"></router-link>
        </div>
    </header>
</template>

<script>
    import { mapState, mapGetters } from 'vuex';

    export default {
        computed: Object.assign({},
            mapState(['hash']),
            mapGetters(['hasAvailableEndpoints'])
        ),

        methods: {
            async onClick(e) {
                const response = await fetch('/endpoints').then(response => response.json());
                const routeData = {
                    name: 'endpoint-page',
                    params: {
                        hash: response.hash
                    }
                };

                if (this.hash) {
                    const route = this.$router.resolve(routeData);
                    window.open(route.href, '_blank');
                } else {
                    this.$router.push(routeData);
                }
            }
        }
    };
</script>

<style scoped>
    .app-header {
        padding: 1.6rem 0;
        border-bottom: 1px solid var(--gray-1);
        background-color: #fff;
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

    .button {
        padding: 0.5em 1em;
        border-radius: 2px;
        font-size: 1.3rem;
        text-transform: uppercase;
        cursor: pointer;
    }

    .create-btn {
        border: 1px solid var(--primary-color-dark-1);
        color: #fff;
        background-color: var(--primary-color);
    }

    .list-btn {
        width: 3.3rem;
        height: 3.3rem;
        border: 1px solid var(--gray-1);
        margin-left: 0.4rem;
        background: url("~images/list.png") center center no-repeat;
        background-size: 50%;
    }
</style>
