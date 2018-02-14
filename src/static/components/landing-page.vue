<template>
    <div class="landing-page">
        <hero-section></hero-section>
        <features-section></features-section>
    </div>
</template>

<script>
    export default {
        components: {
            'hero-section': require('./hero-section.vue').default,
            'features-section': require('./features-section.vue').default
        }
    };
</script>
