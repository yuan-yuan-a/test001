import allure

class Test_001:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("第一步")
    def test_01(self):
        print("\n---test01")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        print("\n---test02")
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        print("\n---test03")

    @allure.severity(allure.severity_level.MINOR)
    def test_04(self):
        print("\n---test04")

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_05(self):
        print("\n---test05")