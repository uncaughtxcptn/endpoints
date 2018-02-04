<template>
    <section class="endpoint-header">
        <header>
            <h2>{{ baseUrl }}/<span>{{ hash }}</span></h2>
        </header>
    </section>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        computed: mapState(['baseUrl', 'hash'])
    };
</script>

<style scoped>
    h2 {
        font-size: 1.8rem;
        font-weight: 300;
        color: var(--gray-3);
    }

    span {
        font-weight: 400;
        color: var(--primary-text-color);
    }
</style>
