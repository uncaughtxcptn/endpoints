<template>
    <div class="request-details">
        <template v-for="line in lines">
            <p v-if="line.length">{{ line }}</p>
            <br v-else>
        </template>
    </div>
</template>

<script>
    export default {
        props: ['data'],

        computed: {
            lines() {
                return this.data.split(/\n/g);
            }
        }
    };
</script>

<style scoped>
    .request-details {
        padding: 0.4rem 0.8rem;
        overflow: auto;
    }
</style>
