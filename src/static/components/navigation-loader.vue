<template>
    <div class="navigation-loader">
        <div class="progress"></div>
    </div>
</template>

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
