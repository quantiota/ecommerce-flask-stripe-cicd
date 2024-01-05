import stripe

# Set your Stripe API key
stripe.api_key = "sk_test_51IPFZjKeK0TSVc1EiFn8JIEesJhxMbvfvbLNkYVeWYv6ROJI1pNEKIE3kbaumJDdKr4Iubphs8VgS2tAsgA6JJrS00VIw5U36i"

# Specify the tax code for which you want to retrieve tax rates
tax_code = "your_tax_code_here"

try:
    # Retrieve tax rates from Stripe based on the tax code
    tax_rates = stripe.TaxRate.list(limit=100, active=True, tax_code=tax_code)

    # Loop through the tax rates and access their information
    for tax_rate in tax_rates:
        print(f"Tax Rate ID: {tax_rate.id}, Percentage: {tax_rate.percentage}%")
except stripe.error.StripeError as e:
    # Handle any Stripe API errors here
    print(f"Stripe API Error: {e}")
