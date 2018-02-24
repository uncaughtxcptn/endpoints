<template>
    <button class="base-button" :class="{ loading }" :type="type" @click="onClick">
        <slot></slot>
    </button>
</template>

<script>
    export default {
        props: {
            loading: Boolean,
            type: {
                type: String,
                default: 'button'
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

    .mini {
        padding: 0.167em 0.33em;
    }

    .loading {
        position: relative;
        color: transparent;
        opacity: 0.5;
        pointer-events: none;
    }

    .loading::before {
        content: "";
        width: 1.2em;
        height: 1.2em;
        border: 1px solid transparent;
        border-left-color: var(--primary-text-color);
        border-right-color: var(--primary-text-color);
        border-radius: 50%;
        position: absolute;
        top: calc(50% - 0.6em);
        left: calc(50% - 0.6em);
        animation: rotate 500ms linear infinite;
    }

    .primary.loading::before {
        border-left-color: #fff;
        border-right-color: #fff;
    }

    @keyframes rotate {
        to {
            transform: rotate(360deg);
        }
    }
</style>
