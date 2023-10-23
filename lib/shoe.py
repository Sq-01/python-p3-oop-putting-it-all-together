#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

# Run the tests
if __name__ == "__main__":
    stan_smith = Shoe("Adidas", 9)
    assert stan_smith.brand == "Adidas"
    assert stan_smith.size == 9

    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.size = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "size must be an integer\n"

    captured_out = io.StringIO()
    sys.stdout = captured_out
    stan_smith.cobble()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Your shoe is as good as new!\n"

    stan_smith = Shoe("Adidas", 9)
    stan_smith.cobble()
    assert stan_smith.condition == "New"