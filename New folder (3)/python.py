def animal_sounds(animal):
    sounds = {
        'dog': 'Woof! Woof!',
        'cat': 'Meow!',
        'cow': 'Moo!',
        'duck': 'Quack!',
        'elephant': 'Trumpet!',
        'lion': 'Roar!',
        'horse': 'Neigh!',
        'pig': 'Oink!',
        'sheep': 'Baa!',
        # Add more animals and their sounds as needed
    }

    return sounds.get(animal.lower(), "Unknown animal!")

def main():
    print("Welcome to the Animal Sounds program!")
    print("Available animals: dog, cat, cow, duck, elephant, lion, horse, pig, sheep")

    while True:
        animal = input("\nEnter the name of an animal (or 'exit' to quit): ")
        
        if animal.lower() == 'exit':
            break

        sound = animal_sounds(animal)
        print(f"The sound of {animal} is {sound}")

if __name__ == "__main__":
    main()
