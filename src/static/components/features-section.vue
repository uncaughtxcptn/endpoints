<template>
    <section class="features-section">
        <div class="wrapper">
            <h2>Features</h2>

            <div class="features">
                <div class="feature">
                    <img src="~images/feature-1.png" alt="Realtime Request Logs">
                    <h4>Realtime Request Logs</h4>
                    <p>See HTTP requests sent to your endpoint in realtime.</p>
                </div>

                <div class="feature">
                    <img src="~images/feature-2.png" alt="Customizeable Responses">
                    <h4>Customizeable Responses</h4>
                    <p>Respond with custom status codes, response headers, and body.</p>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
    .features-section {
        padding: 4rem 0;
    }

    h2 {
        margin-bottom: 4rem;
        font-size: 1.8rem;
        font-weight: 300;
        text-transform: uppercase;
        text-align: center;
        letter-spacing: 2px;
        color: var(--gray-3);
    }

    .features {
        display: flex;
    }

    .feature {
        width: 50%;
        padding: 0 1rem;
        text-align: center;
    }

    img {
        padding: 3px;
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        opacity: 0.5;
        transition: opacity 200ms ease;
    }

    .feature:hover img {
        opacity: 1;
    }

    h4 {
        margin: 1.2rem 0;
        font-size: 1.6rem;
        font-weight: 500;
    }

    p {
        font-weight: 300;
        color: var(--gray-3);
    }
</style>
