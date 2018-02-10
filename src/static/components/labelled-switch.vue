<template>
    <span class="labelled-switch" :class="{ disabled }" @click="toggle">
        <base-switch :checked="isChecked" :disabled="disabled" @change="onChange"></base-switch>
        <span class="label">{{ label }}</span>
    </span>
</template>

<script>
    export default {
        props: {
            checked: {
                type: Boolean,
                default: false
            },
            disabled: {
                type: Boolean,
                default: false
            },
            label: String
        },

        data() {
            return {
                isChecked: this.checked
            };
        },

        watch: {
            isChecked(isChecked) {
                this.$emit('change', isChecked);
            }
        },

        methods: {
            onChange(isChecked) {
                this.isChecked = isChecked;
            },

            toggle() {
                if (!this.disabled) {
                    this.isChecked = !this.isChecked;
                }
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

    .label {
        font-size: 0.8em;
    }

    .disabled .label {
        opacity: 0.5;
    }
</style>
