let fs = require('fs')
let html = fs.readFileSync('index.html', 'utf8')
let python = fs.readFileSync('funcs.py', 'utf8')

const pythonArr = python.split('def ')
let pyToJs = ''
for (let i = 1; i < pythonArr.length; i++) {
  const name = pythonArr[i].split('(event)')[0]
  const funcArr = pythonArr[i].split(':')
  funcArr.shift()
  const funcBody = funcArr.join(':')
  const button = `<button py-click="${name}">${name}</button>`
  const code = `<pre><code>${funcBody}</code></pre>`
  pyToJs += `${button}<div class="code hide"><span>Показать код</span>${code}</div>`
}

const htmlStart = html.split('<div id="output">')[0] + '<div id="output">'
const htmlEnd = '</div><div id="outputEnd">'+html.split('<div id="outputEnd">')[1]

fs.writeFileSync('index.html', htmlStart + pyToJs + htmlEnd)