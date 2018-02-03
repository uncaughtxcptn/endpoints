<template>
    <header class="app-header">
        <div class="wrapper">
            <router-link :to="{ name: 'landing-page' }" class="logo">Endpoints</router-link>
            <button @click="onClick">Create Endpoint</button>
        </div>
    </header>
</template>

<script>
    export default {
        methods: {
            onClick(e) {
                // TODO: Get actual endpoint id/hash from backend.
                const hash = 'abcdefghijklmnopqrstuvwxyz';

                this.$router.push({
                    name: 'endpoint-page',
                    params: { hash }
                });
            }
        }
    };
</script>

<style scoped>
    .app-header {
        padding: 1.6rem 0;
        border-bottom: 1px solid var(--gray-1);
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
        font-size: 13px;
        text-transform: uppercase;
        color: #fff;
        background-color: var(--primary-color);
        cursor: pointer;
    }
</style>
