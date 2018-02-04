<template>
    <label class="labelled-switch">
        <base-switch :checked="checked" @change="onChange"></base-switch>
        <span>{{ label }}</span>
    </label>
</template>

<script>
    export default {
        props: ['checked', 'label'],

        methods: {
            onChange(isChecked) {
                this.$emit('change', isChecked);
            }
        },

        components: {
            'base-switch': require('./base-switch.vue').default
        }
    };
</script>

<style scoped>
    .labelled-switch {
        display: inline-flex;
        align-items: center;
        cursor: pointer;
    }

    .base-switch {
        margin-right: 0.4rem;
    }

    span {
        font-size: 0.8em;
    }
</style>
