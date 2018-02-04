<template>
    <section class="endpoint-header">
        <header>
            <h2>{{ baseUrl }}/<span>{{ hash }}</span></h2>
        </header>
        <div class="switches">
            <labelled-switch label="Live"></labelled-switch>
        </div>
    </section>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        computed: mapState(['baseUrl', 'hash']),

        components: {
            'labelled-switch': require('./labelled-switch.vue').default
        }
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

    .switches {
        margin-top: 0.8rem;
    }

    .labelled-switch {
        text-transform: uppercase;
    }
</style>
