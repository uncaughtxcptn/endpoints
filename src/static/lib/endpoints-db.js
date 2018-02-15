let idb;

function database() {
    if (idb) {
        return Promise.resolve(idb);
    }

    return new Promise((resolve, reject) => {
        const request = indexedDB.open('endpoints', 1);
        request.onupgradeneeded = (e) => {
            const upgradeDb = e.target.result;

            switch (e.oldVersion) {
                case 0:
                    upgradeDb.createObjectStore('endpoints', { keyPath: 'id' });
            }
        };
        request.onsuccess = (e) => {
            idb = e.target.result;
            resolve(idb);
        };
        request.onerror = reject;
    });
}

export function put(data) {
    data = Object.assign({}, data, { timestamp: Date.now() });

    return database().then(db => new Promise((resolve, reject) => {
        const transaction = db.transaction('endpoints', 'readwrite');
        const store = transaction.objectStore('endpoints');
        const request = store.put(data);

        request.onsuccess = () => resolve(data);
        request.onerror = reject;
    }));
}

export function getAll() {
    return database().then(db => new Promise((resolve, reject) => {
        const transaction = db.transaction('endpoints');
        const store = transaction.objectStore('endpoints');
        const request = store.openCursor(null, 'prev');
        const endpoints = [];

        request.onsuccess = (e) => {
            const cursor = e.target.result;
            if (cursor) {
                endpoints.push(cursor.value);
                cursor.continue();
            } else {
                resolve(endpoints);
            }
        };
        request.onerror = reject;
    }));
}
