from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("My name", 30)

    def test_attributes_are_set(self):
        self.assertEqual("My name", self.paint_factory.name)
        self.assertEqual(30, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)

    def test_add_ingredient_not_valid_raises_exception(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("purple", 5)
        expected = "Ingredient of type purple not allowed in PaintFactory"
        self.assertEqual(expected, str(ex.exception))

    def test_try_to_add_ingredient__not_enough_capacity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("blue", 40)
        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ex.exception))

    def test_add_ingredient__ingredient_type_not_in_ingredients_dict(self):
        self.paint_factory.add_ingredient("blue", 10)
        expected = {"blue": 10}
        actual_result = self.paint_factory.ingredients
        self.assertDictEqual(expected, actual_result)

    def test_add_ingredient__ingredient_type_already_in_ingredients_dict(self):
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient("blue", 12)
        self.paint_factory.add_ingredient("blue", 5)
        expected = {"blue": 17}
        actual_result = self.paint_factory.ingredients
        self.assertDictEqual(expected, actual_result)

    def test_try_to_remove_ingredient__type_not_in_ingredients_dict_raises(self):
        self.paint_factory.add_ingredient("yellow", 5)
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("green", 8)
        expected = "'No such product in the factory'"
        self.assertEqual(expected, str(ex.exception))

    def test_try_to_remove_ingredient__quantity_gets_less_than_zero_raises(self):
        self.paint_factory.add_ingredient("red", 15)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("red", 17)
        expected = "Ingredient quantity cannot be less than zero"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_ingredient_from_ingredients(self):
        self.paint_factory.add_ingredient("red", 15)
        self.paint_factory.remove_ingredient("red", 10)
        expected = {"red": 5}
        actual_result = self.paint_factory.ingredients
        self.assertDictEqual(expected, actual_result)
        self.assertNotIn("blue", self.paint_factory.ingredients.keys())

    def test_paint_factory_products__expect_ingredients(self):
        self.paint_factory.add_ingredient("blue", 30)
        expected_result = self.paint_factory.products
        self.assertDictEqual(expected_result, self.paint_factory.ingredients)

#
# if __name__ == '__main__':
#     main()

# import unittest
#
# from project.factory.paint_factory import PaintFactory
#
#
# class PaintFactoryTest(unittest.TestCase):
#     def setUp(self):
#         self.factory = PaintFactory("Factory", 100)
#
#     def test_paint_factory_add_ingredient__not_in_valid_ingredients__expect_exception(self):
#         with self.assertRaises(TypeError) as context:
#             self.factory.add_ingredient("black", 10)
#         expected_result = "Ingredient of type black not allowed in PaintFactory"
#         self.assertEqual(expected_result, str(context.exception))

    # def test_paint_factory_add_ingredient__not_enough_capacity__expect_exception(self):
    #     with self.assertRaises(ValueError) as context:
    #         self.factory.add_ingredient("blue", 110)
    #     expected_result = "Not enough space in factory"
    #     self.assertEqual(expected_result, str(context.exception))

    # def test_paint_factory_add_ingredient__not_in_ingredients_keys__create_ingredient_in_ingredients(self):
    #     self.factory.add_ingredient("blue", 30)
    #     expected_result = {'blue': 30}
    #     actual_result = self.factory.ingredients
    #     self.assertEqual(expected_result, actual_result)

    # def test_paint_factory_add_ingredient__add_ingredient_in_ingredients(self):
    #     self.assertDictEqual({}, self.factory.ingredients)
    #     self.factory.add_ingredient("blue", 30)
    #     self.factory.add_ingredient("blue", 30)
    #     expected_result = {'blue': 60}
    #     actual_result = self.factory.ingredients
    #     self.assertEqual(expected_result, actual_result)

    # def test_paint_factory_remove_ingredient__not_in_ingredients_keys__expect_exception(self):
    #     self.factory.add_ingredient("blue", 30)
    #     with self.assertRaises(KeyError) as context:
    #         self.factory.remove_ingredient("yellow", 30)
    #     expected_result = "'No such ingredient in the factory'"
    #     self.assertEqual(expected_result, str(context.exception))

    # def test_paint_factory_remove_ingredient__not_enough_capacity_in_ingredients__expect_exception(self):
    #     self.factory.add_ingredient("blue", 30)
    #     with self.assertRaises(ValueError) as context:
    #         self.factory.remove_ingredient("blue", 75)
    #     expected_result = "Ingredient quantity cannot be less than zero"
    #     self.assertEqual(expected_result, str(context.exception))

    # def test_paint_factory_remove_ingredient__remove_ingredient_from_ingredients(self):
    #     self.factory.add_ingredient("blue", 30)
    #     self.factory.remove_ingredient("blue", 10)
    #     expected_result = {'blue': 20}
    #     actual_result = self.factory.ingredients
    #     self.assertEqual(expected_result, actual_result)
    #
    # def test_paint_factory_products__expect_ingredients(self):
    #     self.factory.add_ingredient("blue", 30)
    #     expected_result = self.factory.products
    #     self.assertDictEqual(expected_result, self.factory.ingredients)


# if __name__ == '__main__':
#     unittest.main()
#
