const fs = require('fs');
const { exec } = require("child_process");
let rawdata = fs.readFileSync('this_is_literally_the_longest_name_for_a_unnecessarily_meaningless_file.json');
let data = JSON.parse(rawdata);
let str = data['encrypted'];
let encodedStr = Buffer.from(str).toString('base64');
fs.writeFileSync('base64.json', `{"encrypted": "${encodedStr}"}`);
exec("python3 main.py", (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});
