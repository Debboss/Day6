test_h = int(input("Height of wall: "));
test_w = int(input("Width of wall: "));

coverage = 5;

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    round_number = round(number_of_cans)
    print(f"The cans you need to paint your wall is: {round_number}")
    return number_of_cans

paint_calc(height=test_h, width=test_w, cover=coverage)