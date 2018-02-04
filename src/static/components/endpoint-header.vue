<template>
    <section class="endpoint-header">
        <header>
            <h2>{{ baseUrl }}/<span>{{ hash }}</span></h2>
        </header>
        <div class="switches">
            <labelled-switch label="Live" :checked="isLive" @change="onIsLiveChange"></labelled-switch>
            <labelled-switch label="Auto Response" :checked="autoResponse" @change="onAutoResponseChange"></labelled-switch>
        </div>

        <response-form v-if="autoResponse" @submit="onAutoResponseSubmit"></response-form>
    </section>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        data() {
            return {
                isLive: true,
                autoResponse: true
            };
        },

        computed: mapState(['baseUrl', 'hash']),

        methods: {
            onIsLiveChange(isLive) {
                this.isLive = isLive;
            },

            onAutoResponseChange(autoResponse) {
                this.autoResponse = autoResponse;
            },

            async onAutoResponseSubmit(data) {
                data.responseBody = data.responseBody || '';
                const endpoint = `/${this.hash}/response`;
                const response = await fetch(endpoint, {
                    method: 'POST',
                    body: this.objectToFormData(data)
                }).then(response => response.json());
            },

            objectToFormData(data) {
                const formData = new FormData();
                Object.keys(data).forEach(key => {
                    let value = data[key];
                    if (typeof value === 'object') {
                        value = JSON.stringify(value);
                    }
                    formData.set(key, value);
                });
                return formData;
            }
        },

        components: {
            'labelled-switch': require('./labelled-switch.vue').default,
            'response-form': require('./response-form.vue').default
        }
    };
</script>

<style scoped>
    h2 {
        font-size: 1.8rem;
        font-weight: 300;
        color: var(--gray-3);
    }

    span {
        font-weight: 400;
        color: var(--primary-text-color);
    }

    .switches {
        margin-top: 0.8rem;
    }

    .labelled-switch {
        text-transform: uppercase;
    }

    .labelled-switch:not(:last-child) {
        margin-right: 0.8rem;
    }

    .response-form {
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        margin-top: 0.8rem;
        font-size: 1.2rem;
    }
</style>
