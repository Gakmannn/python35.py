let fs = require('fs')
let html = fs.readFileSync('index.html', 'utf8')
let python = fs.readFileSync('funcs.py', 'utf8')

const types = {
  DZ: [],
  PZ: [],
  else: []
}

const now = { name: '', sortName: '', funcBody: '', type: '', module: ''}

let pyArr = python.split('\n')
let name = ''
let funcBody = ''
let first = true
let pyToJs = '<div class="flex">'
for (let string of pyArr) {
  if (string) {
    if (string.startsWith('def')) {
      if (first) {
        first = false
      } else {
        // const code = `<pre><code>${funcBody}</code></pre>`
        // pyToJs += `<div class="code hide"><span>Показать код</span>${code}</div>`
        now.funcBody = funcBody
        if (now.type in types) {
          types[now.type].push({ ...now })
        } else {
          types.else.push({ ...now })
        }
      }
      funcBody = ''
      name = string.split(' ')[1].split('(')[0]

      now.name = name
      now.type = name.split('_')[0]
      now.sortName = isNaN(name.split('_')[1]) ? name.split('_')[0] : +name.split('_')[1]
      // now.sortName = name.split('_').slice(0, 4).join('')
      now.module = name.split('_')[1]

      // const button = `<button py-click="${name}">${name}</button>`
      // pyToJs += `${button}`
    } else {
      if (string) funcBody += string + '\n'
    }
  }

}
// const code = `<pre><code>${funcBody}</code></pre>`
// pyToJs += `<div class="code hide"><span>Показать код</span>${code}</div>`
now.funcBody = funcBody
if (now.type in types) {
  types[now.type].push({ ...now })
} else {
  types.else.push({ ...now })
}

for (let type in types) {
  types[type].sort((a, b) => {
    if (isNaN(a.sortName)) {
      return a.sortName.toString().localeCompare(b.sortName.toString())
      }
    return a.sortName - b.sortName
  })
  if (types[type].length) {
    const name = type == 'DZ' ? 'Домашние задания' : type == 'PZ' ? 'Практические задания' : 'Остальные задания'
    pyToJs += `<div><h2>${name}</h2>`
    let currentModule = 0
    let isModule = false
    for (el of types[type]) {
      if (currentModule != el.module) {
        if (isModule) {
          pyToJs += '</div>'
          isModule = false
        }
        if (types[type].filter(el1 => el1.module == el.module).length>1) {
          currentModule = el.module
          isModule = true
          pyToJs += `<div class="module close">Модуль ${el.module}<p>Открыть</p><br>`
        }
      }
      const button = `<button py-click="${el.name}">${el.name}</button>`
      const code = `<pre><code>${el.funcBody.replaceAll('>', '&gt;').replaceAll('<', '&lt;') }</code></pre>`
      pyToJs += `${button}<div class="code hide"><span>Показать код</span>${code}</div>`
    }
    if (isModule) {
      pyToJs += '</div>'
      isModule = false
    }
    pyToJs += '</div>'
  }  
}

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

pyToJs += '</div>' // flex
const htmlStart = html.split('<div id="output">')[0] + '<div id="output">'
const htmlEnd = '</div><div id="outputEnd">'+html.split('<div id="outputEnd">')[1]

fs.writeFileSync('index.html', htmlStart + pyToJs + htmlEnd)