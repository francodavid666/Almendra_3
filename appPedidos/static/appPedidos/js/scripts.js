/* doms*/
const coffeSmall= document.getElementById('coffeSmall')
const coffeSmallImg= document.getElementById('coffeSmallImg')


const coffeMedium= document.getElementById('coffeMedium')
const coffeMediumImg= document.getElementById('coffeMediumImg')

const coffeLarge= document.getElementById('coffeLarge')
const coffeLargeImg= document.getElementById('coffeLargeImg')

/*candidad*/
const valorInput = document.getElementById('inputCantidad');
const buttonAdd = document.getElementById('buttonAdd')
const buttonSubt = document.getElementById('buttonSubt')
const valor = valorInput.value;


/*cantidad*/

/*Azucar*/

const sinAzucarButton= document.getElementById('sinAzucarButton')
const unoAzucarButton= document.getElementById('unoAzucarButton')
const dosAzucarButton= document.getElementById('dosAzucarButton')
const tresAzucarButton= document.getElementById('tresAzucarButton')

const inputAzucar = document.getElementById('inputAzucar')
/*Azucar*/

/*adicional*/
/*button*/
const conCanelaButton= document.getElementById('conCanelaButton')
const conCremaButton= document.getElementById('conCremaButton')

/*inputs*/
const inputAdicional = document.getElementById('inputAdicional')
/*adicional*/


/*total */
/*Input total */
const inputTotal = document.getElementById('inputTotal')

/* valor del producto */
const valorProducto = document.getElementById('valorProducto')

inputTotal.value =0

let a = valorProducto.textContent
console.log(a)
/*total */

let totalArray = [0]
let valorTamanio = [0]
/**cantidad */
buttonAdd.addEventListener("click",()=>{
    if(valorInput.value == 3){
      
    }else{
        valorInput.value= parseInt(valorInput.value) +1;
        console.log(valorInput.value)
       
    const valorTotalCantidad = parseInt(totalArray)+ parseInt(a)
    totalArray[0]= valorTotalCantidad
    

    console.log(`El valor de cantidad'${totalArray}'`)
    console.log(`El valor de tamaño'${valorTamanio}'`)
    let totalFinal = parseInt(totalArray) + parseInt(valorTamanio)
    inputTotal.value = parseInt(totalFinal)
    
     
    }   
})

buttonSubt.addEventListener("click",()=>{
    if(valorInput.value!=0){
        valorInput.value= parseInt(valorInput.value) -1;
        console.log(valorInput.value)
        const valorTotalCantidad =  parseInt(totalArray)- parseInt(a)
        console.log(valorTotalCantidad)
        totalArray[0]= valorTotalCantidad
        console.log(`El valor de cantidad'${totalArray}'`)
        console.log(`El valor de tamaño' ${valorTamanio}'`)
        let totalFinal = parseInt(totalArray)
    inputTotal.value = parseInt(totalFinal)
    console.log(inputTotal.value = parseInt(totalFinal))
   
     //   totalArray[0]= valorTotalCantidad     
    }
    else{
        
    }


})
/*cantidad*/

 const total = 0
 console.log(total)

/*tamaño */
const tamanioPrecio = document.getElementById('inputTamanioPrecio')

coffeSmall.addEventListener('click',()=>{
    console.log(a)
    coffeSmallImg.style.fill='black'
    coffeMediumImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
    inputCafe.value= 'Cafe chico'


    let total = 0 
    tamanioPrecio.value = parseInt(total) 
    let nuevo = total + 0
    valorTamanio[0]=nuevo
    //totalArray[0]= valorTotalCantidad
    console.log(`El valor de cantidad'${totalArray}'`)
    console.log(`El valor de tamaño'${valorTamanio}'`)
    tamanioPrecio.value = parseInt(valorTamanio)
    let totalFinal = parseInt(totalArray) + parseInt(valorTamanio)
    inputTotal.value = parseInt(totalFinal)
    
    
 
 
})

coffeMedium.addEventListener('click',()=>{
    console.log(a)
    console.log(coffeMedium.value)
    coffeMediumImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeLargeImg.style.fill='grey'
    inputCafe.value= 'Cafe Mediano'
    
    let total = 0 
    tamanioPrecio.value = parseInt(total) 
    let nuevo = total + 200
    valorTamanio[0]=nuevo
    console.log(`El valor de cantidad'${totalArray}'`)
    console.log(`El valor de tamaño'${valorTamanio}'`)
    tamanioPrecio.value = parseInt(valorTamanio)
    let totalFinal = parseInt(totalArray) + parseInt(valorTamanio)
    inputTotal.value = parseInt(totalFinal)
 
})

coffeLarge.addEventListener('click',()=>{
    console.log(coffeLarge.value)
    coffeLargeImg.style.fill='black'
    coffeSmallImg.style.fill='grey'
    coffeMediumImg.style.fill='grey'
    inputCafe.value= 'Cafe Grande'
    let total = 0 
    tamanioPrecio.value = parseInt(total) 
    let nuevo = total + 300
    valorTamanio[0]=nuevo
    console.log(`El valor de cantidad'${totalArray}'`)
    console.log(`El valor de tamaño'${valorTamanio}'`)
    tamanioPrecio.value = parseInt(valorTamanio)
    let totalFinal = parseInt(totalArray) + parseInt(valorTamanio)
    inputTotal.value = parseInt(totalFinal)
   
})

/*tamaño */


/*azucar*/
sinAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Sin Azucar'
    sinAzucarButton.style.backgroundColor=' rgb(250, 191, 113)'
    unoAzucarButton.style.backgroundColor=' antiquewhite'
    dosAzucarButton.style.backgroundColor=' antiquewhite'
    tresAzucarButton.style.backgroundColor=' antiquewhite'

 //1
    
})

unoAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Uno de Azucar'
    sinAzucarButton.style.backgroundColor=' antiquewhite'
    unoAzucarButton.style.backgroundColor=' rgb(250, 191, 113)'
    dosAzucarButton.style.backgroundColor=' antiquewhite'
    tresAzucarButton.style.backgroundColor=' antiquewhite'

    //2
})

dosAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Dos de Azucar'
    sinAzucarButton.style.backgroundColor=' antiquewhite'
    unoAzucarButton.style.backgroundColor=' antiquewhite'
    dosAzucarButton.style.backgroundColor=' rgb(250, 191, 113)'
    tresAzucarButton.style.backgroundColor=' antiquewhite'
    //3
})


tresAzucarButton.addEventListener('click',()=>{
    inputAzucar.value= 'Tres de Azucar'
    sinAzucarButton.style.backgroundColor=' antiquewhite'
    unoAzucarButton.style.backgroundColor=' antiquewhite'
    dosAzucarButton.style.backgroundColor=' antiquewhite'
    tresAzucarButton.style.backgroundColor=' rgb(250, 191, 113)'
    //4
})
/*azucar */


/*adicional*/
conCanelaButton.addEventListener('click',()=>{
    console.log(coffeSmall.value)
    inputAdicional.value= 'Con Canella'
    conCanelaButton.style.backgroundColor=' rgb(250, 191, 113)'
    conCremaButton.style.backgroundColor=' antiquewhite'
})

conCremaButton.addEventListener('click',()=>{
    console.log(coffeSmall.value)
    inputAdicional.value= 'Con Crema'
    conCanelaButton.style.backgroundColor=' antiquewhite'
    conCremaButton.style.backgroundColor=' rgb(250, 191, 113)'
})


/*adicional*/

/*total 

total */

let suma = 0
const funcion=()=>{
    for (let i = 0;i< totalArray.length;i++){
        suma += totalArray[i]
        cero  =  inputTotal.value = 0
        final =  inputTotal.value = parseInt(suma)
    }   
    //console.log(`el resultado final es: '${final}'`)
    console.log(totalArray)
}

funcion()



const funcion2=()=>{
     
    //console.log(`el resultado final es: '${final}'`)
    console.log(totalArray)
}

funcion2()