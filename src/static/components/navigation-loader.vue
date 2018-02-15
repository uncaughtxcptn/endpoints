<template>
    <div class="navigation-loader"></div>
</template>

<style scoped>
    .navigation-loader {
        width: 100%;
        height: 0.2rem;
        background: repeating-linear-gradient(
            to right,
            var(--primary-color) 0%,
            var(--primary-color) 50%,
            #fff 50%,
            #fff 150%
        );
    }
</style>
