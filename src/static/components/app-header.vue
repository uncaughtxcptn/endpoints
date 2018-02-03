<template>
    <header class="app-header">
        <div class="wrapper">
            <router-link :to="{ name: 'landing-page' }" class="logo">Endpoints</router-link>
            <button>Create Endpoint</button>
        </div>
    </header>
</template>

<style scoped>
    .app-header {
        padding: 1.6rem 0;
        border-bottom: 1px solid var(--gray-1);
    }

    .wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: auto;
    }

    .logo {
        font-size: 1.8rem;
        font-weight: 300;
        text-decoration: none;
    }

    button {
        padding: 8px 16px;
        border: 1px solid var(--primary-color-dark-1);
        border-radius: 2px;
        font-size: 14px;
        text-transform: uppercase;
        color: #fff;
        background-color: var(--primary-color);
        cursor: pointer;
    }
</style>
