from tests.api_test.board_test import BoardTest
from tests.api_test.card_test import CardTest
from infra.api_wrapper import APIWrapper


# run last simulation
def main():
    test_cases = [BoardTest, CardTest]
    my_api = APIWrapper()
    my_api.run_tests(test_cases)


if __name__ == "__main__":
    main()
