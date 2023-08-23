const coffeSmall= document.getElementById('coffeSmall')
const coffeSmallImg= document.getElementById('coffeSmallImg')


const coffeMedium= document.getElementById('coffeMedium')
const coffeMediumImg= document.getElementById('coffeMediumImg')

const coffeLarge= document.getElementById('coffeLarge')
const coffeLargeImg= document.getElementById('coffeLargeImg')

/*azucar opcion*/
const sinAzucarButton= document.getElementById('sinAzucarButton')
const unoAzucarButton= document.getElementById('unoAzucarButton')
const dosAzucarButton= document.getElementById('dosAzucarButton')
const tresAzucarButton= document.getElementById('tresAzucarButton')

/*canela y crema*/
const conCanelaButton= document.getElementById('conCanelaButton')
const conCremaButton= document.getElementById('conCremaButton')



coffeSmall.addEventListener('click',()=>{
    console.log(coffeSmall.value)
    coffeSmallImg.style.fill='black'
    coffeMediumImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
})

coffeMedium.addEventListener('click',()=>{
    console.log(coffeMedium.value)
    coffeMediumImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
})

coffeLarge.addEventListener('click',()=>{
    console.log(coffeLarge.value)
    coffeLargeImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeMediumImg.style.fill='grey'
})


sinAzucarButton.addEventListener('click',()=>{
    console.log(sinAzucarButton.value)
})

unoAzucarButton.addEventListener('click',()=>{
    console.log(unoAzucarButton.value)
})

dosAzucarButton.addEventListener('click',()=>{
    console.log(dosAzucarButton.value)
})



tresAzucarButton.addEventListener('click',()=>{
    console.log(tresAzucarButton.value)
})


conCanelaButton.addEventListener('click',()=>{
    console.log(conCanelaButton.value)
})

conCremaButton.addEventListener('click',()=>{
    console.log(conCremaButton.value)
})









