export function objectToFormData(data) {
    const formData = new FormData();
    Object.keys(data).forEach(key => {
        let value = data[key];
        if (typeof value === 'object') {
            value = JSON.stringify(value);
        }
        formData.set(key, value);
    });
    return formData;
};
