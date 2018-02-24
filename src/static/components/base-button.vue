<template>
    <button class="base-button" @click="onClick">
        <slot></slot>
    </button>
</template>

<script>
    export default {
        props: ['loading'],

        methods: {
            onClick(e) {
                this.$emit('click', e);
            }
        }
    };
</script>

<style scoped>
    button {
        padding: 0.5em 1em;
        border-radius: 2px;
        font-size: 1.3rem;
        text-transform: uppercase;
        cursor: pointer;

        /* Default button styles */
        border: 1px solid var(--gray-1);
    }

    .primary {
        border: 1px solid var(--primary-color-dark-1);
        color: #fff;
        background-color: var(--primary-color);
    }
</style>
