import idb from 'idb';

const db = idb.open('endpoints', 1, upgradeDb => {
    switch (upgradeDb.oldVersion) {
        case 0:
            upgradeDb.createObjectStore('endpoints')
    }
});

export function put(data) {
    data = Object.assign({}, data, { timestamp: Date.now() });
    return db.then(db => {
        const transaction = db.transaction('endpoints', 'readwrite');
        transaction.objectStore('endpoints').put(data)
        return transaction.complete;
    });
}
