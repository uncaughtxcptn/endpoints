<template>
    <div class="response-details">
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
                return this.data
                    ? this.data.trim().split(/\n/g).map(line => line.trim())
                    : [];
            }
        }
    };
</script>

<style scoped>
    .response-details {
        padding: 0.4rem 0.8rem;
    }
</style>
