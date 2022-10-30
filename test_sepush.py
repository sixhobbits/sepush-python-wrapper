import sepush
import time

def test_free_calls():
    print(sepush.get_api_allowance())
    time.sleep(0.5)
    print(sepush.get_area("eskdo-8-kentononsea1ndlambeeasterncape", test="current"))
    time.sleep(0.5)
    print(sepush.get_area("eskdo-8-kentononsea1ndlambeeasterncape", test="future"))

if __name__ == '__main__':
    test_free_calls()


