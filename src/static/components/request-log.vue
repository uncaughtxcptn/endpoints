<template>
    <section class="request-log">
        <header>
            <p class="method">GET</p>
            <time class="timestamp" :datetime="data.timestamp">{{ date }}</time>
        </header>

        <p>Request Log</p>
    </section>
</template>

<script>
    import format from 'date-fns/format';

    export default {
        props: ['data'],

        computed: {
            date() {
                const date = new Date(this.data.timestamp);
                return format(date, 'MMM D, YYYY hh:mm:ss a');
            }
        }
    };
</script>
