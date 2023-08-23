const coffeSmall= document.getElementById('coffeSmall')
const coffeSmallImg= document.getElementById('coffeSmallImg')


const coffeMedium= document.getElementById('coffeMedium')
const coffeMediumImg= document.getElementById('coffeMediumImg')

const coffeLarge= document.getElementById('coffeLarge')
const coffeLargeImg= document.getElementById('coffeLargeImg')

/* valor del producto */
const valorProducto = document.getElementById('valorProducto')


/*inputs*/
const inputCafe = document.getElementById('inputCafe')



coffeSmall.addEventListener('click',()=>{
    console.log(coffeSmall.value)
    coffeSmallImg.style.fill='black'
    coffeMediumImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
    inputCafe.value= 'Cafe chico'
    
})

coffeMedium.addEventListener('click',()=>{
    console.log(coffeMedium.value)
    coffeMediumImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
    inputCafe.value= 'Cafe Mediano'
})

coffeLarge.addEventListener('click',()=>{
    console.log(coffeLarge.value)
    coffeLargeImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeMediumImg.style.fill='grey'
    inputCafe.value= 'Cafe Grande'
})










