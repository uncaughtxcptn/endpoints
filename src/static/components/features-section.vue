<template>
    <section class="features-section">
        <div class="wrapper">
            <h2>Features</h2>

            <div class="features">
                <div class="feature">
                    <div class="img-placeholder"></div>
                    <h4>Realtime Request Logs</h4>
                    <p>See HTTP requests sent to your endpoint in realtime.</p>
                </div>

                <div class="feature">
                    <div class="img-placeholder"></div>
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

    .img-placeholder {
        background-color: var(--gray-1);
    }

    .img-placeholder::before {
        content: "";
        display: block;
        padding-top: calc(100% / 16 * 5);
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
