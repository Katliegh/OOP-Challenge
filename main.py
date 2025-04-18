from pet import Pet

def main():
    sipho = Pet("Sipho")
    sipho.get_status()
    sipho.eat()
    sipho.get_status()
    sipho.train("Sit")
    sipho.train("Stay")
    sipho.show_tricks()
    sipho.play()
    sipho.get_status()

if __name__ == "__main__":
    main()