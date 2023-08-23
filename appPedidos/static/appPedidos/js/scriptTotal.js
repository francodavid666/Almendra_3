
/*Input total */
const inputTotal = document.getElementById('inputTotal')

/* valor del producto */
const valorProducto = document.getElementById('valorProducto')

inputTotal.value =0

let a = valorProducto.textContent
console.log(a)



buttonAdd.addEventListener("click",()=>{
    if(valorInput.value == 3){
      
    }else{
        valorInput.value= parseInt(valorInput.value) +1;
        console.log(valorInput.value)
       
        inputTotal.value = parseInt(inputTotal.value) + parseInt(a)
        
      
    }
  
    
})

buttonSubt.addEventListener("click",()=>{
    if(valorInput.value!=0){
        valorInput.value= parseInt(valorInput.value) -1;
        console.log(valorInput.value)
        inputTotal.value = parseInt(inputTotal.value) - parseInt(a)
    }
    else{
        
    }


})


/*totalInput */
