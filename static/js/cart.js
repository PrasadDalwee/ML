var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0 ; i < updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click', function()
    {
        var productId= this.dataset.product
        var action = this.dataset.action
        console.log('productId : ',productId,'action:',action)
        console.log('user :', user)
        if(user == 'AnonymousUser')
        {
            console.log('not logged in')
        }
        else
        {
            updateUserOrder(productId, action)
        }
    } )
}

function updateUserOrder(productId, action)
{
    console.log('ha bhai')
    var url1 = '/update_item/'
    $.ajax({
        url : url1,
        action : action,
        method : 'POST',
        id : productId,
        data : {'id' : productId , 'action' : action},
        success: function(data){
            cartCount = document.getElementsByClassName
            ('cart-quantity');
            cartTotal = document.getElementsByClassName('cart-total');
            var id = productId
            itemPrice = document.getElementById('price-'+id)
            itemCount = document.getElementById('quantity-'+id)
            console.log('price-'+id, itemCount);
            var i;
            for(i = 0 ; i < cartCount.length ;i++)
            {
                cartCount[i].innerHTML = data.cart_quantity
            }
            for(i = 0 ; i < cartTotal.length ;i++)
            {
                cartTotal[i].innerHTML = data.cart_total
            }
            itemCount.innerHTML = data.item_quantity;
            itemPrice.innerHTML = data.item_total;
            if(data.item_quantity < 1)
            {
                row = document.getElementById("row-"+id)
                row.style.visibility = "hidden";
            }

        }
    })
    
}