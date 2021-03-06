<template>
    <section class="endpoint-header">
        <header>
            <h2>{{ baseUrl }}/<span>{{ hash }}</span></h2>
            <button class="copy-btn" @click="copyEndpoint"></button>
        </header>
        <div class="switches">
            <labelled-switch label="Live" :checked="isLive" @change="updateLiveStatus"></labelled-switch>
            <labelled-switch label="Auto Response" :checked="willAutoResponse" :disabled="true" @change="onAutoResponseChange"></labelled-switch>
        </div>

        <response-form
            v-if="willAutoResponse"
            @submit="onAutoResponseSubmit"
            :status-code="autoResponse.statusCode"
            :headers="autoResponse.headers"
            :response-body="autoResponse.responseBody">
        </response-form>
    </section>
</template>

<script>
    import { mapState, mapActions } from 'vuex';
    import { copy } from '../lib/clipboard';

    export default {
        data() {
            return {
                willAutoResponse: true
            };
        },

        computed: mapState(['baseUrl', 'hash', 'isLive', 'autoResponse']),

        methods: {
            ...mapActions(['updateLiveStatus']),

            onAutoResponseChange(autoResponse) {
                this.willAutoResponse = autoResponse;
            },

            onAutoResponseSubmit(data) {
                this.$store.dispatch('setAutoResponse', data);
                this.$ga.event('endpoints', 'set-auto-response');
            },

            copyEndpoint() {
                const endpoint = window.location.protocol + '//' + this.baseUrl + '/' + this.hash;
                copy(endpoint);
            }
        },

        components: {
            'labelled-switch': require('./labelled-switch.vue').default,
            'response-form': require('./response-form.vue').default
        }
    };
</script>

<style scoped>
    header {
        display: flex;
        align-items: center;
    }

    h2 {
        font-size: 1.8rem;
        font-weight: 300;
        color: var(--gray-3);
    }

    span {
        font-weight: 400;
        color: var(--primary-text-color);
    }

    .copy-btn {
        flex-shrink: 0;
        width: 2.4rem;
        height: 2.4rem;
        border: none;
        margin-left: 0.8rem;
        background: url("~images/copy.png") center center no-repeat;
        background-size: 65%;
        opacity: 0.25;
        cursor: pointer;
        transition: opacity 150ms ease;
    }

    .copy-btn:hover,
    .copy-btn:focus {
        opacity: 0.5;
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

    @media (max-width: 600px) {
        header {
            align-items: flex-end;
        }

        h2 {
            font-size: 1.6rem;
        }

        span {
            display: block;
        }
    }

    @media (max-width: 500px) {
        h2 {
            font-size: 1.4rem;
        }
    }
</style>
