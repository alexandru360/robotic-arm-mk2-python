from src.hysrf05_distance import HYSRF05

if __name__ == "__main__":
    hysrf05 = HYSRF05(23, 24)
    try:
        while True:
            distance = hysrf05.measure_distance()
            print(f"Distance: {distance:.2f} cm")

    except KeyboardInterrupt:
        del hysrf05
        pass
