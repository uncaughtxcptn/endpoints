<template>
    <section class="request-log">
        <header class="section" @click="toggleExpanded">
            <p class="method">{{ method }}</p>
            <p class="status">{{ status }}</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <request-details class="section" v-if="isExpanded" :data="data.request"></request-details>
        <response-details class="section" v-if="isExpanded" :data="data.response"></response-details>
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
                const date = new Date(this.data.timestamp);
                return format(date, 'MMM D, YYYY hh:mm:ss A');
            }
        },

        methods: {
            toggleExpanded() {
                this.isExpanded = !this.isExpanded;
            }
        },

        components: {
            'request-details': require('./request-details.vue').default,
            'response-details': require('./response-details.vue').default
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

    .timestamp {
        margin-left: auto;
    }
</style>
