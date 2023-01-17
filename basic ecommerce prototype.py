#basic ecommerce

products = ["iphone","samsung","one plus","oppo","realme","sony"]
while True:
    user = input("view cart/add to cart/remove from cart/update cart/extit from transiction? :")
    if user == "exit":
        print("Sucessfully exit this Page")

    elif user == "view":
        print("Products",products)

    elif user == "add":
        products.append(input("Add  Products to Cart: "))
        print("This is Your Cart",products)

    elif user == "remove":
        products.remove(input("Which product want to remove from cart?: "))
        print("You Sucessfully removed",products)

    elif user == "update":
        w_p = input("Enter wrong products: ")
        r_p = input("Enter right products: ")
        if w_p in products:
            w_p_index = products.index(w_p)
            products[w_p_index] = r_p
            print("Updated cart sucessfully",products)

        else:
            print("Product dosen't match")
    else:
        print("You entired invalid command. Try again")



