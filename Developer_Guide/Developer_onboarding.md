# Developer onboarding

Onboarding as a TikTok Shop developer has **three** main steps:

1. **Create an account** on the TikTok Shop Partner Center.
2. **Register as a developer** (seller developer, or app developer / ISV).
3. **Initiate the compliance and legal review** — required for US and UK partners (and case-by-case for others). This step can take **three or more weeks**, so start planning for it early.

> ⏱️ **Plan for the full timeline.** Steps 1–2 are quick, but the compliance & legal review in step 3 is the long pole. If you're a US or UK partner, factor in 3+ weeks before you can fully launch.

## Step 1: Create an account on Partner Center
If you don't already have one, create an account using the TikTok Shop Partner console:

* **U**S region accounts → [partner.us.tiktokshop.com/account/sign-up](https://partner.us.tiktokshop.com/account/sign-up)
* **N**on-US region accounts → [partner.tiktokshop.com/account/sign-up](https://partner.tiktokshop.com/account/sign-up)

> **Which domain do I use?** Use `partner.us.tiktokshop.com` for US region accounts and `partner.tiktokshop.com` for Global/ROW accounts. US cross-border seller developers use the Global entry. Later, when you make API calls, you'll also encounter `auth.tiktok-shops.com` (token endpoints) and the regional authorization domains (`services.us.tiktokshop.com` / `services.tiktokshop.com`). Each market/purpose has its own domain — see the authorization guides for the full mapping.

The process is the same for both. At the **Log In** dialog, select **Sign Up**, then provide your email address and (optionally) your phone number. Keep your Partner Center email current — it's essential for receiving critical platform updates.
**Why am I being redirected to the US site?**
Using a US VPN or proxy can cause Partner Center to redirect you to the US site based on your public IP. For Global/ROW access, check your IP location, disconnect the US VPN or use a non-US exit, then reopen [Global Partner Center](https://partner.tiktokshop.com/).
Your account region can also cause a redirect after login. If switching networks does not resolve it, sign out and retry in a private window, then confirm that the site matches your account region.
> ⚠️ Use the right email for your developer type. If you want to register as an app developer or system integrator (ISV), do not use the email associated with your TikTok Shop seller account. If you register with a Shop account email, the system will identify you as a seller and you can only register as a seller developer.

**Note:** The TikTok Shop Partner Platform and Open Platform merged into the TikTok Shop Partner Center in late 2022. If you have an existing Partner Platform or Open Platform account, you can log in with those credentials on Partner Center.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b28cc21e222f476c95281075a679196e~tplv-k9wyc2ijk0-image.image)
## Step 2: Register as a developer
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/8e669291d30f4b67bd48cadb951ed878~tplv-k9wyc2ijk0-image.image)
## Before you begin: determine your developer type
When you register, you'll select one of two developer types:

1. **TikTok Shop seller developer** — builds **custom** apps that access **their own** seller data only.
2. **App developer or system integrator (ISV)** — builds **public** apps and can request authorization to access **other sellers'** data on TikTok Shop.

> ✅ **Seller developer prerequisites (read before you start):**

> * You must have an **activated TikTok Shop account and bound an Account Manager before** registering as a developer.
> * The email you use for verification **should be the same** email used to register the TikTok Shop.

> These two constraints are the most common cause of failed seller-developer registrations.

## Registering as an app developer or system integrator (ISV)

1. **Start your partner registration application.** On the business guide dialog, select **For app developers (ISV)**, then **Start Business**.

> If your account needs to be allowlisted for the wrong email (**Using the shop account email**), submit a ticket or contact your Account Manager (AM) to request allowlisting before continuing the registration process. 

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/b13be7a323f042d693ae5b22cc619072~tplv-k9wyc2ijk0-image.image" width="1280px" /></div>


2. **Begin your partner application** by clicking **Start Business**.

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/906a33e285db45fd942596b714ac5e64~tplv-k9wyc2ijk0-image.image" width="1052px" /></div>


3. **Specify your registration region, target market, and business category:**

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/a0b1d2a2200c40f7b16eace530df6034~tplv-k9wyc2ijk0-image.image" width="3812px" /></div>


   * **Registration region:** must be consistent with your company's business certification.
   * **Target market:** cross-border partners (registration region China and/or Hong Kong, China) may select UK, MY, VN, TH, PH, or SG; local partners (entities in the local market) should choose only their local market.
   * **Business category:** select your business category. 📌 Available categories may vary by registration region and target market.
4. **Specify your company name and contact information,** and provide additional business details so the team can support you.

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/c4f7dc5ccb9d453595656649704cdcc2~tplv-k9wyc2ijk0-image.image" width="3816px" /></div>


5. **Upload your company's business certificate and registration information.**

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/53c321e8ce844441bbd2d0c67c5e9654~tplv-k9wyc2ijk0-image.image" width="3810px" /></div>


   * If you don't have these ready, select **Save for later**; you can then go *Back to profile* or *Create app or service*. (If you create an app now, you can't publish it until certification is complete.)

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/4f9839cc656a4d37bdf20715c2eb2e3e~tplv-k9wyc2ijk0-image.image" width="3806px" /></div>


   * Otherwise, select **Submit** to begin certification review.

<div style="text-align: center"><img src="https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/fd21258fe5b8436abd226db7c4d21320~tplv-k9wyc2ijk0-image.image" width="3812px" /></div>

Check your application status under **My Account > My category & market**. Once approved, the **under review** message disappears.
![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/1fcbb9ff22994e46ab601438ec9767d4~tplv-k9wyc2ijk0-image.image)
## Add another market after onboarding
If you already have an ISV app and want to expand it, you can start from that app's **+ Add market (Seller type)** dialog. See **Add markets to an existing app** in [Create your App](https://partner.tiktokshop.com/docv2/page/create-your-app) for the complete flow.
You can also start from your profile:

1. Open your profile and select the option to add a category or market. 
2. Select the target market and business category, then click **Next**. 
3. Review the **Partner info** form and complete the required information. If you already have an app in that category, click **Submit** to save a draft. 
4. On the success page, choose how you want to continue: 
   * **Add to an existing App** opens **App & Service**, filtered to the relevant category. Choose an app and click **Manage**, then use **+ Add market (Seller type)** to select an available market, complete the seller settings and **Save**. If qualification review is required before the market becomes available, complete that review first.
   * **Create a new App** opens the app creation flow with the selected category carried over. Choose **Public** or **Custom**, review the app details and complete creation.


![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/925f6c7c17fc4a0db5572c2b0aa9a415~tplv-k9wyc2ijk0-image.image)

If you do not have an app in the selected category, continue through the app creation flow shown in Partner Center.
> **Check the final step.** The success page confirms that your draft information has been saved. It does not mean qualification review has started, that the market has been added to an app, or that the app is live there.

### Find the app you want to expand
The **Category** filter groups matching Public and Custom categories under one option. Use the separate **Type** filter if you want to see only Public or only Custom apps.
When you arrive from **Add to an existing App**, Partner Center displays a prompt to select an app. Closing this prompt leaves the category filter in place.
## Registering as a seller developer
> Detailed guide refer to: https://partner.tiktokshop.com/docv2/page/seller-developer-onboarding-onepager


* When applying for a target market for a developer account, select the category **Seller inhouse developer / TikTok Shop Seller** and **link the activated TikTok Shop account** in the next step.

![Image](https://p16-arcosite-sg.ibyteimg.com/tos-alisg-i-k9wyc2ijk0-sg/f9513f71b0d84bcab0ad458aa7d7f8f0~tplv-k9wyc2ijk0-image.image)

📌 **Note**: Please ensure the seller account information you entered is authentic.

## Step 3: Initiate the compliance and legal review
Once you've registered as a developer partner, initiate the compliance and legal review. It can take **three or more weeks**. Reviews are required case-by-case for some partners, but are **always required for US and UK partners**.
Contact the Partner Development & Management team for your market to request a due diligence questionnaire:

* US: [partner.us@tiktokshop.com](mailto:partner.us@tiktokshop.com)
* UK: [partner.uk@tiktokshop.com](mailto:partner.uk@tiktokshop.com)
* Other: [partner@tiktokshop.com](mailto:partner@tiktokshop.com)

**When to start:** initiate this review as soon as you've registered, so the 3+ week timeline runs in parallel with your development. Prepare your due diligence questionnaire and supporting business documents in advance. See Compliance and Legal Review for details.
## Next steps
Now that you have a partner developer account, you're ready to [make your first TikTok Shop API call](https://partner.tiktokshop.com/docv2/page/make-your-first-api-call-overview).

