<template>
    <section class="request-log">
        <header>
            <p class="method">GET</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <div class="request-details">
            <p>GET /abcdefghijklmnopqrstuvwxyz HTTP/1.1</p>
            <p>Host: localhost:3000</p>
            <p>Accept: application/json</p>
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

    header {
        display: flex;
        justify-content: space-between;
        padding: 0.4rem 0.8rem;
        border-bottom: 1px solid var(--gray-1);
    }

    .request-details {
        padding: 0.4rem 0.8rem;
    }
</style>
