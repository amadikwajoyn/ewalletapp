## Building A Digital Wallet System (eWallet)

### myEwalletApp API
This is an myEwalletApp API that can be used or injected into any application that needs an ewallet feature for currency transaction. I also have an email otp verification feature.


### Required Endpoints

1. register: User should provide the following data: 'username, email, password' . Afterwards, the 6   numeric generated digit will be sent to the provided email address.
2. Email_verify: User should provide the following data: 'email, OTP' ; to verify the account.
3. Login: User should provide the following data to login: 'email, password'
5. Logout: User should provide the following data to logout: 'email, password'
6. curreny: Admin should provide the cur_category
7. fund: User should provide the 'user_id, currency_types, wallet_address, amount'
8. update_users: user should provide 'mobile and fullname'
9. user_setup: user should be able to provide 'user_id, currency_types, currency_types'
10. user_type: Admin should provide 'catergory'
11. withdraw_fund: user should provide user_id, currency_types, wallet_address, amount'
12. promote_demote: user should provide user_id, pro_demo_action'


### Features

-   Swagger API was used to test and document the API various endpoints
-   Users are able to get OTP code sent to their email address after registeration.
-   Users are able to verify their email using the OTP sent to them.
-   Registered users are able to login and logout.
-   After successful login, a token will be generated for the user.
-   Users are able to create their wallet and get a wallet address
-   Users are able to choose their categories
-   Users are able to fund and withdraw currency from their wallet
-   Admin is able to promote and/or demote user.


# Happy Hacking ...# myewallet
# ewalletapp
