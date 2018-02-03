<template>
    <div class="landing-page">
        <button @click="onClick">Create Endpoint</button>
    </div>
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
