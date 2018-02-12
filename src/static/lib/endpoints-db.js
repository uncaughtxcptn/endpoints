import idb from 'idb';

const db = idb.open('endpoints', 1, upgradeDb => {
    switch (upgradeDb.oldVersion) {
        case 0:
            upgradeDb.createObjectStore('endpoints')
    }
});

export default db;
