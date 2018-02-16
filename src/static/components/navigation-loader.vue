<template>
    <div class="navigation-loader">
        <div ref="progress" class="progress"></div>
    </div>
</template>

<script>
    export default {
        methods: {
            animate() {
                return this.$refs.progress.animate([
                    { left: '-50%', easing: 'ease-in' },
                    { left: '100%', easing: 'ease-out' }
                ], 1500);
            }
        },

        mounted() {
            const animateLoop = () => {
                this.animate().onfinish = animateLoop;
            };
            animateLoop();
        }
    };
</script>

<style scoped>
    .navigation-loader {
        width: 100%;
        height: 0.2rem;
    }

    .progress {
        position: absolute;
        top: 0;
        left: 0;
        width: 50%;
        height: 100%;
        background-color: var(--primary-color);
    }
</style>
