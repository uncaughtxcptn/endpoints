<template>
    <header class="app-header">
        <div class="wrapper">
            <router-link :to="{ name: 'landing-page' }" class="logo">Endpoints</router-link>
            <button @click="onClick">Create Endpoint</button>
        </div>
    </header>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        computed: mapState(['hash']),

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
        justify-content: space-between;
        align-items: center;
    }

    .logo {
        font-size: 1.8rem;
        font-weight: 300;
        text-decoration: none;
    }

    button {
        padding: 0.5em 1em;
        border: 1px solid var(--primary-color-dark-1);
        border-radius: 2px;
        font-size: 1.3rem;
        text-transform: uppercase;
        color: #fff;
        background-color: var(--primary-color);
        cursor: pointer;
    }
</style>
