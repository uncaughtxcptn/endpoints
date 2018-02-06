<template>
    <button class="pending-counter" v-if="count" @click="onClick">{{ count }} New Request Logs</button>
</template>

<script>
    export default {
        props: {
            count: {
                type: Number,
                default: 0
            }
        },

        methods: {
            onClick(e) {
                this.$emit('click', e);
            }
        }
    };
</script>

<style scoped>
    .pending-counter {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border: 1px solid var(--primary-color);
        border-radius: 2px;
        margin-bottom: 0.8rem;
        font-size: 1.2rem;
        color: var(--primary-color-dark-1);
        background-color: #fff;
        cursor: pointer;
    }
</style>
