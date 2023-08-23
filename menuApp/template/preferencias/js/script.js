const valorInput = document.getElementById('inputCantidad');
const buttonAdd = document.getElementById('buttonAdd')
const buttonSubt = document.getElementById('buttonSubt')
const valor = valorInput.value;


buttonAdd.addEventListener("click",()=>{
    if(valorInput.value == 3){
      
    }else{
        valorInput.value= parseInt(valorInput.value) +1;
        console.log(valorInput.value)
    }
  
    
})

buttonSubt.addEventListener("click",()=>{
    if(valorInput.value!=0){
        valorInput.value= parseInt(valorInput.value) -1;
        console.log(valorInput.value)
    }
    else{
        
    }


})






