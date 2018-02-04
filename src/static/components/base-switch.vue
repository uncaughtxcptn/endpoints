<template>
    <label class="base-switch">
        <input type="checkbox" v-model="isChecked">
        <span class="switch"></span>
    </label>
</template>

<script>
    export default {
        props: ['checked'],

        data() {
            return {
                isChecked: this.checked
            };
        },

        watch: {
            checked(checked) {
                this.isChecked = checked;
            },

            isChecked(isChecked) {
                this.$emit('change', isChecked);
            }
        }
    };
</script>

<style scoped>
    .base-switch {
        display: inline-block;
        position: relative;
        font-size: 0.9em;
    }

    input {
        position: absolute;
        opacity: 0.01;
        transform: scale(0.01);
    }

    .switch {
        display: block;
        width: 2em;
        height: 1em;
        border: 1px solid currentColor;
        border-radius: 2px;
        position: relative;
        color: var(--gray-1);
        cursor: pointer;
        transition: color 150ms ease;
    }

    .switch::before {
        content: "";
        width: calc(1em - 1px);
        height: calc(1em - 2px);
        border-radius: 1px;
        position: absolute;
        top: 1px;
        left: 1px;
        background-color: currentColor;
        transition: left 150ms ease;
    }

    input:checked + .switch {
        color: var(--primary-color);
    }

    input:checked + .switch::before {
        left: 50%;
    }
</style>
