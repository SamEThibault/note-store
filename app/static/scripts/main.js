import "https://cdnjs.cloudflare.com/ajax/libs/ace/1.9.5/ace.js"

let editor = document.querySelector("#editor")

ace.edit(editor, {
    theme: 'ace/theme/monokai',
    mode: 'ace/mode/python',
})