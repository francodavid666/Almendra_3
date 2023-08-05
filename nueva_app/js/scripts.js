const buttonIngresar = document.getElementById('button-intro')
const iconoShop = document.getElementById('icono-shop')
const iconoMachine = document.getElementById('icono-machine')

const mainContainer=document.getElementById('main-container')

gsap.to('.titleGsap',{
    duratiom:1,
    
    delay:'0.2s',
    fontSize: '30px'
})




let url = 'https://almendra-productos.up.railway.app/'


/*function eliminarContainer(){
    mainContainer.style.display='none'
}*/

buttonIngresar.addEventListener('click',()=>{
    gsap.to('.iconoShopGsap',{
        scale: 1.3,ease:'power2.out', });
    gsap.to('.iconoShopGsap',{scale:0, ease:'power2.out',delay:0.5,display:'none'
    })

    gsap.to('.titleGsap',{
        scale: 1.1,ease:'power2.out',  });
    gsap.to('.titleGsap',{scale:0,fontSize:0, ease:'power2.out',delay:0.5,display:'none'
    })
    gsap.to('.button-intro',{
        delay:.5,
        transition:.5,
        ease:'power2.out',
        backgroundColor:'white',
        border:'none',
        boxShadow:'none',
        marginBottom:300, 
     }),
     gsap.to('.button-intro',{
        delay:1.5,
        scale:200,
        transition:1,
     })
 
     //setTimeout(eliminarContainer,3000)
    
    //window.open(url)

})





/*buttonIngresar.addEventListener("click",()=>{
   for (let property in stylesIconoShop) {
    iconoShop.style[property]=stylesIconoShop[property]
}
    for (let property in stylesIconoMachine) {
        iconoMachine.style[property]=stylesIconoMachine[property]
   }
});*/


