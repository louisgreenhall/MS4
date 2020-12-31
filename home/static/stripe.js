var stripe = Stripe('pk_test_51I4TYWGBayL5RWdKaHl2jck7cduUSoymkDiSD7VbFFYJYuKDHYANAwMud0YaQgmG3DvKEjZPgEUvLQc5SaTs0rpj00o0ZQuVK1');

$('#checkout_deposit').click(() => {


    stripe
        .redirectToCheckout({
            lineItems: [
                // Replace with the ID of your price
                {
                    price: 'price_1I4VhSGBayL5RWdKRA21yn6d',
                    quantity: 1
                },
            ],
            clientReferenceId: location.href,
            mode: 'payment',
            successUrl: 'http://localhost:8000/checkout/success?session_id={CHECKOUT_SESSION_ID}',
            cancelUrl: location.href,
        })
        .then(function (result) {
            // If `redirectToCheckout` fails due to a browser or network
            // error, display the localized error message to your customer
            // using `result.error.message`.
        })
});


const mappings = {
    'hand_drawn': 'price_1I4Z1JGBayL5RWdKLChX3xvK',
    'digital': 'price_1I4Z84GBayL5RWdKWerm12mR',
    'canvas': 'price_1I4Z2gGBayL5RWdKi5Ol8jZD',
    'framed': 'price_1I4Z37GBayL5RWdK2dpcThLu',
    'included': 'price_1I4Z3aGBayL5RWdK2Ci6cs1Y',
    'sketches': 'price_1I4Z3tGBayL5RWdKTNivREst'
}

$('#checkout_final').click(() => {
    
    let lineItems = [];
    $('.name').each((idx, item) => {

        lineItems.push({
            price: mappings[$(item).html()],
            quantity: 1
        });
    });
    console.log(lineItems)
    stripe
        .redirectToCheckout({
            lineItems: lineItems,
            clientReferenceId: location.href,
            mode: 'payment',
            successUrl: 'http://localhost:8000/checkout/success?session_id={CHECKOUT_SESSION_ID}',
            cancelUrl: location.href,
        })
        .then(function (result) {
            // If `redirectToCheckout` fails due to a browser or network
            // error, display the localized error message to your customer
            // using `result.error.message`.
        })
});