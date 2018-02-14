<template>
    <div class="endpoints-app">
        <app-header></app-header>
        <router-view></router-view>
        <app-footer></app-footer>
    </div>
</template>

<script>
    export default {
        components: {
            'app-header': require('./app-header.vue').default,
            'app-footer': require('./app-footer.vue').default
        }
    };
</script>

<style scoped>
    .endpoints-app {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }

    .app-footer {
        margin-top: auto;
    }
</style>
