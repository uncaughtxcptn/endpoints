<template>
    <section class="request-log">
        <header class="section" @click="toggleExpanded">
            <p class="method">{{ method }}</p>
            <p v-if="status" class="status" :class="getStatusCodeClass(status)">{{ status }}</p>
            <p v-else class="no-status">No Response</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <request-details class="section" v-if="isExpanded" :data="data.request"></request-details>
        <response-details class="section" v-if="isExpanded && data.response" :data="data.response"></response-details>
        <response-form class="section" v-if="isExpanded && !data.response" @submit="onResponse"></response-form>
    </section>
</template>

<script>
    import format from 'date-fns/format';

    export default {
        props: ['data'],

        data() {
            return {
                isExpanded: false
            };
        },

        computed: {
            method() {
                return this.data.request.trim().match(/^[A-Z]+/)[0];
            },

            status() {
                return this.data.response
                    ? this.data.response.trim().match(/\d+ [a-zA-Z\s]+(?=\n|$)/)[0]
                    : null;
            },

            date() {
                const date = new Date(this.data.when);
                return format(date, 'MMM D, YYYY hh:mm:ss A');
            }
        },

        methods: {
            toggleExpanded() {
                this.isExpanded = !this.isExpanded;
            },

            getStatusCodeClass(status) {
                const statusCode = parseInt(status.match(/^\d+/), 10);
                if (statusCode < 400) {
                    return 'status-success';
                } else if (statusCode < 500) {
                    return 'status-warning';
                } else {
                    return 'status-error';
                }
            },

            onResponse(response) {
                this.$store.dispatch('setResponse', {
                    id: this.data.id,
                    response
                });
            }
        },

        components: {
            'request-details': require('./request-details.vue').default,
            'response-details': require('./response-details.vue').default,
            'response-form': require('./response-form.vue').default
        }
    };
</script>

<style scoped>
    .request-log {
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        font-size: 1.2rem;
        background-color: #fff;
    }

    .section:not(:last-child) {
        border-bottom: 1px solid var(--gray-1);
    }

    header {
        display: flex;
        padding: 0.4rem 0.8rem;
        cursor: pointer;
    }

    .method {
        margin-right: 1.6rem;
    }

    .status-success {
        color: var(--success-color);
    }

    .status-warning {
        color: var(--warning-color);
    }

    .status-error {
        color: var(--error-color);
    }

    .no-status {
        padding: 0 0.4rem;
        border-radius: 2px;
        text-transform: uppercase;
        color: #fff;
        background-color: var(--error-color);
    }

    .timestamp {
        margin-left: auto;
    }
</style>
