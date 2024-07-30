#!/usr/bin/node
const filepath = process.argv[2];
const fs = require('fs');

fs.readFile(filepath, 'utf-8', (err, data) => {
    if (err) {
        if (err.code === 'ENOENT') {
            console.error(`Error: File not found - ${filepath}`);
        }
        process.exit(1);
    } else {
        console.log(data);
    }
});