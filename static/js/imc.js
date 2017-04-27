/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


function constructor()
{
    Imc();
}

function Imc()
 {
                 var total=parseFloat($('#id_precio_total').val());
                if(isNaN(total))
                 {
                     total=0;
                 }
                var total1=parseInt($('#id_precio_total1').val());
                
                if(isNaN(total1))
                 {
                     total1=0;
                 }
                var total2=parseInt($('#id_precio_total2').val());
                
                if(isNaN(total2))
                 {
                     total2=0;
                 }
                var total3=parseInt($('#id_precio_total3').val());
                
                if(isNaN(total3))
                 {
                     total3=0;
                 }
                 var total4=parseInt($('#id_precio_total4').val());
                
                if(isNaN(total4))
                 {
                     total4=0;
                 }
                 var total5=parseInt($('#id_precio_total5').val());
                
                if(isNaN(total5))
                 {
                     total5=0;
                 }
                 var total6=parseInt($('#id_precio_total6').val());
                
                if(isNaN(total6))
                 {
                     total6=0;
                 }
                 var total7=parseInt($('#id_precio_total7').val());
                
                if(isNaN(total7))
                 {
                     total7=0;
                 }
                 var total8=parseInt($('#id_precio_total8').val());
                
                if(isNaN(total8))
                 {
                     total8=0;
                 }
                 var total9=parseInt($('#id_precio_total9').val());
                
                if(isNaN(total9))
                 {
                     total9=0;
                 }
                                 
                 $('#id_total').val(total+total1 +total2 + total3 + total4 + total5 + total6 +  total7 + total8 + total9 );               
            
    }

 
 