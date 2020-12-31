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
            clientReferenceId: "123",
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