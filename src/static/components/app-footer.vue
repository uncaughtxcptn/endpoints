<template>
    <footer class="app-footer">
        <div class="wrapper">
            <small>
                Developed by
                <a href="https://github.com/uncaughtxcptn" target="_blank" rel="noopener noreferrer">Uncaught Exception</a>
            </small>
            <a class="github-link" href="https://github.com/uncaughtxcptn/endpoints" target="_blank" rel="noopener noreferrer"></a>
        </div>
    </footer>
</template>

<style scoped>
    .app-footer {
        padding: 3.6rem 0;
        color: var(--gray-2);
    }

    .wrapper {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    a {
        text-decoration: none;
        color: var(--gray-3);
    }

    a:hover,
    a:focus {
        text-decoration: underline;
    }

    .github-link {
        display: inline-block;
        width: 1.25em;
        height: 1.25em;
        margin-left: 1.6rem;
        background: url("~images/github.png") center center no-repeat;
        background-size: cover;
        opacity: 0.35;
        transition: opacity 150ms ease;
    }

    .github-link:hover,
    .github-link:focus {
        opacity: 0.75;
    }
</style>
