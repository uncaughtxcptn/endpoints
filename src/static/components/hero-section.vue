<template>
    <section class="hero-section">
        <div class="wrapper">
            <h3><span>Endpoints</span> allows you to view and respond to requests on an HTTP endpoint.</h3>
        </div>
    </section>
</template>

<style scoped>
    .hero-section {
        border-bottom: 1px solid var(--gray-1);
        text-align: center;
        background-color: var(--gray-0);
    }

    .wrapper {
        padding: 8rem 12rem;
    }

    h3 {
        font-weight: 100;
    }

    span {
        color: var(--primary-color);
    }

    @media (max-width: 600px) {
        .wrapper {
            padding: 8rem 6rem;
        }
    }

    @media (max-width: 450px) {
        .wrapper {
            padding: 6rem 3rem;
        }
    }
</style>
