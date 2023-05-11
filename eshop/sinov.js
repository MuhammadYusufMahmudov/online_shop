    $('.add-cart').click(function () {
        product_id = $(this).data('id')
        data = {'product_id': product_id}
        url_add_cart = '/order/add-cart/'
        post_data(url_add_cart, data,update_badge)

    })

    function update_badge(response) {
        $('#badge').text(response.items_count)
        if (response.event == 'added'){
            $(`#pbtn${response.pid}`).removeClass('btn-primary')
            $(`#pbtn${response.pid}`).text('Added to cart')
            $(`#pbtn${response.pid}`).addClass('btn-success')
        }else if(response.event == 'deleted'){
            $(`#pbtn${response.pid}`).removeClass('btn-success')
            $(`#pbtn${response.pid}`).text('Add to cart')
            $(`#pbtn${response.pid}`).addClass('btn-primary')
        }
    }

    function post_data(url, data, callback) {
        $.ajax({
            type: "POST",
            url: url,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify(data),
            success: callback
        })
    }

    $('.change-quantity').click(function () {
        item_id = $(this).data('item')
        action = $(this).data('action')
        let url_change_quantity = '/order/change-quantity/'
        let data = {
            'item': item_id,
            'action': action
        }
        console.log(item_id, action)
        post_data(url_change_quantity, data, item_quantity_change)
    })

    $('.input-quantity').keyup(function (){
        value = $(this).val()
        item_id = $(this).data('item')
        action = 'onkeyup'
        console.log(value, item_id)
        let url_change_quantity = '/order/change-quantity/'
        let data = {
            'item': item_id,
            'action': action,
            'value': value
        }
        console.log(item_id, action)
        post_data(url_change_quantity, data, item_quantity_change)

    })

    function item_quantity_change(response) {
        if (response.error == false) {
            $(`#${response.item}`).val(response.item_quantity)
            $(`#price${response.item}`).text(`$${response.total_price}.0`)
            $('#total-price').text(`$${response.total}.0`)
        }
    }

    $('.remove-item').click(function () {
        item_id = $(this).data('id')
        console.log(item_id)
        $.ajax({
            type: "GET",
            url: `/order/remove/${item.id}/`,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            success: function (response) {
                console.log(response)
                if (response.success)
                    $(`#item_tr_${response.id}`).remove()
                $('#badge').text(response.items_count)
                $('#total-price').text(`$${response.total}.0`)
            }
        })
    })

