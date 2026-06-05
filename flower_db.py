class flower:
    def __init__ (self, name, color, height, climate_required_to_bloom):
        self.name = name
        self.color = color
        self.height = height
        self.climate = climate_required_to_bloom

    def __str__ (self):
        return (f"Name of the flower: {self.name} \nColor of the Flower: {self.color} \nHeigt of the Flower: {self.height} \nBlooming Season: {self.climate}")
    

flower1 = flower("Rose" , "Red" , "1-2 M" ,"Late Winter to early Summer")
flower2 = flower("Hibiscus" , "Yellow" , "1.2-3 M" ,"Late Winter to entire Autum")
flower3 = flower("Lavender" , "Purple" , "30-90 CM" ,"Late Winter to entire Summer")

flowers = (flower1, flower2, flower3)
while True:
    search = input("Enter number from 1 to 3: ")
    try:
        search = int(search)
        if search == 1:
            print(flower1)
        elif search == 2:
            print(flower2)
        elif search == 3:
            print(flower3)
            break
        else: 
            print("Invalid Input")
            continue
    except ValueError:
        continue


        
