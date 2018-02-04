<template>
    <section class="request-log">
        <header class="section" @click="toggleExpanded">
            <p class="method">{{ method }}</p>
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
        justify-content: space-between;
        padding: 0.4rem 0.8rem;
        cursor: pointer;
    }
</style>
