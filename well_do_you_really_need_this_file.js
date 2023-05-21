const fs = require('fs');

let rawdata = fs.readFileSync('this_is_literally_the_longest_name_for_a_unnecessarily_meaningless_file.json');
let data = JSON.parse(rawdata);

let str = data['encrypted'];
let encodedStr = Buffer.from(str).toString('base64');

fs.writeFileSync('base64.json', `{"encrypted": "${encodedStr}"}`);
