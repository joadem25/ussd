options = {"1.":"Data Plans", "2.":"Social Bundles", "3.":"Balance Check", "4.":"Roaming/Int'l"}

option_data_plans = {"1.":"Daily", "2.":"Weekly", "3.":"Monthly"}
option_social_bundles = {"1.":"Whatsapp", "2.":"Facebook", "3.":"Instagram"}
option_roaming = {"1.":"TravelPass Plans", "2.":"Data Hybrid", "3.":"Inflight Roaming Data"}

data_plans_daily = {"1.":"N50 for 40MB", "2.":"N100 for 100MB", "3.":"N100 for 350MB(IG/TIKTOK/Youtube)"}
data_plans_weekly = {"1.":"N200 for 1GB(IG/TikTok/Youtube ONLY)", "2.":"N300 for 350MB", "3.":"N500 for 1.5GB"}
data_plans_monthly = {"1.":"N1,000 for 1.5GB", "2.":"N1,200 for 2GB", "3.":"N1,500 for 3GB"}

social_bundles_whatsapp = {"1.":"Daily @ N25 for 25MB", "2.":"Weekly @ N50 for 50MB", "3.":"Monthly @ N150 for 150MB"}
social_bundels_facebook = {"1.":"Daily @ N25 for 25MB", "2.":"Weekly @ N50 for 50MB", "3.":"Monthly @ N150 for 150MB"}
social_bundels_instagram = {"1.":"N100 for 250MB/1 day", "2.":"N100 for 250MB", "3.":"N200 for 1GB"}

roaming_travelPass = {"1.":"7days TravelPass @N5000", "2.":"14days TravelPass @N10000", "3.":"7days TravelPass (Data) @N5000"}
roaming_data_hybrid = {"1.":"Eligible Bundles", "2.":"Eligible Destinations"}
roaming_inflight_roaming_data = {"1.":"50MB @N2,000", "2.":"View Airlines"}
code = input("Please enter code: ")



while code != "*131#":
    code = input("Invalid entry, please try again: ")
while code == "*131#":
    for x,y in options.items():
        print(x,y)
    user_option = input("Select an option: ")
    #Option daily
    while user_option == "1":
        for x,y in option_data_plans.items():
            print(x,y)
        print("0. back")
        user_option_data_plans = input("Select an option: ")
        if user_option_data_plans == "1":
            for x,y in data_plans_daily.items():
                print(x,y)
            print("0. back")
            user_option_data_plans_daily = input("Select daily plan: ")
            if user_option_data_plans_daily == "0":
                user_option_data_plans == "1"
            else:
                print("Sorry, transaction not yet available")
                break
        elif user_option_data_plans == "2":
            for x,y in data_plans_weekly.items():
                print(x,y)
            print("0. back")
            user_option_data_plans_weekly = input("Select weekly plan: ")
            if user_option_data_plans_weekly == "0":
                user_option_data_plans == "2"
            else:
                print("Sorry, transaction not yet available")
                break  
        elif user_option_data_plans == "3":
            for x, y in data_plans_monthly.items():
                print(x,y)
            print("0. back")
            user_option_data_plans_monthly = input("Select monthly: ")
            if user_option_data_plans_monthly == "0":
                user_option_data_plans == "3"
            else:
                print("Sorry, transaction not yet available")
                break
        elif user_option_data_plans == "0":
            break
        else:
            print("Invalid input, try again!") 
    #Option Social bundle
    while user_option == "2":
        for x,y in option_social_bundles.items():
            print(x,y)
        user_option_social_bundle = input("Select an option: ")
        while user_option_social_bundle == "1":
            for x,y in social_bundles_whatsapp.items():
                print(x,y)
            user_option_social_bundle = input("Select: ")
        while user_option_social_bundle == "2":
            for x,y in social_bundels_facebook.items():
                print(x,y)
            user_option_social_bundle = input("Select: ")
        while user_option_social_bundle == "3":
            for x,y in social_bundels_instagram.items():
                print(x,y)
            user_option_social_bundle = input("Select: ")
    while user_option == "4":
        for x,y in option_roaming.items():
            print(x,y)
        user_option = input("Select an option: ")


# while code != "*131#":
#     code = input("Invalid entry, please try again: ")
# while code == "*131#":
#     for x,y in options.items():
#         print(x,y)
#     user_option = input("Select an option: ")
    
#     while user_option == d[0]:
#         # print(a)
#         # print(b)
#         # print(c)
#         for x,y in option_data_plans.items():
#             print(x,y)
#         user_option = input("Select an option: ")
#     while user_option == e[0]:
#         for x,y in option_social_bundles.items():
#             print(x,y)
#         user_option = input("Select an option: ")
#     while user_option == f[0]:
#         for x,y in option_roaming.items():
#             print(x,y)
#         user_option = input("Select an option: ")
    
    
    # while user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4":
    #     print("Well-done")


    # while user_option != "1" or user_option != "2" or user_option != "3" or user_option != "4":
    #     user_option = input("Invalid option, please try again: ")