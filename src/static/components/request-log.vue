<template>
    <section class="request-log">
        <header class="section" @click="toggleExpanded">
            <p class="method">GET</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <request-details class="section" v-if="isExpanded" :data="data.request"></request-details>

        <div v-if="isExpanded" class="section response-details">
            <p>HTTP/1.1 200 OK</p>
            <p>Content-Type: application-json</p>
            <p>Content-Length: 100</p>
            <p>Cache-Control: public, max-age=10000</p>
            <p>Etag: w/kdi283lsldjlsjds</p>
            <br>
            <p>{"title":"Hello World"}</p>
        </div>
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
            'request-details': require('./request-details.vue').default
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

    .response-details {
        padding: 0.4rem 0.8rem;
    }
</style>
