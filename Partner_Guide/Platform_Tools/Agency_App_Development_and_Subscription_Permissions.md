# Agency App Development and Subscription Permissions

# 1. Overview
This feature guide explains how TikTok Shop grants API access to onboarded Agencies and how an Agency can use its TikTok Shop Agency identity to build custom applications and subscribe apps for the sellers it works with. With this capability, a seller no longer needs to have their main account complete every step manually.
After reading this guide, an Agency will be able to:

* Confirm that its onboarded account has the correct Agency identity and permission scope.
* Create a Custom App under the TikTok Shop Agency App Category and call TikTok Shop Open APIs.
* Use TSP Access to enter an authorized seller's Seller Center and confirm the App Subscription URL for that seller.
* Effective only in the **US local market**, other markets require separate ISV category applications.

# 2. Background
This capability makes it faster and simpler for Agencies to build and roll out API-based tooling for the sellers they support. It streamlines two areas of the previous experience:

* **Simpler developer access.** Onboarded Agencies now receive the App Developer (ISV) identity automatically, so they can create a Custom App that carries the required API scopes right away. Previously, an Agency needed a separate ISV App Category approval before it could call TikTok Shop APIs.
* **Subscribe on the seller's behalf.** With TSP Access, an Agency can now complete an app's subscription confirmation directly for an authorized seller. Previously, each install and subscription confirmation was completed from the seller's main account, which added steps when onboarding sellers, preparing LIVE launches, and getting ready for campaigns at scale.

Together, these updates give onboarded Agencies a more direct path to app development: onboarded Agencies are automatically granted the App Developer (ISV) identity and assigned to the dedicated TikTok Shop Agency App Category, with no separate ISV application required. Combined with TSP Access, an Agency can then complete subscription confirmations for authorized sellers directly.
# 3. Prerequisites

* Your Agency onboarding application has been approved.
* You can sign in to Partner Center with the account used for onboarding.
* At least one seller has authorized your TSP account through the standard TSP Access authorization flow (required for the subscribe-on-behalf steps in Section 6).

The App Developer (ISV) identity can take up to one working day to appear after onboarding approval. If it does not appear within that window, see the FAQ in Section 8.

# 4. How the feature works
## 4.1 App Developer (ISV) identity
Once an Agency's onboarding application is approved, the account owner will see a new App Developer (ISV) entry in the top-left identity switcher. This identity is the entry point to the TikTok Shop Developer console and unlocks the ability to create and manage Custom Apps.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/552823c3264049fda4647496a4c443c6~tplv-k9wyc2ijk0-image.image)
## 4.2 TikTok Shop Agency App Category
Behind the scenes, the platform assigns approved Agencies to a dedicated App Category named TikTok Shop Agency. This category defines the eligible API scopes an Agency's apps can request and governs the review flow for those apps. Agencies do not need to submit a separate ISV category application.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c6601c3b2060462188d7459d6116523f~tplv-k9wyc2ijk0-image.image)
## 4.3 Building a Custom App
Within the TikTok Shop Agency App Category, an Agency can create a Custom App that calls TikTok Shop Open APIs. The Custom App can then be distributed to and installed by the sellers the Agency works with, under the standard app-subscription flow.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/5f104b535ef945c48f44a76ad7bc3dd0~tplv-k9wyc2ijk0-image.image)
## 4.4 TSP Access and the App Subscription URL
With seller authorization already granted through the standard TSP Access flow, an Agency can enter the seller's Seller Center and open the App Subscription URL to complete the subscription confirmation for that seller. The seller's main account no longer needs to open the subscription screen for each app.
The specific permission point that governs this capability is shown below.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/6453cc542c7c475eabe24a32b91d4453~tplv-k9wyc2ijk0-image.image)
# 5. Permission point summary
| Capability | Identity required | How it is granted | Where it applies |
| --- | --- | --- | --- |
| Access the TikTok Shop Developer console | App Developer (ISV) | Auto-granted upon successful Agency onboarding | Top-left identity switcher |
| Create a Custom App calling TikTok Shop Open APIs | App Developer (ISV) with TikTok Shop Agency App Category | App Category set to TikTok Shop Agency | Developer console, Create App |
| Enter a seller's Seller Center on their behalf | TSP with an authorized seller | TSP Access | Partner Center, Seller list |
| Open the App Subscription URL and confirm a subscription for a seller | TSP with an authorized seller | TSP Access, App Subscription permission point (see Figure 4) | Seller Center, App Subscription URL |
# 6. Step-by-step guide
## 6.1 Verify your Agency identity

* Sign in to Partner Center with the account used for Agency onboarding.
* Open the top-left identity switcher and confirm that App Developer (ISV) is listed.
* If the identity is missing, allow up to one working day after onboarding approval, then verify the onboarding status of your Agency application before proceeding.

## 6.2 Create a Custom App

* Switch to the App Developer (ISV) identity.
* Enter the TikTok Shop Developer console and choose Create App.
* Select TikTok Shop Agency as the App Category.
* Complete the app metadata, request the required API scopes, and submit for review.

## 6.3 Onboard sellers and distribute the app

* Ensure the seller has authorized your TSP account through the standard TSP Access authorization flow.
* Share the app's install or subscription link with the seller, or use TSP Access to enter Seller Center directly.

## 6.4 Subscribe on behalf of the seller

* From Partner Center, locate the authorized seller and use TSP Access to enter their Seller Center.
* Open the App Subscription URL provided by your Custom App.
* Confirm the subscription. The seller's main account is no longer required to complete this step.

# 7. Compliance notes

* All API calls must respect the API scopes granted at app-review time. Requesting scopes beyond the TikTok Shop Agency App Category may result in review rejection.
* TSP Access is only valid while the seller's authorization is active. If the seller revokes authorization, TSP Access and subscribe-on-behalf actions are disabled immediately.
* Agencies remain responsible for the actions taken under TSP Access, including subscription confirmations. Full audit logs are retained by the platform for compliance review.
* Do not share App Developer (ISV) account credentials externally. Custom Apps must be built and maintained under the onboarded Agency entity.

# 8. FAQ
## Q1. I completed Agency onboarding but do not see the App Developer (ISV) identity.
Please allow up to one working day after onboarding approval. If the identity still does not appear, contact your TikTok Shop account manager with your Partner ID and approval timestamp.
## Q2. Do I still need to apply for an ISV App Category separately?
No. Onboarded Agencies are automatically placed under the TikTok Shop Agency App Category. A separate ISV application is not required.
## Q3. Do I still need the seller's main account to select the subscription button?
No. Once TSP Access authorization is in place, you can open the App Subscription URL inside the seller's Seller Center and complete the subscription confirmation for the seller. The seller's main account is not required for each subscription.
## Q4. What happens if the seller revokes TSP Access?
All TSP Access actions, including opening Seller Center and confirming subscriptions for the seller, are disabled immediately. Existing subscriptions remain effective unless the seller cancels them from their own Seller Center.
