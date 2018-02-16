<template>
    <div class="navigation-loader" :class="{ visible: isLoadingNavigation }">
        <div ref="progress" class="progress"></div>
    </div>
</template>

<script>
    import { mapState } from 'vuex';

    export default {
        data() {
            return {
                animation: null
            };
        },

        computed: mapState(['isLoadingNavigation']),

        watch: {
            isLoadingNavigation(isLoadingNavigation) {
                if (isLoadingNavigation) {
                    this.play();
                } else {
                    this.finish();
                }
            }
        },

        methods: {
            play() {
                this.animation.play();
                this.animation.addEventListener('finish', this.play, { once: true });
            },

            finish() {
                this.animation.finish();
                this.animation.removeEventListener('finish', this.play);
            }
        },

        mounted() {
            this.animation = this.$refs.progress.animate([
                { left: '-50%' },
                { left: '100%', easing: 'ease-out' }
            ], 1500);
            this.animation.cancel();

            if (this.isLoadingNavigation) {
                this.play();
            }
        }
    };
</script>

<style scoped>
    .navigation-loader {
        width: 100%;
        height: 0.2rem;
    }

    .navigation-loader:not(.visible) {
        display: none;
    }

    .progress {
        position: absolute;
        top: 0;
        left: -50%;
        width: 50%;
        height: 100%;
        background-color: var(--primary-color);
    }
</style>
