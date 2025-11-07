import math

def calculate_travel_package():
    print("— Trivago-style Travel Package Calculator —")
    
    # Step 1: Get number of travelers
    num_travelers = int(input("Enter number of travelers: "))
    
    # Step 2: Destination selection
    print("Destinations: 1=Goa (₹20,000), 2=Kerala (₹22,000), 3=Manali (₹18,000), 4=Jaipur (₹15,000)")
    dest_choice = int(input("Enter destination choice (1-4): "))
    
    # Destination data without dictionary
    if dest_choice == 1:
        dest_name = "Goa"
        base_price = 20000
    elif dest_choice == 2:
        dest_name = "Kerala"
        base_price = 22000
    elif dest_choice == 3:
        dest_name = "Manali"
        base_price = 18000
    elif dest_choice == 4:
        dest_name = "Jaipur"
        base_price = 15000
    else:
        dest_name = "Kerala"  # default
        base_price = 22000
    
    # Step 3: Travel mode selection
    print("Travel Modes: 1=Flight (₹8,000), 2=Train AC (₹3,000), 3=Train Non-AC (₹1,500)")
    travel_choice = int(input("Enter travel choice (1-3): "))
    
    # Travel mode data without dictionary
    if travel_choice == 1:
        travel_mode = "Flight"
        travel_cost = 8000
    elif travel_choice == 2:
        travel_mode = "Train AC"
        travel_cost = 3000
    elif travel_choice == 3:
        travel_mode = "Train Non-AC"
        travel_cost = 1500
    else:
        travel_mode = "Flight"  # default
        travel_cost = 8000
    
    # Step 4: Hotel selection
    print("Hotels: 1=5-Star, 2=3-Star, 3=Budget")
    hotel_choice = int(input("Enter hotel choice (1-3): "))
    
    # Hotel data without dictionary
    if hotel_choice == 1:
        hotel_type = "5-Star"
        hotel_rate = 5000
    elif hotel_choice == 2:
        hotel_type = "3-Star"
        hotel_rate = 3000
    elif hotel_choice == 3:
        hotel_type = "Budget"
        hotel_rate = 1500
    else:
        hotel_type = "Budget"  # default
        hotel_rate = 1500
    
    nights = int(input("Enter number of nights: "))
    hotel_cost = hotel_rate * nights
    
    # Step 5: Food plan selection
    print("Food Plan: 1=Full Meals (₹4,000), 2=Breakfast Only (₹2,000), 3=None (₹0)")
    food_choice = int(input("Enter food plan (1-3): "))
    
    # Food plan data without dictionary
    if food_choice == 1:
        food_plan = "Full Meals"
        food_cost = 4000
    elif food_choice == 2:
        food_plan = "Breakfast Only"
        food_cost = 2000
    elif food_choice == 3:
        food_plan = "None"
        food_cost = 0
    else:
        food_plan = "Full Meals"  # default
        food_cost = 4000
    
    # Step 6: Sightseeing add-on
    sightseeing_choice = input("Sightseeing Add-on? (Y/N): ").upper()
    if sightseeing_choice == 'Y':
        sightseeing_cost = 3500
        sightseeing_included = "Included"
    else:
        sightseeing_cost = 0
        sightseeing_included = "Not Included"
    
    # Step 7: Travel month for seasonal surcharge
    travel_month = input("Travel Month (Jan-Dec): ").capitalize()
    
    # Calculate seasonal surcharge (30% on Base + Travel cost for Dec or May)
    seasonal_surcharge = 0.0
    if travel_month == "Dec" or travel_month == "May":
        seasonal_surcharge = (base_price + travel_cost) * 0.3
    
    # Step 8: Calculate total before discount
    total_before_discount = base_price + travel_cost + hotel_cost + food_cost + sightseeing_cost + seasonal_surcharge
    
    # Step 9: Apply discount
    discount = 0.0
    if total_before_discount >= 350000:
        discount = total_before_discount * 0.01
    elif total_before_discount >= 340000:
        discount = total_before_discount * 0.01
    
    # Step 10: Calculate GST
    total_after_discount = total_before_discount - discount
    gst = total_after_discount * 0.18
    
    # Step 11: Calculate final price per person
    final_price_per_person = total_after_discount + gst
    
    # Display results
    print("\n— Full Package Details —")
    print(f"Destination: {dest_name}")
    print(f"Travel Mode: {travel_mode}")
    print(f"Hotel Type: {hotel_type} for {nights} nights")
    print(f"Food Plan: {food_plan}")
    print(f"Sightseeing: {sightseeing_included}")
    print(f"Travel Month: {travel_month}")
    
    print("\n— Cost Breakdown (Per Person) —")
    print(f"Base Price = {base_price}")
    print(f"Travel Cost = {travel_cost}")
    print(f"Hotel Cost = {hotel_cost}")
    print(f"Food Cost = {food_cost}")
    print(f"Sightseeing Cost = {sightseeing_cost}")
    print(f"Seasonal Surcharge = {seasonal_surcharge}")
    print(f"Total Before Discount = {total_before_discount}")
    print(f"Discount = {discount}")
    print(f"GST (18%) = {gst}")
    print(f"Final Package Price Per Person = {final_price_per_person}")
    
    # Calculate total for all travelers
    total_package_price = final_price_per_person * num_travelers
    print(f"\nTotal Package Price for {num_travelers} Travellers = {total_package_price}")

# Run the program
if __name__ == "__main__":
    calculate_travel_package()
