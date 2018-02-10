<template>
    <div class="landing-page">
        <app-header></app-header>

        <hero-section></hero-section>
    </div>
</template>

<script>
    export default {
        components: {
            'app-header': require('./app-header.vue').default,
            'hero-section': require('./hero-section.vue').default
        }
    };
</script>
