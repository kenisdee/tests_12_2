import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
        return False

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Используем срез для безопасного удаления элементов
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, results in cls.all_results.items():
            print(f"{test_name}: {results}")

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results['Забег Усэйн - Ник'] = {place: runner.name for place, runner in results.items()}

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Забег Андрей - Ник'] = {place: runner.name for place, runner in results.items()}

    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.all_results['Забег Усэйн - Андрей - Ник'] = {place: runner.name for place, runner in results.items()}

    def test_race_equal_speed(self):
        runner1 = Runner("Runner1", 5)
        runner2 = Runner("Runner2", 5)
        tournament = Tournament(50, runner1, runner2)
        results = tournament.start()
        self.all_results['Забег с участниками одинаковой скорости'] = {place: runner.name for place, runner in results.items()}

    def test_race_long_distance(self):
        runner1 = Runner("Runner1", 1)
        runner2 = Runner("Runner2", 2)
        tournament = Tournament(100, runner1, runner2)
        results = tournament.start()
        self.all_results['Забег на длинную дистанцию'] = {place: runner.name for place, runner in results.items()}

if __name__ == "__main__":
    unittest.main()