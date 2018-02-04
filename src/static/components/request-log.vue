<template>
    <section class="request-log">
        <header class="section">
            <p class="method">GET</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <div class="section request-details">
            <p>GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1</p>
            <p>Host: localhost:3000</p>
            <p>Accept: application/json</p>
        </div>

        <div class="section response-details">
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

        computed: {
            date() {
                const date = new Date(this.data.timestamp);
                return format(date, 'MMM D, YYYY hh:mm:ss A');
            }
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
    }

    .request-details,
    .response-details {
        padding: 0.4rem 0.8rem;
    }
</style>
