function createInputElement() {
    const input = document.createElement('input');
    input.type = 'text';
    input.style.position = 'absolute';
    input.style.opacity = 0.01;
    input.style.transform = 'scale(0.01)';
    return input;
}

export function copy(text) {
    return new Promise((resolve, reject) => {
        const input = createInputElement();
        document.body.appendChild(input);

        input.value = text;
        input.select();

        try {
            document.execCommand('copy');
            input.remove();
            resolve();
        } catch (err) {
            reject(err);
        }
    });
};
