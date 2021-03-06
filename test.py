import unittest

from API import GetSearchOption, SearchInDataBaseBYDate, SearchInDataBaseBYAcident, GetID, GetDate, GetAcident, CheckInPuts


obj1 = {"id": 1, "name": "John", "age": 20, "address": "Highway 37", "Phone": "01304050", "height": 170,
        "weight": 60, "MedicalHistory": "diabetic , Hypertension", "Date": "2020-12-25", "Doctor_Name": "magdy", "Diagnose": "Immune Deficiency Syndrome", "Accident": "Car Accident"}
obj2 = {"id": 2, "name": "ahmed", "age": 30, "address": "imbaba", "Phone": "01305603", "height": 160, "weight": 80,
        "MedicalHistory": "diabetic", "Date": "2011-11-25", "Doctor_Name": "Wassif", "Diagnose": "cancer", "Accident": "Bus Accident"}
obj3 = {"id": 1, "name": "John", "age": 20, "address": "Highway 37", "Phone": "01304050", "height": 170, "weight": 60,
        "MedicalHistory": "diabetic , Hypertension", "Date": "2010-11-25", "Doctor_Name": "Hanan", "Diagnose": "Preumonin", "Accident": "Train Accident"}

obj4 = {"id": 1, "date": "2010-11-25",
        "Accident": "Car Accident", "searchoption": "accidenttype"}
obj5 = {"id": "", "date": "2010-11-25", "Accident": "Car Accident"}


class UnitTest(unittest.TestCase):
    def test1_SearchInDataBaseBYDate(self):
        result = SearchInDataBaseBYDate(1, "2020-12-25")
        self.assertEqual(result[0], obj1)

    def test2_SearchInDataBaseBYDate(self):
        result = SearchInDataBaseBYDate(1, "2010-11-25")
        self.assertEqual(result[0], obj3)

    def test1_SearchInDataBaseBYAcident(self):
        result = SearchInDataBaseBYAcident(1, "Car Accident")
        self.assertEqual(result[0], obj1)

    def test2_SearchInDataBaseBYAcident(self):
        result = SearchInDataBaseBYAcident(1, "Train Accident")
        self.assertEqual(result[0], obj3)

    def test1_GetID(self):
        result = GetID(obj4)
        self.assertEqual(result, obj4["id"])

    def test2_GetID(self):
        result = GetID(obj5)
        self.assertEqual(result, None)

    def test1_GetDate(self):
        result = GetDate(obj4)
        self.assertEqual(result, obj4["date"])

    def test1_GetAcident(self):
        result = GetAcident(obj4)
        self.assertEqual(result, obj4["Accident"])

    def test1_CheckInPuts(self):
        result = CheckInPuts(None, "", "")
        Expected = "User Must Enter ID"
        self.assertEqual(result, Expected)

    def test2_CheckInPuts(self):
        result = CheckInPuts(1, "", "")
        Expected = "You Must Enter Date or Accident"
        self.assertEqual(result, Expected)

    def test3_CheckInPuts(self):
        result = CheckInPuts(1, "2020-12-25", "")
        Expected = "checked"
        self.assertEqual(result, Expected)

    def test4_CheckInPuts(self):
        result = CheckInPuts(1, "", "Car Accident")
        Expected = "checked"
        self.assertEqual(result, Expected)

    def test1_GetSearchOption(self):
        result = GetSearchOption(obj4)
        Expected = "accidenttype"
        self.assertEqual(result, Expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
