while True:
    models = ["iPhone 8", "iPhone XR", "iPhone 11", "iPhone 12", "iPhone 13 mini", "Other"]

    def phone_algorithm():
        # Ask user to select a model
        print("Please select a model:")
        print("Just type the number")
        print("More Phones Coming Soon!")
        for i, model in enumerate(models):
            print(f"{i + 1}. {model}")
        selected_model = int(input()) - 1

        # Set default values for selected model
        if models[selected_model] == "iPhone 8":
            displaytype = 1
            displaysize = 4.7
            displayres = 750 * 1334
            displaydensity = 326
            storage = int(input("How much storage? (64, 256) "))
            processorspeed = 2.4
            processorarch = 64
            processorquantity = 6
            graphicmemory = 2
            graphicchipquantity = 3
            camera = 12
            bluetooth = 5
            batterycapacity = 1821
            batterylife = 14
            # Define price using the storage
            if storage == 64:
                price = int(699)
            elif storage == 256:
                price = int(849)
        elif models[selected_model] == "iPhone XR":
            displaytype = 1
            displaysize = 6.1
            displayres = 828 * 1792
            displaydensity = 326
            storage = int(input("How much storage? (64, 128, 256) "))
            processorspeed = 2.5
            processorarch = 64
            processorquantity = 6
            graphicmemory = 3
            graphicchipquantity = 2
            camera = 12
            bluetooth = 5
            batterycapacity = 2942
            batterylife = 25
            # Define price using the storage
            if storage == 64:
                price = int(749)
            elif storage == 128:
                price = int(799)
            elif storage == 256:
                price = int(899)
        elif models[selected_model] == "iPhone 11":
            displaytype = 1
            displaysize = 6.1
            displayres = 828 * 1792
            displaydensity = 326
            storage = 64
            processorspeed = 2.5
            processorarch = 64
            processorquantity = 6
            graphicmemory = 4
            graphicchipquantity = 2
            camera = 12
            bluetooth = 5
            batterycapacity = 3110
            batterylife = 25
            price = 699
        elif models[selected_model] == "iPhone 12":
            displaytype = 1
            displaysize = 6.1
            displayres = 828 * 1792
            displaydensity = 326
            storage = 64
            processorspeed = 2.5
            processorarch = 64
            processorquantity = 6
            graphicmemory = 4
            graphicchipquantity = 2
            camera = 12
            bluetooth = 5
            batterycapacity = 3110
            batterylife = 25
            price = 699
        elif models[selected_model] == "iPhone 13 mini":
            displaytype = 2
            displaysize = 5.4
            displayres = 1080 * 2340
            displaydensity = 476
            storage = int(input("How much storage? (128, 256, 512) "))
            processorspeed = 3.2
            processorarch = 64
            processorquantity = 6
            graphicmemory = 4
            graphicchipquantity = 4
            camera = 12
            bluetooth = 5
            batterycapacity = 2406
            batterylife = 17
            # Define price using the storage
            if storage == 128:
                price = int(729)
            elif storage == 256:
                price = int(829)
            elif storage == 512:
                price = int(1029)
        elif models[selected_model] == "Other":
            # Prompt user to enter values for each factor
            displaytype = float(input("Enter the display type (0 for LCD, 1 for LCD-Retina, 2 for OLED): "))
            displaysize = float(input("Enter the display size in inches: "))
            width, height = map(float, input("Enter the display resolution in pixels (width x height): ").split("*"))
            displayres = width * height
            displaydensity = float(input("Enter the display density in pixels per inch: "))
            storage = float(input("Enter the storage capacity in GB: "))
            processorspeed = float(input("Enter the processor speed in GHz: "))
            processorarch = float(input("Enter the processor architecture: "))
            processorquantity = float(input("Enter the number of processors: "))
            graphicmemory = float(input("Enter the graphic memory in GB: "))
            graphicchipquantity = float(input("Enter the number of graphic chips: "))
            camera = float(input("Enter the rear camera resolution in MP: "))
            bluetooth = float(input("Enter the bluetooth version: "))
            batterycapacity = float(input("Enter the battery capacity in mAh: "))
            batterylife = float(input("Enter the battery life in hours: "))
            price = float(input("Enter the price in USD: "))

        # Assign weights to different factors
        displaytype_weight = 0.05
        displaysize_weight = 0.05
        displayres_weight = 0.05
        displaydensity_weight = 0.1
        storage_weight = 0.1
        processorspeed_weight = 0.1
        processorarch_weight = 0.05
        processorquantity_weight = 0.05
        graphicmemory_weight = 0.05
        graphicchipquantity_weight = 0.05
        camera_weight = 0.1
        bluetooth_weight = 0.05
        batterycapacity_weight = 0.1
        batterylife_weight = 0.1
        price_weight = 0.5

        # Calculate normalized values for each factor
        normalized_displaytype = displaytype / 2
        normalized_displaysize = displaysize / 6
        normalized_displayres = displayres / (2560 * 1440)
        normalized_displaydensity = displaydensity / 800
        normalized_storage = storage / 512
        normalized_processorspeed = processorspeed / 2.5
        normalized_processorarch = processorarch / 64
        normalized_processorquantity = processorquantity / 8
        normalized_graphicmemory = graphicmemory / 8
        normalized_graphicchipquantity = graphicchipquantity / 8
        normalized_camera = camera / 64
        normalized_bluetooth = bluetooth / 5
        normalized_batterycapacity = batterycapacity / 6000
        normalized_batterylife = batterylife / 40
        normalized_price = price / 1500

        # Calculate the score using the weights and normalized values
        score = displaytype_weight * normalized_displaytype + displaysize_weight * normalized_displaysize + displayres_weight * normalized_displayres + displaydensity_weight * normalized_displaydensity + storage_weight * normalized_storage + processorspeed_weight * normalized_processorspeed + processorarch_weight * normalized_processorarch + processorquantity_weight * normalized_processorquantity + graphicmemory_weight * normalized_graphicmemory + graphicchipquantity_weight * normalized_graphicchipquantity + camera_weight * normalized_camera + bluetooth_weight * normalized_bluetooth + batterycapacity_weight * normalized_batterycapacity + batterylife_weight * normalized_batterylife + price_weight * normalized_price

        return score


    score = phone_algorithm()
    print("Score: ", score)
