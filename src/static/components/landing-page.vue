<template>
    <div class="landing-page">
        <app-header></app-header>
        <hero-section></hero-section>
        <features-section></features-section>
        <app-footer></app-footer>
    </div>
</template>

<script>
    export default {
        components: {
            'app-header': require('./app-header.vue').default,
            'app-footer': require('./app-footer.vue').default,
            'hero-section': require('./hero-section.vue').default,
            'features-section': require('./features-section.vue').default
        }
    };
</script>
