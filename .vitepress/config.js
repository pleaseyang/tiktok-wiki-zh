import { defineConfig } from 'vitepress'

export default defineConfig({
  ignoreDeadLinks: true,
  base: process.env.BASE_PATH || '/tiktok-docs/',
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'TikTok Shop Partner Center',
      description: 'TikTok Shop Partner Center Documentation',
      themeConfig: {
        nav: [
          { text: 'Partner Guide', link: '/Partner_Guide/About_the_Partner_Center_Console' },
          { text: 'Developer Guide', link: '/Developer_Guide/TikTok_Shop_developer_guide' },
          { text: 'API Reference', link: '/API_Reference/Guide' },
          { text: 'Webhooks', link: '/Webhooks/Order/(1)_Order_status_change' }
        ],
        sidebar: [
          {
            text: 'Partner Guide',
            collapsed: false,
            items: [
              { text: 'About the Partner Center Console', link: '/Partner_Guide/About_the_Partner_Center_Console' },
              {
                text: 'Partner Type',
                collapsed: true,
                items: [
                  { text: 'Developer', link: '/Partner_Guide/Partner_type/Developer' },
                  { text: 'TikTok Shop Partner (TSP)', link: '/Partner_Guide/Partner_type/TikTok_Shop_Partner_(TSP)' },
                  { text: 'Creator Agency Partner (CAP)', link: '/Partner_Guide/Partner_type/Creator_Agency_Partner_(CAP)' },
                  { text: 'Non-US Affiliate Partner (TAP)', link: '/Partner_Guide/Partner_type/Non-US_TikTok_Shop_Affiliate_Partner_(TAP)' },
                  { text: 'US Affiliate Partner (TAP)', link: '/Partner_Guide/Partner_type/US_TikTok_Shop_Affiliate_Partner_(TAP)' },
                  { text: 'Multi-Channel Network (MCN)', link: '/Partner_Guide/Partner_type/Multi-Channel_Network_(MCN)' }
                ]
              },
              {
                text: 'Become a Partner',
                collapsed: true,
                items: [
                  { text: 'Register as a Service Partner', link: '/Partner_Guide/Become_a_partner/Register_as_a_service_partner' },
                  { text: '[US] Agency Partner Onboard Guide', link: '/Partner_Guide/Become_a_partner/[US]_Agency_Partner_Onboard_Guide' },
                  { text: 'Partner Service Categories', link: '/Partner_Guide/Become_a_partner/Partner_service_categories' },
                  { text: 'Partner Registration Requirement', link: '/Partner_Guide/Become_a_partner/Partner_registration_application_requirement' },
                  { text: 'Managing Main and Member Accounts', link: '/Partner_Guide/Become_a_partner/Managing_Main_and_Member_Accounts' }
                ]
              },
              {
                text: 'Console Guides for TSP',
                collapsed: true,
                items: [
                  { text: 'Create and Publish a Service', link: '/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Create_and_publish_a_service' },
                  { text: 'Listing Your Service', link: '/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Listing_your_service_on_the_App_&_Service_Store' },
                  { text: 'Seller Leads Pool', link: '/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Seller_Leads_Pool' },
                  { text: 'Steps to Get Service Authorization', link: '/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Steps_to_Get_Service_Authorization' },
                  { text: 'TSP Access Feature', link: '/Partner_Guide/Partner_Center_Console_Guides_for_TSP/TSP_Access_Feature' }
                ]
              },
              {
                text: 'Console Guides for CAP/MCN',
                collapsed: true,
                items: [
                  { text: 'Find Creators', link: '/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Creator_Management_-_Find_Creators' },
                  { text: 'Linked Creators', link: '/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Creator_Management_-_Linked_Creators' },
                  { text: 'Product Management', link: '/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Product_Management' }
                ]
              },
              {
                text: 'Finance',
                collapsed: true,
                items: [
                  { text: '[CAP/TAP] Finance Guide (US)', link: '/Partner_Guide/Finance/[CAP_TAP]_Finance_guide_(US_only)' },
                  { text: 'Finance (Non-US)', link: '/Partner_Guide/Finance/Finance(Non-us)' }
                ]
              }
            ]
          },
          {
            text: 'Developer Guide',
            collapsed: false,
            items: [
              { text: 'TikTok Shop Developer Guide', link: '/Developer_Guide/TikTok_Shop_developer_guide' },
              {
                text: 'Get Started',
                collapsed: true,
                items: [
                  { text: 'Get Started Overview', link: '/Developer_Guide/Get_started/Get_started_overview' },
                  { text: 'App Category Selection Guide', link: '/Developer_Guide/Get_started/App_Category_Selection_Guide' }
                ]
              },
              {
                text: 'API Concepts',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/Developer_Guide/TikTok_Shop_API_concepts/Overview' },
                  { text: 'Methods and Endpoints', link: '/Developer_Guide/TikTok_Shop_API_concepts/Methods_and_endpoints' },
                  { text: 'Sign Your API Request', link: '/Developer_Guide/TikTok_Shop_API_concepts/Sign_your_API_request' },
                  { text: 'Common Parameters', link: '/Developer_Guide/TikTok_Shop_API_concepts/Common_parameters' },
                  { text: 'Common Errors', link: '/Developer_Guide/TikTok_Shop_API_concepts/Common_errors' },
                  { text: 'Rate Limits', link: '/Developer_Guide/TikTok_Shop_API_concepts/Rate_limits' },
                  { text: 'API Versioning', link: '/Developer_Guide/TikTok_Shop_API_concepts/API_versioning' }
                ]
              },
              {
                text: 'Solution Guidance',
                collapsed: true,
                items: [
                  { text: 'Product API Solution Guide', link: '/Developer_Guide/Solution_Guidance/Product_API_Solution_Guide' },
                  { text: 'Orders and Fulfillment API Guide', link: '/Developer_Guide/Solution_Guidance/Orders_and_Fulfillment_API_Solution_Guide' },
                  { text: 'Affiliate API Solution Guide', link: '/Developer_Guide/Solution_Guidance/Affiliate_API_Solution_Guide' }
                ]
              },
              {
                text: 'API SDK',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/Developer_Guide/TikTok_Shop_API_SDK/Overview' },
                  { text: 'Download SDK', link: '/Developer_Guide/TikTok_Shop_API_SDK/Download_SDK' },
                  { text: 'Integrate Java SDK', link: '/Developer_Guide/TikTok_Shop_API_SDK/Integrate_Java_SDK' },
                  { text: 'Integrate Node.js SDK', link: '/Developer_Guide/TikTok_Shop_API_SDK/Integrate_Node.js_SDK' }
                ]
              },
              {
                text: 'Webhooks',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/Developer_Guide/TikTok_Shop_webhooks/Overview' },
                  { text: 'Configuration Guide', link: '/Developer_Guide/TikTok_Shop_webhooks/Configuration_guide' }
                ]
              }
            ]
          },
          {
            text: 'API Reference',
            collapsed: true,
            items: [
        {
          text: 'Tools',
          collapsed: true,
          items: [
          { text: 'Common Error Codes', link: '/API_Reference/Tools/Common_Error_Codes' },
          { text: 'Common Parameters', link: '/API_Reference/Tools/Common_Parameters' },
          { text: 'Get Access Token', link: '/API_Reference/Tools/Get_Access_Token' },
          { text: 'Partner Authorization Guide', link: '/API_Reference/Tools/Partner_Authorization_Guide' }
          ]
        },
        {
          text: 'Authorization',
          collapsed: true,
          items: [
          { text: 'Get Authorized Category Assets', link: '/API_Reference/Authorization/Get_Authorized_Category_Assets' },
          { text: 'Get Authorized Shops', link: '/API_Reference/Authorization/Get_Authorized_Shops' }
          ]
        },
        {
          text: 'Event',
          collapsed: true,
          items: [
          { text: 'Delete Webhook for an Event', link: '/API_Reference/Event/Delete_Webhook_for_an_Event' },
          { text: 'Get Shop Webhooks', link: '/API_Reference/Event/Get_Shop_Webhooks' },
          { text: 'Update Shop Webhook', link: '/API_Reference/Event/Update_Shop_Webhook' }
          ]
        },
        {
          text: 'Seller',
          collapsed: true,
          items: [
          { text: 'Seller API overview', link: '/API_Reference/Seller/Seller_API_overview' },
          { text: 'Get Active Shops', link: '/API_Reference/Seller/Get_Active_Shops' },
          { text: 'Get Global Product Permission', link: '/API_Reference/Seller/Get_Global_Product_Permission' },
          { text: 'Get Shop Group and Related Shops', link: '/API_Reference/Seller/Get_Shop_Group_and_Related_Shops' }
          ]
        },
        {
          text: 'Products',
          collapsed: true,
          items: [
          { text: 'Products API overview', link: '/API_Reference/Products/Products_API_overview' },
          { text: 'Activate Products', link: '/API_Reference/Products/Activate_Products' },
          { text: 'Check Listing Prerequisites', link: '/API_Reference/Products/Check_Listing_Prerequisites' },
          { text: 'Check Product Listing', link: '/API_Reference/Products/Check_Product_Listing' },
          { text: 'Common mistakes', link: '/API_Reference/Products/Common_mistakes' },
          { text: 'Create Category Upgrade Task', link: '/API_Reference/Products/Create_Category_Upgrade_Task' },
          { text: 'Create Custom Brands', link: '/API_Reference/Products/Create_Custom_Brands' },
          { text: 'Create GPA Upgrade Task', link: '/API_Reference/Products/Create_GPA_Upgrade_Task' },
          { text: 'Create Image Translation Tasks', link: '/API_Reference/Products/Create_Image_Translation_Tasks' },
          { text: 'Create Product', link: '/API_Reference/Products/Create_Product' },
          { text: 'Deactivate Products', link: '/API_Reference/Products/Deactivate_Products' },
          { text: 'Delete Products', link: '/API_Reference/Products/Delete_Products' },
          { text: 'Diagnose and Optimize Product', link: '/API_Reference/Products/Diagnose_and_Optimize_Product' },
          { text: 'Edit Product', link: '/API_Reference/Products/Edit_Product' },
          { text: 'Get Brands', link: '/API_Reference/Products/Get_Brands' },
          { text: 'Get Categories', link: '/API_Reference/Products/Get_Categories' },
          { text: 'Get Category Attributes', link: '/API_Reference/Products/Get_Category_Attributes' },
          { text: 'Get Category Rules', link: '/API_Reference/Products/Get_Category_Rules' },
          { text: 'Get Global Listing Rules', link: '/API_Reference/Products/Get_Global_Listing_Rules' },
          { text: 'Get Global Replicated Products', link: '/API_Reference/Products/Get_Global_Replicated_Products' },
          { text: 'Get Image Translation Tasks', link: '/API_Reference/Products/Get_Image_Translation_Tasks' },
          { text: 'Get Opportunity Detail', link: '/API_Reference/Products/Get_Opportunity_Detail' },
          { text: 'Get Product', link: '/API_Reference/Products/Get_Product' },
          { text: 'Get Product Diagnoses', link: '/API_Reference/Products/Get_Product_Diagnoses' },
          { text: 'Get Product Package Recommendations', link: '/API_Reference/Products/Get_Product_Package_Recommendations' },
          { text: 'Get Product SKPP Detail', link: '/API_Reference/Products/Get_Product_SKPP_Detail' },
          { text: 'Get Products SEO Words', link: '/API_Reference/Products/Get_Products_SEO_Words' },
          { text: 'Get Recommended Product Title And Description', link: '/API_Reference/Products/Get_Recommended_Product_Title_And_Description' },
          { text: 'Get Shop SKPP Summary', link: '/API_Reference/Products/Get_Shop_SKPP_Summary' },
          { text: 'Get Submission Records', link: '/API_Reference/Products/Get_Submission_Records' },
          { text: 'Inventory Search', link: '/API_Reference/Products/Inventory_Search' },
          { text: 'List Opportunities', link: '/API_Reference/Products/List_Opportunities' },
          { text: 'List Product SKPP Statuses', link: '/API_Reference/Products/List_Product_SKPP_Statuses' },
          { text: 'Listing quality diagnosis', link: '/API_Reference/Products/Listing_quality_diagnosis' },
          { text: 'Optimize Images', link: '/API_Reference/Products/Optimize_Images' },
          { text: 'Partial Edit Global Product', link: '/API_Reference/Products/Partial_Edit_Global_Product' },
          { text: 'Partial Edit Product', link: '/API_Reference/Products/Partial_Edit_Product' },
          { text: 'Product pricing', link: '/API_Reference/Products/Product_pricing' },
          { text: 'Recommend Category', link: '/API_Reference/Products/Recommend_Category' },
          { text: 'Recover Products', link: '/API_Reference/Products/Recover_Products' },
          { text: 'Replicate Product', link: '/API_Reference/Products/Replicate_Product' },
          { text: 'Search Products', link: '/API_Reference/Products/Search_Products' },
          { text: 'Search Products for Compliance Auditing', link: '/API_Reference/Products/Search_Products_for_Compliance_Auditing' },
          { text: 'Search Size Charts', link: '/API_Reference/Products/Search_Size_Charts' },
          { text: 'Submit Product via Opportunity', link: '/API_Reference/Products/Submit_Product_via_Opportunity' },
          { text: 'Submit Size Chart Appeal', link: '/API_Reference/Products/Submit_Size_Chart_Appeal' },
          { text: 'Suggest Brands', link: '/API_Reference/Products/Suggest_Brands' },
          { text: 'Update Inventory', link: '/API_Reference/Products/Update_Inventory' },
          { text: 'Update Price', link: '/API_Reference/Products/Update_Price' },
          { text: 'Update Stock Operation Settings', link: '/API_Reference/Products/Update_Stock_Operation_Settings' },
          { text: 'Upload Product File', link: '/API_Reference/Products/Upload_Product_File' },
          { text: 'Upload Product Image', link: '/API_Reference/Products/Upload_Product_Image' }
          ]
        },
        {
          text: 'Global Products',
          collapsed: true,
          items: [
          { text: 'Create Global Product', link: '/API_Reference/Products_Global_Products/Create_Global_Product' },
          { text: 'Delete Global Products', link: '/API_Reference/Products_Global_Products/Delete_Global_Products' },
          { text: 'Edit Global Product', link: '/API_Reference/Products_Global_Products/Edit_Global_Product' },
          { text: 'Get Global Attributes', link: '/API_Reference/Products_Global_Products/Get_Global_Attributes' },
          { text: 'Get Global Categories', link: '/API_Reference/Products_Global_Products/Get_Global_Categories' },
          { text: 'Get Global Category Rules', link: '/API_Reference/Products_Global_Products/Get_Global_Category_Rules' },
          { text: 'Get Global Product', link: '/API_Reference/Products_Global_Products/Get_Global_Product' },
          { text: 'Publish Global Product', link: '/API_Reference/Products_Global_Products/Publish_Global_Product' },
          { text: 'Recommend Global Categories', link: '/API_Reference/Products_Global_Products/Recommend_Global_Categories' },
          { text: 'Search Global Products', link: '/API_Reference/Products_Global_Products/Search_Global_Products' },
          { text: 'Update Global Inventory', link: '/API_Reference/Products_Global_Products/Update_Global_Inventory' }
          ]
        },
        {
          text: 'Compliance',
          collapsed: true,
          items: [
          { text: 'Create Manufacturer', link: '/API_Reference/Products_Compliance/Create_Manufacturer' },
          { text: 'Create Responsible Person', link: '/API_Reference/Products_Compliance/Create_Responsible_Person' },
          { text: 'Partial Edit Manufacturer', link: '/API_Reference/Products_Compliance/Partial_Edit_Manufacturer' },
          { text: 'Partial Edit Responsible Person', link: '/API_Reference/Products_Compliance/Partial_Edit_Responsible_Person' },
          { text: 'Search Manufacturers', link: '/API_Reference/Products_Compliance/Search_Manufacturers' },
          { text: 'Search Responsible Persons', link: '/API_Reference/Products_Compliance/Search_Responsible_Persons' }
          ]
        },
        {
          text: 'Promotion',
          collapsed: true,
          items: [
          { text: 'Promotion API overview', link: '/API_Reference/Promotion/Promotion_API_overview' },
          { text: 'Create Promotion Activity', link: '/API_Reference/Promotion/Create_Promotion_Activity' },
          { text: 'Deactivate Activity', link: '/API_Reference/Promotion/Deactivate_Activity' },
          { text: 'Get Activity', link: '/API_Reference/Promotion/Get_Activity' },
          { text: 'Get Coupon', link: '/API_Reference/Promotion/Get_Coupon' },
          { text: 'Remove Promotion Activity Products', link: '/API_Reference/Promotion/Remove_Promotion_Activity_Products' },
          { text: 'Republish Activity', link: '/API_Reference/Promotion/Republish_Activity' },
          { text: 'Search Coupon List', link: '/API_Reference/Promotion/Search_Coupon_List' },
          { text: 'Search Promotion Activities', link: '/API_Reference/Promotion/Search_Promotion_Activities' },
          { text: 'Shipping discount supported areas', link: '/API_Reference/Promotion/Shipping_discount_supported_areas' },
          { text: 'Update Promotion Activity', link: '/API_Reference/Promotion/Update_Promotion_Activity' },
          { text: 'Update Promotion Activity Products', link: '/API_Reference/Promotion/Update_Promotion_Activity_Products' }
          ]
        },
        {
          text: 'Orders',
          collapsed: true,
          items: [
          { text: 'Order API overview', link: '/API_Reference/Orders/Order_API_overview' },
          { text: 'Add External Order References', link: '/API_Reference/Orders/Add_External_Order_References' },
          { text: 'Get External Order References', link: '/API_Reference/Orders/Get_External_Order_References' },
          { text: 'Get Order Detail', link: '/API_Reference/Orders/Get_Order_Detail' },
          { text: 'Get Order List', link: '/API_Reference/Orders/Get_Order_List' },
          { text: 'Get Order Price Details', link: '/API_Reference/Orders/Get_Order_Price_Details' },
          { text: 'Search Orders by External Order Reference', link: '/API_Reference/Orders/Search_Orders_by_External_Order_Reference' },
          { text: 'Search POD Customization Details', link: '/API_Reference/Orders/Search_POD_Customization_Details' },
          { text: 'Update The Blind Box Opening Results', link: '/API_Reference/Orders/Update_The_Blind_Box_Opening_Results' }
          ]
        },
        {
          text: 'Fulfillment',
          collapsed: true,
          items: [
          { text: 'Fulfillment API overview', link: '/API_Reference/Fulfillment/Fulfillment_API_overview' },
          { text: 'Batch Ship Packages', link: '/API_Reference/Fulfillment/Batch_Ship_Packages' },
          { text: 'Check TikTok Shipping and Collection by TikTok Coverage', link: '/API_Reference/Fulfillment/Check_TikTok_Shipping_and_Collection_by_TikTok_Coverage' },
          { text: 'Combine Package', link: '/API_Reference/Fulfillment/Combine_Package' },
          { text: 'Confirm Order Split', link: '/API_Reference/Fulfillment/Confirm_Order_Split' },
          { text: 'Confirm Package Shipment', link: '/API_Reference/Fulfillment/Confirm_Package_Shipment' },
          { text: 'Create First Mile Bundle', link: '/API_Reference/Fulfillment/Create_First_Mile_Bundle' },
          { text: 'Create First Mile Bundle(V2)', link: '/API_Reference/Fulfillment/Create_First_Mile_Bundle(V2)' },
          { text: 'Create Packages', link: '/API_Reference/Fulfillment/Create_Packages' },
          { text: 'Get Eligible Shipping Services', link: '/API_Reference/Fulfillment/Get_Eligible_Shipping_Services' },
          { text: 'Get Order Customs Requirements', link: '/API_Reference/Fulfillment/Get_Order_Customs_Requirements' },
          { text: 'Get Order Split Attributes', link: '/API_Reference/Fulfillment/Get_Order_Split_Attributes' },
          { text: 'Get Order Tracking', link: '/API_Reference/Fulfillment/Get_Order_Tracking' },
          { text: 'Get Package Detail', link: '/API_Reference/Fulfillment/Get_Package_Detail' },
          { text: 'Get Package Handover Time Slots', link: '/API_Reference/Fulfillment/Get_Package_Handover_Time_Slots' },
          { text: 'Get Package Shipping Document', link: '/API_Reference/Fulfillment/Get_Package_Shipping_Document' },
          { text: 'Get POD Customization Details', link: '/API_Reference/Fulfillment/Get_POD_Customization_Details' },
          { text: 'Mark Package As Shipped', link: '/API_Reference/Fulfillment/Mark_Package_As_Shipped' },
          { text: 'Search Combinable Packages', link: '/API_Reference/Fulfillment/Search_Combinable_Packages' },
          { text: 'Search Package', link: '/API_Reference/Fulfillment/Search_Package' },
          { text: 'Ship Package', link: '/API_Reference/Fulfillment/Ship_Package' },
          { text: 'Submit Customs Clearance Information', link: '/API_Reference/Fulfillment/Submit_Customs_Clearance_Information' },
          { text: 'Submit Redemption Information', link: '/API_Reference/Fulfillment/Submit_Redemption_Information' },
          { text: 'Tracking status update', link: '/API_Reference/Fulfillment/Tracking_status_update' },
          { text: 'Uncombine Packages', link: '/API_Reference/Fulfillment/Uncombine_Packages' },
          { text: 'Update Order Shipping Info', link: '/API_Reference/Fulfillment/Update_Order_Shipping_Info' },
          { text: 'Update Package Delivery Status', link: '/API_Reference/Fulfillment/Update_Package_Delivery_Status' },
          { text: 'Update Package Shipping Info', link: '/API_Reference/Fulfillment/Update_Package_Shipping_Info' },
          { text: 'Upload Invoice', link: '/API_Reference/Fulfillment/Upload_Invoice' },
          { text: 'Upload Proof of Delivery File', link: '/API_Reference/Fulfillment/Upload_Proof_of_Delivery_File' },
          { text: 'Upload Proof of Delivery Image', link: '/API_Reference/Fulfillment/Upload_Proof_of_Delivery_Image' }
          ]
        },
        {
          text: 'Fulfilled by TikTok (FBT)',
          collapsed: true,
          items: [
          { text: 'FBT Inbound API Overview Guide', link: '/API_Reference/Fulfilled_by_TikTok_FBT/FBT_Inbound_API_Overview_Guide' },
          { text: 'Cancel FBT MCF Order', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Cancel_FBT_MCF_Order' },
          { text: 'Cancel Inbound Order', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Cancel_Inbound_Order' },
          { text: 'Confirm Inbound Method', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Confirm_Inbound_Method' },
          { text: 'Create FBT Goods', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Create_FBT_Goods' },
          { text: 'Create FBT MCF Order', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Create_FBT_MCF_Order' },
          { text: 'Create or Update Inbound Plan', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Create_or_Update_Inbound_Plan' },
          { text: 'Get FBT Inbound Order Details', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Inbound_Order_Details' },
          { text: 'Get FBT MCF Order Status', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_MCF_Order_Status' },
          { text: 'Get FBT Merchant MCF Status', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Merchant_MCF_Status' },
          { text: 'Get FBT Merchant Onboarded Regions', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Merchant_Onboarded_Regions' },
          { text: 'Get FBT Warehouse List', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Warehouse_List' },
          { text: 'Get Inbound Method Detail', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Get_Inbound_Method_Detail' },
          { text: 'List Available Inbound Methods', link: '/API_Reference/Fulfilled_by_TikTok_FBT/List_Available_Inbound_Methods' },
          { text: 'Print Inbound Order Labels', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Print_Inbound_Order_Labels' },
          { text: 'Query Goods Inventory For MCF', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Query_Goods_Inventory_For_MCF' },
          { text: 'Search FBT Inventory', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Search_FBT_Inventory' },
          { text: 'Search FBT Inventory Record', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Search_FBT_Inventory_Record' },
          { text: 'Search Goods Hazmat And Expiration Info', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Search_Goods_Hazmat_And_Expiration_Info' },
          { text: 'Search Goods Info', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Search_Goods_Info' },
          { text: 'Ship Inbound Order', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Ship_Inbound_Order' },
          { text: 'Update FBT Goods Info', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Update_FBT_Goods_Info' },
          { text: 'Update Goods-SKU Relations', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Update_Goods-SKU_Relations' },
          { text: 'Update Inbound Order Tracking', link: '/API_Reference/Fulfilled_by_TikTok_FBT/Update_Inbound_Order_Tracking' }
          ]
        },
        {
          text: 'Logistics',
          collapsed: true,
          items: [
          { text: 'Logistic API overview', link: '/API_Reference/Logistics/Logistic_API_overview' },
          { text: 'Action Code Name', link: '/API_Reference/Logistics/Action_Code_Name' },
          { text: 'Additional Notes', link: '/API_Reference/Logistics/Additional_Notes' },
          { text: 'Check Shipping Template Existence', link: '/API_Reference/Logistics/Check_Shipping_Template_Existence' },
          { text: 'Get Global Seller Warehouses', link: '/API_Reference/Logistics/Get_Global_Seller_Warehouses' },
          { text: 'Get Logistics Tracking', link: '/API_Reference/Logistics/Get_Logistics_Tracking' },
          { text: 'Get Shipping Providers', link: '/API_Reference/Logistics/Get_Shipping_Providers' },
          { text: 'Get Shipping Template Availability', link: '/API_Reference/Logistics/Get_Shipping_Template_Availability' },
          { text: 'Get Warehouse Delivery Options', link: '/API_Reference/Logistics/Get_Warehouse_Delivery_Options' },
          { text: 'Get Warehouse List', link: '/API_Reference/Logistics/Get_Warehouse_List' }
          ]
        },
        {
          text: 'Return and Refund',
          collapsed: true,
          items: [
          { text: 'Return, refund, and cancel API overview', link: '/API_Reference/Return_and_refund/Return,_refund,_and_cancel_API_overview' },
          { text: 'Approve Cancellation', link: '/API_Reference/Return_and_refund/Approve_Cancellation' },
          { text: 'Approve Return', link: '/API_Reference/Return_and_refund/Approve_Return' },
          { text: 'Calculate Refund', link: '/API_Reference/Return_and_refund/Calculate_Refund' },
          { text: 'Cancel Order', link: '/API_Reference/Return_and_refund/Cancel_Order' },
          { text: 'Cancel reasons', link: '/API_Reference/Return_and_refund/Cancel_reasons' },
          { text: 'Create Return', link: '/API_Reference/Return_and_refund/Create_Return' },
          { text: 'Get Aftersale Eligibility', link: '/API_Reference/Return_and_refund/Get_Aftersale_Eligibility' },
          { text: 'Get Available Review Decisions', link: '/API_Reference/Return_and_refund/Get_Available_Review_Decisions' },
          { text: 'Get Decision Eligibility', link: '/API_Reference/Return_and_refund/Get_Decision_Eligibility' },
          { text: 'Get Reject Reasons', link: '/API_Reference/Return_and_refund/Get_Reject_Reasons' },
          { text: 'Get Return Records', link: '/API_Reference/Return_and_refund/Get_Return_Records' },
          { text: 'Refund reasons', link: '/API_Reference/Return_and_refund/Refund_reasons' },
          { text: 'Reject Cancellation', link: '/API_Reference/Return_and_refund/Reject_Cancellation' },
          { text: 'Reject Return', link: '/API_Reference/Return_and_refund/Reject_Return' },
          { text: 'Return reasons', link: '/API_Reference/Return_and_refund/Return_reasons' },
          { text: 'Review Aftersales Requests', link: '/API_Reference/Return_and_refund/Review_Aftersales_Requests' },
          { text: 'Search Aftersales Requests', link: '/API_Reference/Return_and_refund/Search_Aftersales_Requests' },
          { text: 'Search Cancellations', link: '/API_Reference/Return_and_refund/Search_Cancellations' },
          { text: 'Search Return Merchandise Authorizations', link: '/API_Reference/Return_and_refund/Search_Return_Merchandise_Authorizations' },
          { text: 'Search Returns', link: '/API_Reference/Return_and_refund/Search_Returns' },
          { text: 'Upload Return Shipping Information', link: '/API_Reference/Return_and_refund/Upload_Return_Shipping_Information' }
          ]
        },
        {
          text: 'Finance',
          collapsed: true,
          items: [
          { text: 'Finance API overview', link: '/API_Reference/Finance/Finance_API_overview' },
          { text: 'Get Payments', link: '/API_Reference/Finance/Get_Payments' },
          { text: 'Get Seller Financial Transactions', link: '/API_Reference/Finance/Get_Seller_Financial_Transactions' },
          { text: 'Get Statements', link: '/API_Reference/Finance/Get_Statements' },
          { text: 'Get TradeIn Account Transactions', link: '/API_Reference/Finance/Get_TradeIn_Account_Transactions' },
          { text: 'Get TradeIn Supplier Account Balance', link: '/API_Reference/Finance/Get_TradeIn_Supplier_Account_Balance' },
          { text: 'Get Transactions by Order', link: '/API_Reference/Finance/Get_Transactions_by_Order' },
          { text: 'Get Transactions by Statement', link: '/API_Reference/Finance/Get_Transactions_by_Statement' },
          { text: 'Get Unsettled Transactions', link: '/API_Reference/Finance/Get_Unsettled_Transactions' }
          ]
        },
        {
          text: 'Analytics',
          collapsed: true,
          items: [
          { text: 'Get ACC Audience Overview', link: '/API_Reference/Analytics/Get_ACC_Audience_Overview' },
          { text: 'Get Off Site Performance Overview', link: '/API_Reference/Analytics/Get_Off_Site_Performance_Overview' },
          { text: 'Get Shop LIVE Performance Overview', link: '/API_Reference/Analytics/Get_Shop_LIVE_Performance_Overview' },
          { text: 'Get Shop Video Performance Overview', link: '/API_Reference/Analytics/Get_Shop_Video_Performance_Overview' },
          { text: 'Get SPS Overview', link: '/API_Reference/Analytics/Get_SPS_Overview' },
          { text: 'Get ACC Audience Penetration', link: '/API_Reference/Analytics/Get_ACC_Audience_Penetration' },
          { text: 'Get ACC Audience Preference List', link: '/API_Reference/Analytics/Get_ACC_Audience_Preference_List' },
          { text: 'Get ACC Audience Preference Summary', link: '/API_Reference/Analytics/Get_ACC_Audience_Preference_Summary' },
          { text: 'Get ACC Brands', link: '/API_Reference/Analytics/Get_ACC_Brands' },
          { text: 'Get ACC LIVE Sales Factors', link: '/API_Reference/Analytics/Get_ACC_LIVE_Sales_Factors' },
          { text: 'Get ACC Top Sales Categories', link: '/API_Reference/Analytics/Get_ACC_Top_Sales_Categories' },
          { text: 'Get Bestselling Creators', link: '/API_Reference/Analytics/Get_Bestselling_Creators' },
          { text: 'Get Bestselling LIVE Sessions', link: '/API_Reference/Analytics/Get_Bestselling_LIVE_Sessions' },
          { text: 'Get Bestselling Products', link: '/API_Reference/Analytics/Get_Bestselling_Products' },
          { text: 'Get Bestselling Videos', link: '/API_Reference/Analytics/Get_Bestselling_Videos' },
          { text: 'Get Live Room Core Stats', link: '/API_Reference/Analytics/Get_Live_Room_Core_Stats' },
          { text: 'Get Live Room GMV and Order Trends', link: '/API_Reference/Analytics/Get_Live_Room_GMV_and_Order_Trends' },
          { text: 'Get Live Room Interactive Trends', link: '/API_Reference/Analytics/Get_Live_Room_Interactive_Trends' },
          { text: 'Get Live Room Product Stats', link: '/API_Reference/Analytics/Get_Live_Room_Product_Stats' },
          { text: 'Get Live Room Traffic Performance', link: '/API_Reference/Analytics/Get_Live_Room_Traffic_Performance' },
          { text: 'Get Live Room User Portraits', link: '/API_Reference/Analytics/Get_Live_Room_User_Portraits' },
          { text: 'Get Live Room View Trends', link: '/API_Reference/Analytics/Get_Live_Room_View_Trends' },
          { text: 'Get Off Site Audience Insights', link: '/API_Reference/Analytics/Get_Off_Site_Audience_Insights' },
          { text: 'Get Off Site Performance Details', link: '/API_Reference/Analytics/Get_Off_Site_Performance_Details' },
          { text: 'Get Shop LIVE Minute Performance', link: '/API_Reference/Analytics/Get_Shop_LIVE_Minute_Performance' },
          { text: 'Get Shop LIVE Performance List', link: '/API_Reference/Analytics/Get_Shop_LIVE_Performance_List' },
          { text: 'Get Shop LIVE Products Performance List', link: '/API_Reference/Analytics/Get_Shop_LIVE_Products_Performance_List' },
          { text: 'Get Shop Off Site Pixels', link: '/API_Reference/Analytics/Get_Shop_Off_Site_Pixels' },
          { text: 'Get Shop Performance', link: '/API_Reference/Analytics/Get_Shop_Performance' },
          { text: 'Get Shop Performance Per Hour', link: '/API_Reference/Analytics/Get_Shop_Performance_Per_Hour' },
          { text: 'Get Shop Product Performance Detail', link: '/API_Reference/Analytics/Get_Shop_Product_Performance_Detail' },
          { text: 'Get Shop Product Performance List', link: '/API_Reference/Analytics/Get_Shop_Product_Performance_List' },
          { text: 'Get Shop SKU Performance Detail', link: '/API_Reference/Analytics/Get_Shop_SKU_Performance_Detail' },
          { text: 'Get Shop SKU Performance List', link: '/API_Reference/Analytics/Get_Shop_SKU_Performance_List' },
          { text: 'Get Shop Video Performance Details', link: '/API_Reference/Analytics/Get_Shop_Video_Performance_Details' },
          { text: 'Get Shop Video Performance List', link: '/API_Reference/Analytics/Get_Shop_Video_Performance_List' },
          { text: 'Get Shop Video Product Performance List', link: '/API_Reference/Analytics/Get_Shop_Video_Product_Performance_List' },
          { text: 'Get Shop Videos Performance Details', link: '/API_Reference/Analytics/Get_Shop_Videos_Performance_Details' },
          { text: 'Get SPS Metric Diagnosis', link: '/API_Reference/Analytics/Get_SPS_Metric_Diagnosis' },
          { text: 'Get SPS Metric Problem Details', link: '/API_Reference/Analytics/Get_SPS_Metric_Problem_Details' },
          { text: 'Get SPS Metric Top Items', link: '/API_Reference/Analytics/Get_SPS_Metric_Top_Items' },
          { text: 'Get SPS Metrics', link: '/API_Reference/Analytics/Get_SPS_Metrics' },
          { text: 'Get Video Performances', link: '/API_Reference/Analytics/Get_Video_Performances' }
          ]
        },
        {
          text: 'Customer Service',
          collapsed: true,
          items: [
          { text: 'Customer Service API overview', link: '/API_Reference/Customer_service/Customer_Service_API_overview' },
          { text: 'Create Conversation', link: '/API_Reference/Customer_service/Create_Conversation' },
          { text: 'End Session', link: '/API_Reference/Customer_service/End_Session' },
          { text: 'Get Agent Settings', link: '/API_Reference/Customer_service/Get_Agent_Settings' },
          { text: 'Get Conversation', link: '/API_Reference/Customer_service/Get_Conversation' },
          { text: 'Get Conversation Messages', link: '/API_Reference/Customer_service/Get_Conversation_Messages' },
          { text: 'Get Conversations', link: '/API_Reference/Customer_service/Get_Conversations' },
          { text: 'Get Customer Service Performance', link: '/API_Reference/Customer_service/Get_Customer_Service_Performance' },
          { text: 'Mark Buyer Messages as Read', link: '/API_Reference/Customer_service/Mark_Buyer_Messages_as_Read' },
          { text: 'Message Types', link: '/API_Reference/Customer_service/Message_Types' },
          { text: 'Post-sales Solutions for Customer Services', link: '/API_Reference/Customer_service/Post-sales_Solutions_for_Customer_Services' },
          { text: 'Search Sessions', link: '/API_Reference/Customer_service/Search_Sessions' },
          { text: 'Send Message', link: '/API_Reference/Customer_service/Send_Message' },
          { text: 'Update Agent Settings', link: '/API_Reference/Customer_service/Update_Agent_Settings' },
          { text: 'Upload Image for Buyer Messages', link: '/API_Reference/Customer_service/Upload_Image_for_Buyer_Messages' }
          ]
        },
        {
          text: 'Customer Engagement',
          collapsed: true,
          items: [
          { text: 'Customer engagement API overview', link: '/API_Reference/Customer_engagement/Customer_engagement_API_overview' },
          { text: 'Create Custom Engagement Task', link: '/API_Reference/Customer_engagement/Create_Custom_Engagement_Task' },
          { text: 'Create Engagement Task', link: '/API_Reference/Customer_engagement/Create_Engagement_Task' },
          { text: 'Get Engagement Feature Permissions', link: '/API_Reference/Customer_engagement/Get_Engagement_Feature_Permissions' },
          { text: 'Get Engagement Task Performances', link: '/API_Reference/Customer_engagement/Get_Engagement_Task_Performances' },
          { text: 'Get Message Templates', link: '/API_Reference/Customer_engagement/Get_Message_Templates' },
          { text: 'Send Engagement Message', link: '/API_Reference/Customer_engagement/Send_Engagement_Message' }
          ]
        },
        {
          text: 'Affiliate Creator',
          collapsed: true,
          items: [
          { text: 'Affiliate Creator API overview', link: '/API_Reference/Affiliate_creator/Affiliate_Creator_API_overview' },
          { text: 'Add Showcase Products', link: '/API_Reference/Affiliate_creator/Add_Showcase_Products' },
          { text: 'Check Creator Sample Eligibility', link: '/API_Reference/Affiliate_creator/Check_Creator_Sample_Eligibility' },
          { text: 'Create Video Precheck Task', link: '/API_Reference/Affiliate_creator/Create_Video_Precheck_Task' },
          { text: 'Creator Search Sample Application Fulfillments', link: '/API_Reference/Affiliate_creator/Creator_Search_Sample_Application_Fulfillments' },
          { text: 'Generate General Sharing Links', link: '/API_Reference/Affiliate_creator/Generate_General_Sharing_Links' },
          { text: 'Generate Publisher Sharing Links in Batch', link: '/API_Reference/Affiliate_creator/Generate_Publisher_Sharing_Links_in_Batch' },
          { text: 'Get Creator Profile', link: '/API_Reference/Affiliate_creator/Get_Creator_Profile' },
          { text: 'Get Creator Sample Application Detail', link: '/API_Reference/Affiliate_creator/Get_Creator_Sample_Application_Detail' },
          { text: 'Get Open Collaboration Product List By Product Ids', link: '/API_Reference/Affiliate_creator/Get_Open_Collaboration_Product_List_By_Product_Ids' },
          { text: 'Get Shop Products', link: '/API_Reference/Affiliate_creator/Get_Shop_Products' },
          { text: 'Get Shoppable Video Precheck Result', link: '/API_Reference/Affiliate_creator/Get_Shoppable_Video_Precheck_Result' },
          { text: 'Get Shoppable Video Status', link: '/API_Reference/Affiliate_creator/Get_Shoppable_Video_Status' },
          { text: 'Get Showcase Products', link: '/API_Reference/Affiliate_creator/Get_Showcase_Products' },
          { text: 'Get Tokopedia and TikTok Shop Product ID Mappings', link: '/API_Reference/Affiliate_creator/Get_Tokopedia_and_TikTok_Shop_Product_ID_Mappings' },
          { text: 'Map Tokopedia to TikTok Shop Product IDs', link: '/API_Reference/Affiliate_creator/Map_Tokopedia_to_TikTok_Shop_Product_IDs' },
          { text: 'Move Showcase Products to the Top', link: '/API_Reference/Affiliate_creator/Move_Showcase_Products_to_the_Top' },
          { text: 'Post Shoppable Photos', link: '/API_Reference/Affiliate_creator/Post_Shoppable_Photos' },
          { text: 'Post Shoppable Video', link: '/API_Reference/Affiliate_creator/Post_Shoppable_Video' },
          { text: 'Remove Showcase Products', link: '/API_Reference/Affiliate_creator/Remove_Showcase_Products' },
          { text: 'Search Affiliate Orders by Creator', link: '/API_Reference/Affiliate_creator/Search_Affiliate_Orders_by_Creator' },
          { text: 'Search Creator Affiliate Orders', link: '/API_Reference/Affiliate_creator/Search_Creator_Affiliate_Orders' },
          { text: 'Search Creator Sample Applications', link: '/API_Reference/Affiliate_creator/Search_Creator_Sample_Applications' },
          { text: 'Search Creator Target Collaborations', link: '/API_Reference/Affiliate_creator/Search_Creator_Target_Collaborations' },
          { text: 'Search Open Collaboration Products', link: '/API_Reference/Affiliate_creator/Search_Open_Collaboration_Products' },
          { text: 'Upload Shoppable Photo File', link: '/API_Reference/Affiliate_creator/Upload_Shoppable_Photo_File' },
          { text: 'Upload Shoppable Video File', link: '/API_Reference/Affiliate_creator/Upload_Shoppable_Video_File' }
          ]
        },
        {
          text: 'Affiliate Partner',
          collapsed: true,
          items: [
          { text: 'Affiliate Partner API overview', link: '/API_Reference/Affiliate_partner/Affiliate_Partner_API_overview' },
          { text: 'Create Affiliate Partner Campaign', link: '/API_Reference/Affiliate_partner/Create_Affiliate_Partner_Campaign' },
          { text: 'Edit Affiliate Partner Campaign', link: '/API_Reference/Affiliate_partner/Edit_Affiliate_Partner_Campaign' },
          { text: 'Generate Affiliate Partner Campaign Product Link', link: '/API_Reference/Affiliate_partner/Generate_Affiliate_Partner_Campaign_Product_Link' },
          { text: 'Generate Campaign Product Promotion Links in Batch', link: '/API_Reference/Affiliate_partner/Generate_Campaign_Product_Promotion_Links_in_Batch' },
          { text: 'Get Affiliate Campaign Creator Product Content Statistics', link: '/API_Reference/Affiliate_partner/Get_Affiliate_Campaign_Creator_Product_Content_Statistics' },
          { text: 'Get Affiliate Campaign Creator Product Sample Status', link: '/API_Reference/Affiliate_partner/Get_Affiliate_Campaign_Creator_Product_Sample_Status' },
          { text: 'Get Affiliate Partner Campaign Detail', link: '/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_Detail' },
          { text: 'Get Affiliate Partner Campaign List', link: '/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_List' },
          { text: 'Get Affiliate Partner Campaign Product List', link: '/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_Product_List' },
          { text: 'Get Campaign Product Performance List', link: '/API_Reference/Affiliate_partner/Get_Campaign_Product_Performance_List' },
          { text: 'Get Creator Performance for Campaign Product', link: '/API_Reference/Affiliate_partner/Get_Creator_Performance_for_Campaign_Product' },
          { text: 'Publish Affiliate Partner Campaign', link: '/API_Reference/Affiliate_partner/Publish_Affiliate_Partner_Campaign' },
          { text: 'Review Affiliate Partner Campaign Product', link: '/API_Reference/Affiliate_partner/Review_Affiliate_Partner_Campaign_Product' },
          { text: 'Search CAP Affiliate Orders', link: '/API_Reference/Affiliate_partner/Search_CAP_Affiliate_Orders' },
          { text: 'Search TAP Affiliate Orders', link: '/API_Reference/Affiliate_partner/Search_TAP_Affiliate_Orders' }
          ]
        },
        {
          text: 'Affiliate Seller',
          collapsed: true,
          items: [
          { text: 'Affiliate Seller API overview', link: '/API_Reference/Affiliate_seller/Affiliate_Seller_API_overview' },
          { text: 'Check Target Collaboration Conflicts', link: '/API_Reference/Affiliate_seller/Check_Target_Collaboration_Conflicts' },
          { text: 'Create Compass Offline Export Task', link: '/API_Reference/Affiliate_seller/Create_Compass_Offline_Export_Task' },
          { text: 'Create Open Collaboration', link: '/API_Reference/Affiliate_seller/Create_Open_Collaboration' },
          { text: 'Create Target Collaboration', link: '/API_Reference/Affiliate_seller/Create_Target_Collaboration' },
          { text: 'Download Compass Task File', link: '/API_Reference/Affiliate_seller/Download_Compass_Task_File' },
          { text: 'Edit Open Collaboration Sample Rule', link: '/API_Reference/Affiliate_seller/Edit_Open_Collaboration_Sample_Rule' },
          { text: 'Edit Open Collaboration Settings', link: '/API_Reference/Affiliate_seller/Edit_Open_Collaboration_Settings' },
          { text: 'Generate Affiliate Product Promotion Link', link: '/API_Reference/Affiliate_seller/Generate_Affiliate_Product_Promotion_Link' },
          { text: 'Generate Target Collaboration Link', link: '/API_Reference/Affiliate_seller/Generate_Target_Collaboration_Link' },
          { text: 'Get Compass Task List', link: '/API_Reference/Affiliate_seller/Get_Compass_Task_List' },
          { text: 'Get Conversation List', link: '/API_Reference/Affiliate_seller/Get_Conversation_List' },
          { text: 'Get Creator Conversation Messages', link: '/API_Reference/Affiliate_seller/Get_Creator_Conversation_Messages' },
          { text: 'Get Creator Marketplace Advanced Search Filters', link: '/API_Reference/Affiliate_seller/Get_Creator_Marketplace_Advanced_Search_Filters' },
          { text: 'Get Inbox Category Counts', link: '/API_Reference/Affiliate_seller/Get_Inbox_Category_Counts' },
          { text: 'Get Latest Unread Messages', link: '/API_Reference/Affiliate_seller/Get_Latest_Unread_Messages' },
          { text: 'Get Marketplace Creator Performance', link: '/API_Reference/Affiliate_seller/Get_Marketplace_Creator_Performance' },
          { text: 'Get Open Collaboration Creator Content Details', link: '/API_Reference/Affiliate_seller/Get_Open_Collaboration_Creator_Content_Details' },
          { text: 'Get Open Collaboration Sample Rules', link: '/API_Reference/Affiliate_seller/Get_Open_Collaboration_Sample_Rules' },
          { text: 'Get Open Collaboration Settings', link: '/API_Reference/Affiliate_seller/Get_Open_Collaboration_Settings' },
          { text: 'Get or Create Creator Conversation', link: '/API_Reference/Affiliate_seller/Get_or_Create_Creator_Conversation' },
          { text: 'Get Weekly Creator Outreach Quota', link: '/API_Reference/Affiliate_seller/Get_Weekly_Creator_Outreach_Quota' },
          { text: 'Get Weekly Creator Outreach Records', link: '/API_Reference/Affiliate_seller/Get_Weekly_Creator_Outreach_Records' },
          { text: 'Mark Conversations as Read', link: '/API_Reference/Affiliate_seller/Mark_Conversations_as_Read' },
          { text: 'Query Creator Promotion Details in Target Collaboration', link: '/API_Reference/Affiliate_seller/Query_Creator_Promotion_Details_in_Target_Collaboration' },
          { text: 'Query Target Collaboration Detail', link: '/API_Reference/Affiliate_seller/Query_Target_Collaboration_Detail' },
          { text: 'Remove Creator From Open Collaboration Product', link: '/API_Reference/Affiliate_seller/Remove_Creator_From_Open_Collaboration_Product' },
          { text: 'Remove Open Collaboration', link: '/API_Reference/Affiliate_seller/Remove_Open_Collaboration' },
          { text: 'Remove Target Collaboration', link: '/API_Reference/Affiliate_seller/Remove_Target_Collaboration' },
          { text: 'Resolve Target Collaboration Conflicts', link: '/API_Reference/Affiliate_seller/Resolve_Target_Collaboration_Conflicts' },
          { text: 'Review a Sample Application', link: '/API_Reference/Affiliate_seller/Review_a_Sample_Application' },
          { text: 'Search Creators in Creator Marketplace', link: '/API_Reference/Affiliate_seller/Search_Creators_in_Creator_Marketplace' },
          { text: 'Search Open Collaborations', link: '/API_Reference/Affiliate_seller/Search_Open_Collaborations' },
          { text: 'Search Sample Application Fulfillments', link: '/API_Reference/Affiliate_seller/Search_Sample_Application_Fulfillments' },
          { text: 'Search Sample Applications', link: '/API_Reference/Affiliate_seller/Search_Sample_Applications' },
          { text: 'Search Seller Affiliate Orders', link: '/API_Reference/Affiliate_seller/Search_Seller_Affiliate_Orders' },
          { text: 'Search Target Collaborations', link: '/API_Reference/Affiliate_seller/Search_Target_Collaborations' },
          { text: 'Seller Get Sample Request Deeplink', link: '/API_Reference/Affiliate_seller/Seller_Get_Sample_Request_Deeplink' },
          { text: 'Seller Search Open Collaboration Products', link: '/API_Reference/Affiliate_seller/Seller_Search_Open_Collaboration_Products' },
          { text: 'Send IM Message', link: '/API_Reference/Affiliate_seller/Send_IM_Message' },
          { text: 'Update Conversation Status', link: '/API_Reference/Affiliate_seller/Update_Conversation_Status' },
          { text: 'Update Target Collaboration', link: '/API_Reference/Affiliate_seller/Update_Target_Collaboration' },
          { text: 'Upload Message Image', link: '/API_Reference/Affiliate_seller/Upload_Message_Image' },
          { text: 'Upload Message Image V2', link: '/API_Reference/Affiliate_seller/Upload_Message_Image_V2' }
          ]
        },
        {
          text: 'Supply Chain',
          collapsed: true,
          items: [
          { text: 'Upload File Init', link: '/API_Reference/Supply_chain/Upload_File_Init' }
          ]
        }
        ]
      },
      {
        text: 'Webhooks',
            collapsed: true,
            items: [
              {
                text: 'Order',
                collapsed: true,
                items: [
                  { text: '(1) Order Status Change', link: '/Webhooks/Order/(1)_Order_status_change' },
                  { text: '(11) Cancellation Status Change', link: '/Webhooks/Order/(11)_Cancellation_status_change' }
                ]
              },
              {
                text: 'Product',
                collapsed: true,
                items: [
                  { text: '(5) Product Status Change', link: '/Webhooks/Product/(5)_Product_status_change' },
                  { text: '(15) Product Information Change', link: '/Webhooks/Product/(15)_Product_information_change' },
                  { text: '(16) Product Creation', link: '/Webhooks/Product/(16)_Product_creation' },
                  { text: '(27) Inventory Status Change', link: '/Webhooks/Product/(27)_Inventory_status_change' }
                ]
              },
              {
                text: 'Fulfillment',
                collapsed: true,
                items: [
                  { text: '(36) Invoice Status Change', link: '/Webhooks/Fulfillment/(36)_Invoice_status_change' },
                  { text: '(21) Inbound FBT Order Status Change', link: '/Webhooks/Fulfilled_by_TikTok/(21)_Inbound_FBT_order_status_change' },
                  { text: '(24) FBT Inventory Update', link: '/Webhooks/Fulfilled_by_TikTok/(24)_FBT_inventory_update' }
                ]
              },
              {
                text: 'Logistics',
                collapsed: true,
                items: [
                  { text: '(3) Recipient Address Update', link: '/Webhooks/Logistics/(3)_Recipient_address_update' },
                  { text: '(4) Package Update', link: '/Webhooks/Logistics/(4)_Package_update' }
                ]
              },
              {
                text: 'Return and Refund',
                collapsed: true,
                items: [
                  { text: '(12) Return Status Change', link: '/Webhooks/Return_and_Refund/(12)_Return_status_change' },
                  { text: '(67) Refund Success', link: '/Webhooks/Return_and_Refund/(67)_Refund_Success' }
                ]
              },
              {
                text: 'Seller',
                collapsed: true,
                items: [
                  { text: '(6) Seller Deauthorization', link: '/Webhooks/Seller/(6)_Seller_deauthorization' },
                  { text: '(7) Authorization Expiration', link: '/Webhooks/Seller/(7)_Upcoming_authorization_expiration' }
                ]
              }
            ]
          }
        ],
        socialLinks: [
          { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
        ],
        search: {
          provider: 'local'
        },
        footer: {
          message: 'TikTok Shop Partner Center Documentation',
          copyright: 'Downloaded from partner.tiktokshop.com'
        }
      }
    },
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      link: '/zh/',
      title: 'TikTok Shop 合作伙伴中心',
      description: 'TikTok Shop 合作伙伴中心文档',
      themeConfig: {
        nav: [
          { text: '合作伙伴指南', link: '/zh/Partner_Guide/About_the_Partner_Center_Console' },
          { text: '开发者指南', link: '/zh/Developer_Guide/TikTok_Shop_developer_guide' },
          { text: '合作伙伴授权指南', link: '/zh/API_Reference/Guide' },
          { text: 'Webhooks', link: '/zh/Webhooks/Order/(1)_Order_status_change' }
        ],
        sidebar: [
          {
            text: '合作伙伴指南',
            collapsed: false,
            items: [
              { text: '关于合作伙伴中心控制台', link: '/zh/Partner_Guide/About_the_Partner_Center_Console' },
              {
                text: '合作伙伴类型',
                collapsed: true,
                items: [
                  { text: '开发者', link: '/zh/Partner_Guide/Partner_type/Developer' },
                  { text: 'TikTok Shop 合作伙伴 (TSP)', link: '/zh/Partner_Guide/Partner_type/TikTok_Shop_Partner_(TSP)' },
                  { text: '创作者经纪合作伙伴 (CAP)', link: '/zh/Partner_Guide/Partner_type/Creator_Agency_Partner_(CAP)' },
                  { text: '非美国联盟合作伙伴 (TAP)', link: '/zh/Partner_Guide/Partner_type/Non-US_TikTok_Shop_Affiliate_Partner_(TAP)' },
                  { text: '美国联盟合作伙伴 (TAP)', link: '/zh/Partner_Guide/Partner_type/US_TikTok_Shop_Affiliate_Partner_(TAP)' },
                  { text: '多渠道网络 (MCN)', link: '/zh/Partner_Guide/Partner_type/Multi-Channel_Network_(MCN)' }
                ]
              },
              {
                text: '成为合作伙伴',
                collapsed: true,
                items: [
                  { text: '注册为服务合作伙伴', link: '/zh/Partner_Guide/Become_a_partner/Register_as_a_service_partner' },
                  { text: '[美国] 经纪合作伙伴入驻指南', link: '/zh/Partner_Guide/Become_a_partner/[US]_Agency_Partner_Onboard_Guide' },
                  { text: '合作伙伴服务类别', link: '/zh/Partner_Guide/Become_a_partner/Partner_service_categories' },
                  { text: '合作伙伴注册申请要求', link: '/zh/Partner_Guide/Become_a_partner/Partner_registration_application_requirement' },
                  { text: '管理主账户和成员账户', link: '/zh/Partner_Guide/Become_a_partner/Managing_Main_and_Member_Accounts' }
                ]
              },
              {
                text: 'TSP 控制台指南',
                collapsed: true,
                items: [
                  { text: '创建和发布服务', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Create_and_publish_a_service' },
                  { text: '在应用和服务商店上架', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Listing_your_service_on_the_App_&_Service_Store' },
                  { text: '卖家线索池', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Seller_Leads_Pool' },
                  { text: '获取服务授权的步骤', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_TSP/Steps_to_Get_Service_Authorization' },
                  { text: 'TSP 访问功能', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_TSP/TSP_Access_Feature' }
                ]
              },
              {
                text: 'CAP/MCN 控制台指南',
                collapsed: true,
                items: [
                  { text: '查找创作者', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Creator_Management_-_Find_Creators' },
                  { text: '已关联创作者', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Creator_Management_-_Linked_Creators' },
                  { text: '商品管理', link: '/zh/Partner_Guide/Partner_Center_Console_Guides_for_CAP_and_MCN/Product_Management' }
                ]
              },
              {
                text: '财务',
                collapsed: true,
                items: [
                  { text: '[CAP/TAP] 财务指南（仅美国）', link: '/zh/Partner_Guide/Finance/[CAP_TAP]_Finance_guide_(US_only)' },
                  { text: '财务（非美国）', link: '/zh/Partner_Guide/Finance/Finance(Non-us)' }
                ]
              }
            ]
          },
          {
            text: '开发者指南',
            collapsed: false,
            items: [
              { text: 'TikTok Shop 开发者指南', link: '/zh/Developer_Guide/TikTok_Shop_developer_guide' },
              {
                text: '快速开始',
                collapsed: true,
                items: [
                  { text: '快速开始概览', link: '/zh/Developer_Guide/Get_started/Get_started_overview' },
                  { text: '应用类别选择指南', link: '/zh/Developer_Guide/Get_started/App_Category_Selection_Guide' }
                ]
              },
              {
                text: 'API 概念',
                collapsed: true,
                items: [
                  { text: '概述', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Overview' },
                  { text: '方法和端点', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Methods_and_endpoints' },
                  { text: '签名 API 请求', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Sign_your_API_request' },
                  { text: '公共参数', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Common_parameters' },
                  { text: '常见错误', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Common_errors' },
                  { text: '速率限制', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/Rate_limits' },
                  { text: 'API 版本控制', link: '/zh/Developer_Guide/TikTok_Shop_API_concepts/API_versioning' }
                ]
              },
              {
                text: '解决方案指南',
                collapsed: true,
                items: [
                  { text: '商品 API 解决方案指南', link: '/zh/Developer_Guide/Solution_Guidance/Product_API_Solution_Guide' },
                  { text: '订单和履约 API 指南', link: '/zh/Developer_Guide/Solution_Guidance/Orders_and_Fulfillment_API_Solution_Guide' },
                  { text: '联盟 API 解决方案指南', link: '/zh/Developer_Guide/Solution_Guidance/Affiliate_API_Solution_Guide' }
                ]
              },
              {
                text: 'API SDK',
                collapsed: true,
                items: [
                  { text: '概述', link: '/zh/Developer_Guide/TikTok_Shop_API_SDK/Overview' },
                  { text: '下载 SDK', link: '/zh/Developer_Guide/TikTok_Shop_API_SDK/Download_SDK' },
                  { text: '集成 Java SDK', link: '/zh/Developer_Guide/TikTok_Shop_API_SDK/Integrate_Java_SDK' },
                  { text: '集成 Node.js SDK', link: '/zh/Developer_Guide/TikTok_Shop_API_SDK/Integrate_Node.js_SDK' }
                ]
              },
              {
                text: 'Webhooks',
                collapsed: true,
                items: [
                  { text: '概述', link: '/zh/Developer_Guide/TikTok_Shop_webhooks/Overview' },
                  { text: '配置指南', link: '/zh/Developer_Guide/TikTok_Shop_webhooks/Configuration_guide' }
                ]
              }
            ]
          },
          {
            text: 'API 参考',
            collapsed: true,
            items: [
        {
          text: '工具',
          collapsed: true,
          items: [
          { text: '公共错误码', link: '/zh/API_Reference/Tools/Common_Error_Codes' },
          { text: '公共参数', link: '/zh/API_Reference/Tools/Common_Parameters' },
          { text: '获取 Access Token', link: '/zh/API_Reference/Tools/Get_Access_Token' },
          { text: '合作伙伴授权指南', link: '/zh/API_Reference/Tools/Partner_Authorization_Guide' }
          ]
        },
        {
          text: '授权',
          collapsed: true,
          items: [
          { text: '获取已授权类目资产', link: '/zh/API_Reference/Authorization/Get_Authorized_Category_Assets' },
          { text: '获取已授权店铺', link: '/zh/API_Reference/Authorization/Get_Authorized_Shops' }
          ]
        },
        {
          text: '事件',
          collapsed: true,
          items: [
          { text: '删除事件的 Webhook', link: '/zh/API_Reference/Event/Delete_Webhook_for_an_Event' },
          { text: '获取店铺 Webhook', link: '/zh/API_Reference/Event/Get_Shop_Webhooks' },
          { text: '更新店铺 Webhook', link: '/zh/API_Reference/Event/Update_Shop_Webhook' }
          ]
        },
        {
          text: '卖家',
          collapsed: true,
          items: [
          { text: '卖家 API 概览', link: '/zh/API_Reference/Seller/Seller_API_overview' },
          { text: '获取活跃店铺', link: '/zh/API_Reference/Seller/Get_Active_Shops' },
          { text: '获取全球商品权限', link: '/zh/API_Reference/Seller/Get_Global_Product_Permission' },
          { text: '获取店铺组及相关店铺', link: '/zh/API_Reference/Seller/Get_Shop_Group_and_Related_Shops' }
          ]
        },
        {
          text: '商品',
          collapsed: true,
          items: [
          { text: 'Products API 概览', link: '/zh/API_Reference/Products/Products_API_overview' },
          { text: '激活产品', link: '/zh/API_Reference/Products/Activate_Products' },
          { text: '检查上架前提条件', link: '/zh/API_Reference/Products/Check_Listing_Prerequisites' },
          { text: '检查产品上架', link: '/zh/API_Reference/Products/Check_Product_Listing' },
          { text: '常见错误', link: '/zh/API_Reference/Products/Common_mistakes' },
          { text: '创建分类升级任务', link: '/zh/API_Reference/Products/Create_Category_Upgrade_Task' },
          { text: '创建自定义品牌', link: '/zh/API_Reference/Products/Create_Custom_Brands' },
          { text: '创建 GPA 升级任务', link: '/zh/API_Reference/Products/Create_GPA_Upgrade_Task' },
          { text: '创建图片翻译任务', link: '/zh/API_Reference/Products/Create_Image_Translation_Tasks' },
          { text: '创建产品', link: '/zh/API_Reference/Products/Create_Product' },
          { text: '下架产品', link: '/zh/API_Reference/Products/Deactivate_Products' },
          { text: '删除产品', link: '/zh/API_Reference/Products/Delete_Products' },
          { text: '诊断和优化产品', link: '/zh/API_Reference/Products/Diagnose_and_Optimize_Product' },
          { text: '编辑产品', link: '/zh/API_Reference/Products/Edit_Product' },
          { text: '获取品牌', link: '/zh/API_Reference/Products/Get_Brands' },
          { text: '获取分类', link: '/zh/API_Reference/Products/Get_Categories' },
          { text: '获取分类属性', link: '/zh/API_Reference/Products/Get_Category_Attributes' },
          { text: '获取分类规则', link: '/zh/API_Reference/Products/Get_Category_Rules' },
          { text: '获取全球上架规则', link: '/zh/API_Reference/Products/Get_Global_Listing_Rules' },
          { text: '获取全球复制产品', link: '/zh/API_Reference/Products/Get_Global_Replicated_Products' },
          { text: '获取图片翻译任务', link: '/zh/API_Reference/Products/Get_Image_Translation_Tasks' },
          { text: '获取商机详情', link: '/zh/API_Reference/Products/Get_Opportunity_Detail' },
          { text: '获取产品', link: '/zh/API_Reference/Products/Get_Product' },
          { text: '获取产品诊断结果', link: '/zh/API_Reference/Products/Get_Product_Diagnoses' },
          { text: '获取产品包装建议', link: '/zh/API_Reference/Products/Get_Product_Package_Recommendations' },
          { text: '获取产品 SKPP 详情', link: '/zh/API_Reference/Products/Get_Product_SKPP_Detail' },
          { text: '获取产品 SEO 关键词', link: '/zh/API_Reference/Products/Get_Products_SEO_Words' },
          { text: '获取推荐产品标题和描述', link: '/zh/API_Reference/Products/Get_Recommended_Product_Title_And_Description' },
          { text: '获取店铺 SKPP 摘要', link: '/zh/API_Reference/Products/Get_Shop_SKPP_Summary' },
          { text: '获取提交记录', link: '/zh/API_Reference/Products/Get_Submission_Records' },
          { text: '库存搜索', link: '/zh/API_Reference/Products/Inventory_Search' },
          { text: '列出商机', link: '/zh/API_Reference/Products/List_Opportunities' },
          { text: '列出产品 SKPP 状态', link: '/zh/API_Reference/Products/List_Product_SKPP_Statuses' },
          { text: '上架质量诊断', link: '/zh/API_Reference/Products/Listing_quality_diagnosis' },
          { text: '优化图片', link: '/zh/API_Reference/Products/Optimize_Images' },
          { text: '部分编辑全球产品', link: '/zh/API_Reference/Products/Partial_Edit_Global_Product' },
          { text: '部分编辑产品', link: '/zh/API_Reference/Products/Partial_Edit_Product' },
          { text: '产品定价', link: '/zh/API_Reference/Products/Product_pricing' },
          { text: '推荐分类', link: '/zh/API_Reference/Products/Recommend_Category' },
          { text: '恢复产品', link: '/zh/API_Reference/Products/Recover_Products' },
          { text: '复制产品', link: '/zh/API_Reference/Products/Replicate_Product' },
          { text: '搜索产品', link: '/zh/API_Reference/Products/Search_Products' },
          { text: '搜索合规审核产品', link: '/zh/API_Reference/Products/Search_Products_for_Compliance_Auditing' },
          { text: '搜索尺码表', link: '/zh/API_Reference/Products/Search_Size_Charts' },
          { text: '通过商机提交产品', link: '/zh/API_Reference/Products/Submit_Product_via_Opportunity' },
          { text: '提交尺码表申诉', link: '/zh/API_Reference/Products/Submit_Size_Chart_Appeal' },
          { text: '建议品牌', link: '/zh/API_Reference/Products/Suggest_Brands' },
          { text: '更新库存', link: '/zh/API_Reference/Products/Update_Inventory' },
          { text: '更新价格', link: '/zh/API_Reference/Products/Update_Price' },
          { text: '更新库存操作设置', link: '/zh/API_Reference/Products/Update_Stock_Operation_Settings' },
          { text: '上传产品文件', link: '/zh/API_Reference/Products/Upload_Product_File' },
          { text: '上传产品图片', link: '/zh/API_Reference/Products/Upload_Product_Image' }
          ]
        },
        {
          text: '全球商品',
          collapsed: true,
          items: [
          { text: '创建全球产品', link: '/zh/API_Reference/Products_Global_Products/Create_Global_Product' },
          { text: '删除全球产品', link: '/zh/API_Reference/Products_Global_Products/Delete_Global_Products' },
          { text: '编辑全球产品', link: '/zh/API_Reference/Products_Global_Products/Edit_Global_Product' },
          { text: '获取全球属性', link: '/zh/API_Reference/Products_Global_Products/Get_Global_Attributes' },
          { text: '获取全球分类', link: '/zh/API_Reference/Products_Global_Products/Get_Global_Categories' },
          { text: '获取全球分类规则', link: '/zh/API_Reference/Products_Global_Products/Get_Global_Category_Rules' },
          { text: '获取全球产品', link: '/zh/API_Reference/Products_Global_Products/Get_Global_Product' },
          { text: '发布全球产品', link: '/zh/API_Reference/Products_Global_Products/Publish_Global_Product' },
          { text: '推荐全球分类', link: '/zh/API_Reference/Products_Global_Products/Recommend_Global_Categories' },
          { text: '搜索全球产品', link: '/zh/API_Reference/Products_Global_Products/Search_Global_Products' },
          { text: '更新全球库存', link: '/zh/API_Reference/Products_Global_Products/Update_Global_Inventory' }
          ]
        },
        {
          text: '合规',
          collapsed: true,
          items: [
          { text: '创建制造商', link: '/zh/API_Reference/Products_Compliance/Create_Manufacturer' },
          { text: '创建负责人', link: '/zh/API_Reference/Products_Compliance/Create_Responsible_Person' },
          { text: '部分编辑制造商', link: '/zh/API_Reference/Products_Compliance/Partial_Edit_Manufacturer' },
          { text: '部分编辑负责人', link: '/zh/API_Reference/Products_Compliance/Partial_Edit_Responsible_Person' },
          { text: '搜索制造商', link: '/zh/API_Reference/Products_Compliance/Search_Manufacturers' },
          { text: '搜索负责人', link: '/zh/API_Reference/Products_Compliance/Search_Responsible_Persons' }
          ]
        },
        {
          text: '促销',
          collapsed: true,
          items: [
          { text: 'Promotion API 概述', link: '/zh/API_Reference/Promotion/Promotion_API_overview' },
          { text: '创建 Promotion 活动', link: '/zh/API_Reference/Promotion/Create_Promotion_Activity' },
          { text: '停用活动', link: '/zh/API_Reference/Promotion/Deactivate_Activity' },
          { text: '获取活动详情', link: '/zh/API_Reference/Promotion/Get_Activity' },
          { text: '获取优惠券', link: '/zh/API_Reference/Promotion/Get_Coupon' },
          { text: '移除 Promotion 活动商品', link: '/zh/API_Reference/Promotion/Remove_Promotion_Activity_Products' },
          { text: '重新发布活动', link: '/zh/API_Reference/Promotion/Republish_Activity' },
          { text: '搜索优惠券列表', link: '/zh/API_Reference/Promotion/Search_Coupon_List' },
          { text: '搜索促销活动', link: '/zh/API_Reference/Promotion/Search_Promotion_Activities' },
          { text: '运费折扣支持区域', link: '/zh/API_Reference/Promotion/Shipping_discount_supported_areas' },
          { text: '更新 Promotion 活动', link: '/zh/API_Reference/Promotion/Update_Promotion_Activity' },
          { text: '更新促销活动商品', link: '/zh/API_Reference/Promotion/Update_Promotion_Activity_Products' }
          ]
        },
        {
          text: '订单',
          collapsed: true,
          items: [
          { text: '订单 API 概览', link: '/zh/API_Reference/Orders/Order_API_overview' },
          { text: '添加外部订单引用', link: '/zh/API_Reference/Orders/Add_External_Order_References' },
          { text: '获取外部订单引用', link: '/zh/API_Reference/Orders/Get_External_Order_References' },
          { text: '获取订单详情', link: '/zh/API_Reference/Orders/Get_Order_Detail' },
          { text: '获取订单列表', link: '/zh/API_Reference/Orders/Get_Order_List' },
          { text: '获取订单价格详情', link: '/zh/API_Reference/Orders/Get_Order_Price_Details' },
          { text: '通过外部订单引用搜索订单', link: '/zh/API_Reference/Orders/Search_Orders_by_External_Order_Reference' },
          { text: '搜索 POD 定制详情', link: '/zh/API_Reference/Orders/Search_POD_Customization_Details' },
          { text: '更新盲盒开箱结果', link: '/zh/API_Reference/Orders/Update_The_Blind_Box_Opening_Results' }
          ]
        },
        {
          text: '履约',
          collapsed: true,
          items: [
          { text: 'Fulfillment API 概述', link: '/zh/API_Reference/Fulfillment/Fulfillment_API_overview' },
          { text: '批量发货 Package', link: '/zh/API_Reference/Fulfillment/Batch_Ship_Packages' },
          { text: '检查 TikTok Shipping 和 Collection by TikTok 覆盖范围', link: '/zh/API_Reference/Fulfillment/Check_TikTok_Shipping_and_Collection_by_TikTok_Coverage' },
          { text: '合并 Package', link: '/zh/API_Reference/Fulfillment/Combine_Package' },
          { text: '确认订单拆分', link: '/zh/API_Reference/Fulfillment/Confirm_Order_Split' },
          { text: '确认包裹发货', link: '/zh/API_Reference/Fulfillment/Confirm_Package_Shipment' },
          { text: '创建首程 bundle', link: '/zh/API_Reference/Fulfillment/Create_First_Mile_Bundle' },
          { text: '创建首程 Bundle (V2)', link: '/zh/API_Reference/Fulfillment/Create_First_Mile_Bundle(V2)' },
          { text: '创建 Package', link: '/zh/API_Reference/Fulfillment/Create_Packages' },
          { text: '获取符合条件的 shipping 服务', link: '/zh/API_Reference/Fulfillment/Get_Eligible_Shipping_Services' },
          { text: '获取订单海关要求', link: '/zh/API_Reference/Fulfillment/Get_Order_Customs_Requirements' },
          { text: '获取订单拆包属性', link: '/zh/API_Reference/Fulfillment/Get_Order_Split_Attributes' },
          { text: '获取订单 Tracking 信息', link: '/zh/API_Reference/Fulfillment/Get_Order_Tracking' },
          { text: '获取 Package 详情', link: '/zh/API_Reference/Fulfillment/Get_Package_Detail' },
          { text: '获取 Package 交接时间段', link: '/zh/API_Reference/Fulfillment/Get_Package_Handover_Time_Slots' },
          { text: '获取 Package Shipping 单据', link: '/zh/API_Reference/Fulfillment/Get_Package_Shipping_Document' },
          { text: '获取 POD 定制详情', link: '/zh/API_Reference/Fulfillment/Get_POD_Customization_Details' },
          { text: '标记包裹为已发货', link: '/zh/API_Reference/Fulfillment/Mark_Package_As_Shipped' },
          { text: '搜索可合并的 Package', link: '/zh/API_Reference/Fulfillment/Search_Combinable_Packages' },
          { text: '搜索 Package', link: '/zh/API_Reference/Fulfillment/Search_Package' },
          { text: '发货 Package', link: '/zh/API_Reference/Fulfillment/Ship_Package' },
          { text: '提交清关信息', link: '/zh/API_Reference/Fulfillment/Submit_Customs_Clearance_Information' },
          { text: '提交兑换信息', link: '/zh/API_Reference/Fulfillment/Submit_Redemption_Information' },
          { text: '物流状态更新', link: '/zh/API_Reference/Fulfillment/Tracking_status_update' },
          { text: '取消合并 Package', link: '/zh/API_Reference/Fulfillment/Uncombine_Packages' },
          { text: '更新订单 Shipping 信息', link: '/zh/API_Reference/Fulfillment/Update_Order_Shipping_Info' },
          { text: '更新 Package 配送状态', link: '/zh/API_Reference/Fulfillment/Update_Package_Delivery_Status' },
          { text: '更新包裹物流信息', link: '/zh/API_Reference/Fulfillment/Update_Package_Shipping_Info' },
          { text: '上传发票', link: '/zh/API_Reference/Fulfillment/Upload_Invoice' },
          { text: '上传交付证明文件', link: '/zh/API_Reference/Fulfillment/Upload_Proof_of_Delivery_File' },
          { text: '上传交付证明图片', link: '/zh/API_Reference/Fulfillment/Upload_Proof_of_Delivery_Image' }
          ]
        },
        {
          text: 'TikTok 履约 (FBT)',
          collapsed: true,
          items: [
          { text: 'FBT Inbound API 概述指南', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/FBT_Inbound_API_Overview_Guide' },
          { text: '取消 FBT MCF 订单', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Cancel_FBT_MCF_Order' },
          { text: '取消 Inbound 订单', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Cancel_Inbound_Order' },
          { text: '确认 Inbound 方式', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Confirm_Inbound_Method' },
          { text: '创建 FBT 商品', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Create_FBT_Goods' },
          { text: '创建 FBT MCF 订单', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Create_FBT_MCF_Order' },
          { text: '创建或更新 Inbound Plan', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Create_or_Update_Inbound_Plan' },
          { text: '获取 FBT Inbound 订单详情', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Inbound_Order_Details' },
          { text: '获取 FBT MCF 订单状态', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_MCF_Order_Status' },
          { text: '获取 FBT Merchant MCF 状态', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Merchant_MCF_Status' },
          { text: '获取 FBT Merchant 已入驻区域', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Merchant_Onboarded_Regions' },
          { text: '获取 FBT Warehouse 列表', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_FBT_Warehouse_List' },
          { text: '获取 Inbound 方式详情', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Get_Inbound_Method_Detail' },
          { text: '列出可用 Inbound 方式', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/List_Available_Inbound_Methods' },
          { text: '打印 Inbound 订单标签', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Print_Inbound_Order_Labels' },
          { text: '查询 MCF 商品 Inventory', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Query_Goods_Inventory_For_MCF' },
          { text: '搜索 FBT Inventory', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Search_FBT_Inventory' },
          { text: '搜索 FBT Inventory 记录', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Search_FBT_Inventory_Record' },
          { text: '查询商品危险品和保质期信息', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Search_Goods_Hazmat_And_Expiration_Info' },
          { text: '搜索商品信息', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Search_Goods_Info' },
          { text: '发货 Inbound 订单', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Ship_Inbound_Order' },
          { text: '更新 FBT 商品信息', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Update_FBT_Goods_Info' },
          { text: '更新 Goods-SKU 关联关系', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Update_Goods-SKU_Relations' },
          { text: '更新 Inbound 订单追踪信息', link: '/zh/API_Reference/Fulfilled_by_TikTok_FBT/Update_Inbound_Order_Tracking' }
          ]
        },
        {
          text: '物流',
          collapsed: true,
          items: [
          { text: 'Logistics API 概览', link: '/zh/API_Reference/Logistics/Logistic_API_overview' },
          { text: 'Action Code 名称对照表', link: '/zh/API_Reference/Logistics/Action_Code_Name' },
          { text: '补充说明', link: '/zh/API_Reference/Logistics/Additional_Notes' },
          { text: '检查运费模板是否存在', link: '/zh/API_Reference/Logistics/Check_Shipping_Template_Existence' },
          { text: '获取全球卖家仓库', link: '/zh/API_Reference/Logistics/Get_Global_Seller_Warehouses' },
          { text: '获取物流追踪信息', link: '/zh/API_Reference/Logistics/Get_Logistics_Tracking' },
          { text: '获取物流服务商', link: '/zh/API_Reference/Logistics/Get_Shipping_Providers' },
          { text: '获取运费模板可用性', link: '/zh/API_Reference/Logistics/Get_Shipping_Template_Availability' },
          { text: '获取仓库配送选项', link: '/zh/API_Reference/Logistics/Get_Warehouse_Delivery_Options' },
          { text: '获取仓库列表', link: '/zh/API_Reference/Logistics/Get_Warehouse_List' }
          ]
        },
        {
          text: '退货退款',
          collapsed: true,
          items: [
          { text: 'Return, refund, and cancel API 概览', link: '/zh/API_Reference/Return_and_refund/Return,_refund,_and_cancel_API_overview' },
          { text: '批准取消', link: '/zh/API_Reference/Return_and_refund/Approve_Cancellation' },
          { text: '批准退货', link: '/zh/API_Reference/Return_and_refund/Approve_Return' },
          { text: '计算退款', link: '/zh/API_Reference/Return_and_refund/Calculate_Refund' },
          { text: '取消订单', link: '/zh/API_Reference/Return_and_refund/Cancel_Order' },
          { text: '取消原因', link: '/zh/API_Reference/Return_and_refund/Cancel_reasons' },
          { text: '创建退货', link: '/zh/API_Reference/Return_and_refund/Create_Return' },
          { text: '获取售后资格', link: '/zh/API_Reference/Return_and_refund/Get_Aftersale_Eligibility' },
          { text: '获取可用审核决策', link: '/zh/API_Reference/Return_and_refund/Get_Available_Review_Decisions' },
          { text: '获取决策资格', link: '/zh/API_Reference/Return_and_refund/Get_Decision_Eligibility' },
          { text: '获取拒绝原因', link: '/zh/API_Reference/Return_and_refund/Get_Reject_Reasons' },
          { text: '获取退货记录', link: '/zh/API_Reference/Return_and_refund/Get_Return_Records' },
          { text: '退款原因', link: '/zh/API_Reference/Return_and_refund/Refund_reasons' },
          { text: '拒绝取消', link: '/zh/API_Reference/Return_and_refund/Reject_Cancellation' },
          { text: '拒绝退货', link: '/zh/API_Reference/Return_and_refund/Reject_Return' },
          { text: '退货原因', link: '/zh/API_Reference/Return_and_refund/Return_reasons' },
          { text: '审核售后请求', link: '/zh/API_Reference/Return_and_refund/Review_Aftersales_Requests' },
          { text: '搜索售后请求', link: '/zh/API_Reference/Return_and_refund/Search_Aftersales_Requests' },
          { text: '搜索取消', link: '/zh/API_Reference/Return_and_refund/Search_Cancellations' },
          { text: '搜索退货授权', link: '/zh/API_Reference/Return_and_refund/Search_Return_Merchandise_Authorizations' },
          { text: '搜索退货', link: '/zh/API_Reference/Return_and_refund/Search_Returns' },
          { text: '上传退货物流信息', link: '/zh/API_Reference/Return_and_refund/Upload_Return_Shipping_Information' }
          ]
        },
        {
          text: '财务',
          collapsed: true,
          items: [
          { text: 'Finance API 概述', link: '/zh/API_Reference/Finance/Finance_API_overview' },
          { text: '获取付款', link: '/zh/API_Reference/Finance/Get_Payments' },
          { text: '获取卖家财务交易', link: '/zh/API_Reference/Finance/Get_Seller_Financial_Transactions' },
          { text: '获取对账单', link: '/zh/API_Reference/Finance/Get_Statements' },
          { text: '获取 TradeIn 账户交易', link: '/zh/API_Reference/Finance/Get_TradeIn_Account_Transactions' },
          { text: '获取 TradeIn 供应商账户余额', link: '/zh/API_Reference/Finance/Get_TradeIn_Supplier_Account_Balance' },
          { text: '按订单获取交易', link: '/zh/API_Reference/Finance/Get_Transactions_by_Order' },
          { text: '按对账单获取交易', link: '/zh/API_Reference/Finance/Get_Transactions_by_Statement' },
          { text: '获取未结算交易', link: '/zh/API_Reference/Finance/Get_Unsettled_Transactions' }
          ]
        },
        {
          text: '数据分析',
          collapsed: true,
          items: [
          { text: '获取 ACC 受众概览', link: '/zh/API_Reference/Analytics/Get_ACC_Audience_Overview' },
          { text: '获取站外表现概览', link: '/zh/API_Reference/Analytics/Get_Off_Site_Performance_Overview' },
          { text: '获取店铺直播表现概览', link: '/zh/API_Reference/Analytics/Get_Shop_LIVE_Performance_Overview' },
          { text: '获取店铺视频表现概览', link: '/zh/API_Reference/Analytics/Get_Shop_Video_Performance_Overview' },
          { text: '获取 SPS 概览', link: '/zh/API_Reference/Analytics/Get_SPS_Overview' },
          { text: '获取 ACC 受众渗透率', link: '/zh/API_Reference/Analytics/Get_ACC_Audience_Penetration' },
          { text: '获取 ACC 受众偏好列表', link: '/zh/API_Reference/Analytics/Get_ACC_Audience_Preference_List' },
          { text: '获取 ACC 受众偏好摘要', link: '/zh/API_Reference/Analytics/Get_ACC_Audience_Preference_Summary' },
          { text: '获取 ACC 品牌', link: '/zh/API_Reference/Analytics/Get_ACC_Brands' },
          { text: '获取 ACC 直播销售因素', link: '/zh/API_Reference/Analytics/Get_ACC_LIVE_Sales_Factors' },
          { text: '获取 ACC 热销类目', link: '/zh/API_Reference/Analytics/Get_ACC_Top_Sales_Categories' },
          { text: '获取畅销达人', link: '/zh/API_Reference/Analytics/Get_Bestselling_Creators' },
          { text: '获取畅销 LIVE 场次', link: '/zh/API_Reference/Analytics/Get_Bestselling_LIVE_Sessions' },
          { text: '获取畅销商品', link: '/zh/API_Reference/Analytics/Get_Bestselling_Products' },
          { text: '获取畅销 video', link: '/zh/API_Reference/Analytics/Get_Bestselling_Videos' },
          { text: '获取直播间核心统计', link: '/zh/API_Reference/Analytics/Get_Live_Room_Core_Stats' },
          { text: '获取直播间 GMV 和订单趋势', link: '/zh/API_Reference/Analytics/Get_Live_Room_GMV_and_Order_Trends' },
          { text: '获取直播间互动趋势', link: '/zh/API_Reference/Analytics/Get_Live_Room_Interactive_Trends' },
          { text: '获取直播间商品统计', link: '/zh/API_Reference/Analytics/Get_Live_Room_Product_Stats' },
          { text: '获取直播间流量表现', link: '/zh/API_Reference/Analytics/Get_Live_Room_Traffic_Performance' },
          { text: '获取直播间用户画像', link: '/zh/API_Reference/Analytics/Get_Live_Room_User_Portraits' },
          { text: '获取直播间观看趋势', link: '/zh/API_Reference/Analytics/Get_Live_Room_View_Trends' },
          { text: '获取站外受众洞察', link: '/zh/API_Reference/Analytics/Get_Off_Site_Audience_Insights' },
          { text: '获取站外表现详情', link: '/zh/API_Reference/Analytics/Get_Off_Site_Performance_Details' },
          { text: '获取店铺直播分钟表现', link: '/zh/API_Reference/Analytics/Get_Shop_LIVE_Minute_Performance' },
          { text: '获取店铺直播表现列表', link: '/zh/API_Reference/Analytics/Get_Shop_LIVE_Performance_List' },
          { text: '获取店铺直播商品表现列表', link: '/zh/API_Reference/Analytics/Get_Shop_LIVE_Products_Performance_List' },
          { text: '获取店铺站外像素', link: '/zh/API_Reference/Analytics/Get_Shop_Off_Site_Pixels' },
          { text: '获取店铺表现', link: '/zh/API_Reference/Analytics/Get_Shop_Performance' },
          { text: '获取店铺每小时表现', link: '/zh/API_Reference/Analytics/Get_Shop_Performance_Per_Hour' },
          { text: '获取店铺商品表现详情', link: '/zh/API_Reference/Analytics/Get_Shop_Product_Performance_Detail' },
          { text: '获取店铺商品 Performance 列表', link: '/zh/API_Reference/Analytics/Get_Shop_Product_Performance_List' },
          { text: '获取店铺 SKU 表现详情', link: '/zh/API_Reference/Analytics/Get_Shop_SKU_Performance_Detail' },
          { text: '获取店铺 SKU 表现列表', link: '/zh/API_Reference/Analytics/Get_Shop_SKU_Performance_List' },
          { text: '获取店铺视频表现详情', link: '/zh/API_Reference/Analytics/Get_Shop_Video_Performance_Details' },
          { text: '获取店铺 video Performance 列表', link: '/zh/API_Reference/Analytics/Get_Shop_Video_Performance_List' },
          { text: '获取店铺 video 商品表现列表', link: '/zh/API_Reference/Analytics/Get_Shop_Video_Product_Performance_List' },
          { text: '获取店铺视频表现详情', link: '/zh/API_Reference/Analytics/Get_Shop_Videos_Performance_Details' },
          { text: '获取 SPS 指标诊断', link: '/zh/API_Reference/Analytics/Get_SPS_Metric_Diagnosis' },
          { text: '获取 SPS 指标问题详情', link: '/zh/API_Reference/Analytics/Get_SPS_Metric_Problem_Details' },
          { text: '获取 SPS 指标 Top 项目', link: '/zh/API_Reference/Analytics/Get_SPS_Metric_Top_Items' },
          { text: '获取 SPS 指标', link: '/zh/API_Reference/Analytics/Get_SPS_Metrics' },
          { text: '获取视频表现', link: '/zh/API_Reference/Analytics/Get_Video_Performances' }
          ]
        },
        {
          text: '客户服务',
          collapsed: true,
          items: [
          { text: 'Customer Service API 概述', link: '/zh/API_Reference/Customer_service/Customer_Service_API_overview' },
          { text: '创建 Conversation', link: '/zh/API_Reference/Customer_service/Create_Conversation' },
          { text: '结束 Session', link: '/zh/API_Reference/Customer_service/End_Session' },
          { text: '获取客服人员设置', link: '/zh/API_Reference/Customer_service/Get_Agent_Settings' },
          { text: '获取 Conversation', link: '/zh/API_Reference/Customer_service/Get_Conversation' },
          { text: '获取 Conversation Messages', link: '/zh/API_Reference/Customer_service/Get_Conversation_Messages' },
          { text: '获取 Conversations', link: '/zh/API_Reference/Customer_service/Get_Conversations' },
          { text: '获取客服绩效', link: '/zh/API_Reference/Customer_service/Get_Customer_Service_Performance' },
          { text: '标记买家消息为已读', link: '/zh/API_Reference/Customer_service/Mark_Buyer_Messages_as_Read' },
          { text: '消息类型', link: '/zh/API_Reference/Customer_service/Message_Types' },
          { text: '客服售后解决方案', link: '/zh/API_Reference/Customer_service/Post-sales_Solutions_for_Customer_Services' },
          { text: '搜索 Sessions', link: '/zh/API_Reference/Customer_service/Search_Sessions' },
          { text: '发送消息', link: '/zh/API_Reference/Customer_service/Send_Message' },
          { text: '更新客服人员设置', link: '/zh/API_Reference/Customer_service/Update_Agent_Settings' },
          { text: '上传买家消息图片', link: '/zh/API_Reference/Customer_service/Upload_Image_for_Buyer_Messages' }
          ]
        },
        {
          text: '客户互动',
          collapsed: true,
          items: [
          { text: 'Customer Engagement API 概览', link: '/zh/API_Reference/Customer_engagement/Customer_engagement_API_overview' },
          { text: '创建自定义 Engagement Task', link: '/zh/API_Reference/Customer_engagement/Create_Custom_Engagement_Task' },
          { text: '创建 Engagement Task', link: '/zh/API_Reference/Customer_engagement/Create_Engagement_Task' },
          { text: '获取 Engagement 功能权限', link: '/zh/API_Reference/Customer_engagement/Get_Engagement_Feature_Permissions' },
          { text: '获取 Engagement Task 绩效', link: '/zh/API_Reference/Customer_engagement/Get_Engagement_Task_Performances' },
          { text: '获取消息模板', link: '/zh/API_Reference/Customer_engagement/Get_Message_Templates' },
          { text: '发送 Engagement Message', link: '/zh/API_Reference/Customer_engagement/Send_Engagement_Message' }
          ]
        },
        {
          text: '联盟达人',
          collapsed: true,
          items: [
          { text: 'Affiliate Creator API 概览', link: '/zh/API_Reference/Affiliate_creator/Affiliate_Creator_API_overview' },
          { text: '添加 Showcase 产品', link: '/zh/API_Reference/Affiliate_creator/Add_Showcase_Products' },
          { text: '检查 Creator 样品资格', link: '/zh/API_Reference/Affiliate_creator/Check_Creator_Sample_Eligibility' },
          { text: '创建视频预审任务', link: '/zh/API_Reference/Affiliate_creator/Create_Video_Precheck_Task' },
          { text: 'Creator 搜索样品申请履约', link: '/zh/API_Reference/Affiliate_creator/Creator_Search_Sample_Application_Fulfillments' },
          { text: '生成通用分享链接', link: '/zh/API_Reference/Affiliate_creator/Generate_General_Sharing_Links' },
          { text: '批量生成发布者分享链接', link: '/zh/API_Reference/Affiliate_creator/Generate_Publisher_Sharing_Links_in_Batch' },
          { text: '获取 Creator 资料', link: '/zh/API_Reference/Affiliate_creator/Get_Creator_Profile' },
          { text: '获取 Creator 样品申请详情', link: '/zh/API_Reference/Affiliate_creator/Get_Creator_Sample_Application_Detail' },
          { text: '通过产品 ID 获取 Open Collaboration 产品列表', link: '/zh/API_Reference/Affiliate_creator/Get_Open_Collaboration_Product_List_By_Product_Ids' },
          { text: '获取店铺产品', link: '/zh/API_Reference/Affiliate_creator/Get_Shop_Products' },
          { text: '获取可购物视频预审结果', link: '/zh/API_Reference/Affiliate_creator/Get_Shoppable_Video_Precheck_Result' },
          { text: '获取可购物视频状态', link: '/zh/API_Reference/Affiliate_creator/Get_Shoppable_Video_Status' },
          { text: '获取 Showcase 产品', link: '/zh/API_Reference/Affiliate_creator/Get_Showcase_Products' },
          { text: '获取 Tokopedia 和 TikTok Shop 产品 ID 映射', link: '/zh/API_Reference/Affiliate_creator/Get_Tokopedia_and_TikTok_Shop_Product_ID_Mappings' },
          { text: '映射 Tokopedia 到 TikTok Shop 产品 ID', link: '/zh/API_Reference/Affiliate_creator/Map_Tokopedia_to_TikTok_Shop_Product_IDs' },
          { text: '将 Showcase 产品置顶', link: '/zh/API_Reference/Affiliate_creator/Move_Showcase_Products_to_the_Top' },
          { text: '发布可购物图片', link: '/zh/API_Reference/Affiliate_creator/Post_Shoppable_Photos' },
          { text: '发布可购物视频', link: '/zh/API_Reference/Affiliate_creator/Post_Shoppable_Video' },
          { text: '移除 Showcase 产品', link: '/zh/API_Reference/Affiliate_creator/Remove_Showcase_Products' },
          { text: '按 Creator 搜索 Affiliate 订单', link: '/zh/API_Reference/Affiliate_creator/Search_Affiliate_Orders_by_Creator' },
          { text: '搜索 Creator Affiliate 订单', link: '/zh/API_Reference/Affiliate_creator/Search_Creator_Affiliate_Orders' },
          { text: '搜索 Creator 样品申请', link: '/zh/API_Reference/Affiliate_creator/Search_Creator_Sample_Applications' },
          { text: '搜索 Creator Target Collaboration', link: '/zh/API_Reference/Affiliate_creator/Search_Creator_Target_Collaborations' },
          { text: '搜索 Open Collaboration 产品', link: '/zh/API_Reference/Affiliate_creator/Search_Open_Collaboration_Products' },
          { text: '上传可购物图片文件', link: '/zh/API_Reference/Affiliate_creator/Upload_Shoppable_Photo_File' },
          { text: '上传可购物视频文件', link: '/zh/API_Reference/Affiliate_creator/Upload_Shoppable_Video_File' }
          ]
        },
        {
          text: '联盟合作伙伴',
          collapsed: true,
          items: [
          { text: 'Affiliate Partner API 概览', link: '/zh/API_Reference/Affiliate_partner/Affiliate_Partner_API_overview' },
          { text: ' tmp edit', link: '/zh/API_Reference/Affiliate_partner/_tmp_edit' },
          { text: '创建 Affiliate Partner Campaign', link: '/zh/API_Reference/Affiliate_partner/Create_Affiliate_Partner_Campaign' },
          { text: '编辑 Affiliate Partner Campaign', link: '/zh/API_Reference/Affiliate_partner/Edit_Affiliate_Partner_Campaign' },
          { text: '生成 Affiliate Partner Campaign Product Link', link: '/zh/API_Reference/Affiliate_partner/Generate_Affiliate_Partner_Campaign_Product_Link' },
          { text: '批量生成 Campaign Product 推广链接', link: '/zh/API_Reference/Affiliate_partner/Generate_Campaign_Product_Promotion_Links_in_Batch' },
          { text: '获取 Affiliate Campaign Creator 产品内容统计', link: '/zh/API_Reference/Affiliate_partner/Get_Affiliate_Campaign_Creator_Product_Content_Statistics' },
          { text: '获取 Affiliate Campaign Creator 产品样品状态', link: '/zh/API_Reference/Affiliate_partner/Get_Affiliate_Campaign_Creator_Product_Sample_Status' },
          { text: '获取 Affiliate Partner Campaign 详情', link: '/zh/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_Detail' },
          { text: '获取 Affiliate Partner Campaign 列表', link: '/zh/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_List' },
          { text: '获取 Affiliate Partner Campaign Product 列表', link: '/zh/API_Reference/Affiliate_partner/Get_Affiliate_Partner_Campaign_Product_List' },
          { text: '获取 Campaign Product Performance 列表', link: '/zh/API_Reference/Affiliate_partner/Get_Campaign_Product_Performance_List' },
          { text: '获取 Campaign Product 的 Creator Performance', link: '/zh/API_Reference/Affiliate_partner/Get_Creator_Performance_for_Campaign_Product' },
          { text: '发布 Affiliate Partner Campaign', link: '/zh/API_Reference/Affiliate_partner/Publish_Affiliate_Partner_Campaign' },
          { text: '审核 Affiliate Partner Campaign Product', link: '/zh/API_Reference/Affiliate_partner/Review_Affiliate_Partner_Campaign_Product' },
          { text: '搜索 CAP Affiliate 订单', link: '/zh/API_Reference/Affiliate_partner/Search_CAP_Affiliate_Orders' },
          { text: '搜索 TAP Affiliate 订单', link: '/zh/API_Reference/Affiliate_partner/Search_TAP_Affiliate_Orders' }
          ]
        },
        {
          text: '联盟卖家',
          collapsed: true,
          items: [
          { text: 'Affiliate Seller API 概述', link: '/zh/API_Reference/Affiliate_seller/Affiliate_Seller_API_overview' },
          { text: '检查 Target Collaboration 冲突', link: '/zh/API_Reference/Affiliate_seller/Check_Target_Collaboration_Conflicts' },
          { text: '创建 Compass 离线导出任务', link: '/zh/API_Reference/Affiliate_seller/Create_Compass_Offline_Export_Task' },
          { text: '创建 Open Collaboration', link: '/zh/API_Reference/Affiliate_seller/Create_Open_Collaboration' },
          { text: '创建 Target Collaboration', link: '/zh/API_Reference/Affiliate_seller/Create_Target_Collaboration' },
          { text: '下载 Compass 任务文件', link: '/zh/API_Reference/Affiliate_seller/Download_Compass_Task_File' },
          { text: '编辑 Open Collaboration Sample 规则', link: '/zh/API_Reference/Affiliate_seller/Edit_Open_Collaboration_Sample_Rule' },
          { text: '编辑 Open Collaboration 设置', link: '/zh/API_Reference/Affiliate_seller/Edit_Open_Collaboration_Settings' },
          { text: '生成 Affiliate 产品推广链接', link: '/zh/API_Reference/Affiliate_seller/Generate_Affiliate_Product_Promotion_Link' },
          { text: '生成 Target Collaboration 链接', link: '/zh/API_Reference/Affiliate_seller/Generate_Target_Collaboration_Link' },
          { text: '获取 Compass 任务列表', link: '/zh/API_Reference/Affiliate_seller/Get_Compass_Task_List' },
          { text: '获取对话列表', link: '/zh/API_Reference/Affiliate_seller/Get_Conversation_List' },
          { text: '获取 Creator 对话消息', link: '/zh/API_Reference/Affiliate_seller/Get_Creator_Conversation_Messages' },
          { text: '获取 Marketplace Creator 高级搜索筛选条件', link: '/zh/API_Reference/Affiliate_seller/Get_Creator_Marketplace_Advanced_Search_Filters' },
          { text: '获取收件箱分类计数', link: '/zh/API_Reference/Affiliate_seller/Get_Inbox_Category_Counts' },
          { text: '获取最新未读消息', link: '/zh/API_Reference/Affiliate_seller/Get_Latest_Unread_Messages' },
          { text: '获取 Marketplace Creator 表现', link: '/zh/API_Reference/Affiliate_seller/Get_Marketplace_Creator_Performance' },
          { text: '获取 Open Collaboration Creator 内容详情', link: '/zh/API_Reference/Affiliate_seller/Get_Open_Collaboration_Creator_Content_Details' },
          { text: '获取 Open Collaboration Sample 规则', link: '/zh/API_Reference/Affiliate_seller/Get_Open_Collaboration_Sample_Rules' },
          { text: '获取 Open Collaboration 设置', link: '/zh/API_Reference/Affiliate_seller/Get_Open_Collaboration_Settings' },
          { text: '获取或创建 Creator 对话', link: '/zh/API_Reference/Affiliate_seller/Get_or_Create_Creator_Conversation' },
          { text: '获取每周 Creator 外联配额', link: '/zh/API_Reference/Affiliate_seller/Get_Weekly_Creator_Outreach_Quota' },
          { text: '获取每周 Creator 外联记录', link: '/zh/API_Reference/Affiliate_seller/Get_Weekly_Creator_Outreach_Records' },
          { text: '标记对话为已读', link: '/zh/API_Reference/Affiliate_seller/Mark_Conversations_as_Read' },
          { text: '查询 Target Collaboration 中的 Creator 推广详情', link: '/zh/API_Reference/Affiliate_seller/Query_Creator_Promotion_Details_in_Target_Collaboration' },
          { text: '查询 Target Collaboration 详情', link: '/zh/API_Reference/Affiliate_seller/Query_Target_Collaboration_Detail' },
          { text: '从 Open Collaboration 产品中移除 Creator', link: '/zh/API_Reference/Affiliate_seller/Remove_Creator_From_Open_Collaboration_Product' },
          { text: '移除 Open Collaboration', link: '/zh/API_Reference/Affiliate_seller/Remove_Open_Collaboration' },
          { text: '移除 Target Collaboration', link: '/zh/API_Reference/Affiliate_seller/Remove_Target_Collaboration' },
          { text: '解决 Target Collaboration 冲突', link: '/zh/API_Reference/Affiliate_seller/Resolve_Target_Collaboration_Conflicts' },
          { text: '审核 Sample 申请', link: '/zh/API_Reference/Affiliate_seller/Review_a_Sample_Application' },
          { text: '在 Creator Marketplace 中搜索 Creator', link: '/zh/API_Reference/Affiliate_seller/Search_Creators_in_Creator_Marketplace' },
          { text: '搜索 Open Collaboration', link: '/zh/API_Reference/Affiliate_seller/Search_Open_Collaborations' },
          { text: '搜索 Sample 申请履约', link: '/zh/API_Reference/Affiliate_seller/Search_Sample_Application_Fulfillments' },
          { text: '搜索 Sample 申请', link: '/zh/API_Reference/Affiliate_seller/Search_Sample_Applications' },
          { text: '搜索卖家 Affiliate 订单', link: '/zh/API_Reference/Affiliate_seller/Search_Seller_Affiliate_Orders' },
          { text: '搜索 Target Collaboration', link: '/zh/API_Reference/Affiliate_seller/Search_Target_Collaborations' },
          { text: '卖家获取 Sample 请求 Deeplink', link: '/zh/API_Reference/Affiliate_seller/Seller_Get_Sample_Request_Deeplink' },
          { text: '卖家搜索 Open Collaboration 产品', link: '/zh/API_Reference/Affiliate_seller/Seller_Search_Open_Collaboration_Products' },
          { text: '发送 IM 消息', link: '/zh/API_Reference/Affiliate_seller/Send_IM_Message' },
          { text: '更新对话状态', link: '/zh/API_Reference/Affiliate_seller/Update_Conversation_Status' },
          { text: '更新 Target Collaboration', link: '/zh/API_Reference/Affiliate_seller/Update_Target_Collaboration' },
          { text: '上传消息图片', link: '/zh/API_Reference/Affiliate_seller/Upload_Message_Image' },
          { text: '上传消息图片 V2', link: '/zh/API_Reference/Affiliate_seller/Upload_Message_Image_V2' }
          ]
        },
        {
          text: '供应链',
          collapsed: true,
          items: [
          { text: '上传文件初始化', link: '/zh/API_Reference/Supply_chain/Upload_File_Init' }
          ]
        }
        ]
      },
      {
        text: 'Webhooks',
        collapsed: true,
        items: [
          {
            text: '订单',
                collapsed: true,
                items: [
                  { text: '(1) 订单状态变更', link: '/zh/Webhooks/Order/(1)_Order_status_change' },
                  { text: '(11) 取消状态变更', link: '/zh/Webhooks/Order/(11)_Cancellation_status_change' }
                ]
              },
              {
                text: '商品',
                collapsed: true,
                items: [
                  { text: '(5) 商品状态变更', link: '/zh/Webhooks/Product/(5)_Product_status_change' },
                  { text: '(15) 商品信息变更', link: '/zh/Webhooks/Product/(15)_Product_information_change' },
                  { text: '(16) 商品创建', link: '/zh/Webhooks/Product/(16)_Product_creation' },
                  { text: '(27) 库存状态变更', link: '/zh/Webhooks/Product/(27)_Inventory_status_change' }
                ]
              },
              {
                text: '履约',
                collapsed: true,
                items: [
                  { text: '(36) 发票状态变更', link: '/zh/Webhooks/Fulfillment/(36)_Invoice_status_change' },
                  { text: '(21) FBT 入库订单状态变更', link: '/zh/Webhooks/Fulfilled_by_TikTok/(21)_Inbound_FBT_order_status_change' },
                  { text: '(24) FBT 库存更新', link: '/zh/Webhooks/Fulfilled_by_TikTok/(24)_FBT_inventory_update' }
                ]
              },
              {
                text: '物流',
                collapsed: true,
                items: [
                  { text: '(3) 收件地址更新', link: '/zh/Webhooks/Logistics/(3)_Recipient_address_update' },
                  { text: '(4) 包裹更新', link: '/zh/Webhooks/Logistics/(4)_Package_update' }
                ]
              },
              {
                text: '退货和退款',
                collapsed: true,
                items: [
                  { text: '(12) 退货状态变更', link: '/zh/Webhooks/Return_and_Refund/(12)_Return_status_change' },
                  { text: '(67) 退款成功', link: '/zh/Webhooks/Return_and_Refund/(67)_Refund_Success' }
                ]
              },
              {
                text: '卖家',
                collapsed: true,
                items: [
                  { text: '(6) 卖家取消授权', link: '/zh/Webhooks/Seller/(6)_Seller_deauthorization' },
                  { text: '(7) 授权即将过期', link: '/zh/Webhooks/Seller/(7)_Upcoming_authorization_expiration' }
                ]
              }
            ]
          }
        ],
        socialLinks: [
          { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
        ],
        search: {
          provider: 'local'
        },
        footer: {
          message: 'TikTok Shop 合作伙伴中心文档',
          copyright: '下载自 partner.tiktokshop.com'
        }
      }
    }
  }
})
