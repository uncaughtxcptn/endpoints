import idb from 'idb';

const db = idb.open('endpoints', 1, upgradeDb => {
    switch (upgradeDb.oldVersion) {
        case 0:
            upgradeDb.createObjectStore('endpoints', { keyPath: 'id' });
    }
});

export function put(data) {
    data = Object.assign({}, data, { timestamp: Date.now() });
    return db.then(db => {
        const transaction = db.transaction('endpoints', 'readwrite')
            .objectStore('endpoints')
            .put(data)
        return transaction.complete;
    });
}

export function getAll() {
    return db.then(db => {
        const endpoints = [];
        const transaction = db.transaction('endpoints');
        transaction.objectStore('endpoints')
            .openCursor(null, 'prev')
            .then(function iterate(cursor) {
                if (!cursor) return;
                endpoints.push(cursor.value);
                cursor.continue().then(iterate);
            });
        return transaction.complete.then(() => endpoints);
    });
}
