let fs = require('fs')
let html = fs.readFileSync('index.html', 'utf8')
let python = fs.readFileSync('funcs.py', 'utf8')

let pyArr = python.split('\n')
let name = ''
let funcBody = ''
let first = true
let pyToJs = ''
for (let string of pyArr) {
  if (string) {
    if (string.startsWith('def')) {
      if (first) {
        first = false
      } else {
        const code = `<pre><code>${funcBody}</code></pre>`
        pyToJs += `<div class="code hide"><span>Показать код</span>${code}</div>`
      }
      funcBody = ''
      name = string.split(' ')[1].split('(')[0]
      const button = `<button py-click="${name}">${name}</button>`
      pyToJs += `${button}`
    } else {
      if (string) funcBody += string + '\n'
    }
  }

}
const code = `<pre><code>${funcBody}</code></pre>`
pyToJs += `<div class="code hide"><span>Показать код</span>${code}</div>`

// const pythonArr = python.split('def ')
// let pyToJs = ''
// for (let i = 1; i < pythonArr.length; i++) {
//   const name = pythonArr[i].split('(event)')[0]
//   const funcArr = pythonArr[i].split(':')
//   funcArr.shift()
//   const funcBody = funcArr.join(':')
//   const button = `<button py-click="${name}">${name}</button>`
//   const code = `<pre><code>${funcBody}</code></pre>`
//   pyToJs += `${button}<div class="code hide"><span>Показать код</span>${code}</div>`
// }

const htmlStart = html.split('<div id="output">')[0] + '<div id="output">'
const htmlEnd = '</div><div id="outputEnd">'+html.split('<div id="outputEnd">')[1]

fs.writeFileSync('index.html', htmlStart + pyToJs + htmlEnd)