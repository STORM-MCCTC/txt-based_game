def clothing():
    pant = ["none","shorts", "Sweatpants", "Ripped Jeans", "Cargo Pants", "Dress Slacks", "Tailored Trousers", "Yoga Leggings"]
    Shirt = ["none", "T-Shirt", "Graphic T-Shirt", "Dress Shirt", "wife_beater"]
    Outerwear = ["none","Leather Jacket", "Hoodie", "Trench Coat", "Blazer"]
    Footwear_under = ["none","basic Socks", "long socks", "stockings"]
    Footwear = ["none", "boots", "sneakers"] # if not wearing Footware your feet will be damaged over time 
    underware_upper = ["none", "basic Bra"]
    underware_lower =["none", "male Underware", "female Underware"]
    Accessories_head = ["none", "Snapback", "Baseball Cap", "Beanie", "Bucket Hat", "Top Hat", "Fedora", "Newsboy Cap", "Balaclava", "Headband"]
    Accessories_face = ["none", "Sunglasses", "Glasses" "Round Glasses"]
    Accessories_face_mask = ["none", "Basic FaceMask"] # hides your idendety stopping reputation lost and gain
    Accessories_back = ["none", "Backpack", "Gym Bag"] # bag items give more Inventory space
    Accessories_neck = ["none ", "chocker"]
    Accessories_hands = ["none ", "Cufflinks", "Watch"] # watch lets you see the in-game time
    Dress = ["none", "Sundress", "Evening Gown"]
    coverall = ["none", "Denim Overalls","Track Suit"]

    return pant, Shirt, Outerwear, Footwear_under, Footwear, underware_upper, underware_lower, Accessories_head, Accessories_face, Accessories_face_mask, Accessories_back, Accessories_neck, Accessories_hands, Dress, coverall

# stress increses faster if pants or shirts are set to "none"
# in normal game play underware will never be set to "none"
# clothing can get dirty, wet, bloody, etc. and will need to be washed