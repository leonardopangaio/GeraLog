const fs = require('fs/promises');
const path = require('path');

const currentDate = new Date();
const year = currentDate.getFullYear();
const month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Meses começam do zero, por isso somamos 1
const day = String(currentDate.getDate()).padStart(2, '0'); // Garante que o dia tenha 2 dígitos
const now = `${('0' + currentDate.getHours()).slice(-2)}${('0' + currentDate.getMinutes()).slice(-2)}${('0' + currentDate.getSeconds()).slice(-2)}`;

async function GeraLog(type, message) {
    const date=new Date();
    const formattedDateTime = `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).slice(-2)}-${('0' + date.getDate()).slice(-2)} ${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)}.${date.getMilliseconds()}`;

    const logDirectory = path.join(__dirname, 'logs', year.toString(), month, day);
    const logFileName = `LogFileName_${now}.log`;
    const FullLogPath = path.join(logDirectory,logFileName);

    const error = new Error();
    const stackLines = error.stack.split('\n');
    const callerLine = stackLines[2] || '';
    const functionMatch = callerLine.match(/at (.+) \(/);
    const functionName = functionMatch ? functionMatch[1] : 'anonymous';
    // const locationMatch = callerLine.match(/\((.*):(\d+):(\d+)\)/);
    // const location = locationMatch ? `${locationMatch[1]}:${locationMatch[2]}` : 'unknown';

    try {
        // Verifica se o diretório já existe
        await fs.access(logDirectory);
    } catch (err) {
        // Caso não exista, cria a estrutura de diretórios
        await fs.mkdir(logDirectory, { recursive: true });
    }

    const FormattedMessage = `${formattedDateTime} - [${functionName}] - [${type}] - ${message}`;

    await fs.appendFile(FullLogPath, FormattedMessage);
    console.log(FormattedMessage);

};