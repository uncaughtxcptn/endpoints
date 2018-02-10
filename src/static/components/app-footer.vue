<template>
    <footer class="app-footer">
        <div class="wrapper">
            <small>
                Developed by
                <a href="https://github.com/uncaughtxcptn" target="_blank" rel="noopener noreferrer">Uncaught Exception</a>
            </small>
        </div>
    </footer>
</template>

<style scoped>
    .app-footer {
        padding: 1.2rem 0;
        border-top: 1px solid var(--gray-1);
        color: var(--gray-2);
    }

    .wrapper {
        text-align: right;
    }

    a {
        text-decoration: none;
        color: var(--gray-3);
    }

    a:hover,
    a:focus {
        text-decoration: underline;
    }
</style>
