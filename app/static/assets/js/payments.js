// Get Stripe publishable key
fetch("/config")
.then(result => result.json())
.then(data => {
    // Initialize Stripe.js with the public key
    const stripe = Stripe(data.publicKey);

    // Event handler for the submit button
    document.querySelector("#submitBtn").addEventListener("click", () => {

        var productSlug = document.getElementById('product_slug').innerText;
        console.log('Product Slug:', productSlug); // Debugging

        // Get Checkout Session ID
        fetch("/create-checkout-session/" + productSlug)
        .then(result => result.json())
        .then(data => {
            console.log('Checkout Session Data:', data); // Debugging
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then(res => {
            console.log('Stripe Checkout Response:', res); // Debugging
        })
        .catch(error => {
            console.error('Error during Stripe Checkout:', error);
            // Handle or display error
        });
    });
})
.catch(error => {
    console.error('Error fetching Stripe config:', error);
    // Handle or display error
});

