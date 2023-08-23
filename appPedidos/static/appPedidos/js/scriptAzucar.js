/*buttons*/

const sinAzucarButton= document.getElementById('sinAzucarButton')
const unoAzucarButton= document.getElementById('unoAzucarButton')
const dosAzucarButton= document.getElementById('dosAzucarButton')
const tresAzucarButton= document.getElementById('tresAzucarButton')

const inputAzucar = document.getElementById('inputAzucar')




sinAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Sin Azucar'
})

unoAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Uno de Azucar'
})

dosAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Dos de Azucar'
})


tresAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Tres de Azucar'
})






