import unittest
import pygame


class ContextModuleTest(unittest.TestCase):

    # how do you test something that creates a folder?
    # it's going to be run locally, I mean, is it okay
    # to do that to people's systems?
    def test_get_pref_path(self):
        pass

    def test_get_pref_locales(self):
        locales = pygame.context.get_pref_locales()

        # check type of return first
        self.assertIsInstance(locales, list)
        for lc in locales:
            self.assertIsInstance(lc, dict)
            lang = lc.get("language", None)
            self.assertIsInstance(lang, str)

            # length of language code should be greater than 1
            self.assertTrue(len(lang) > 1)

            try:
                # country field is optional
                country = lc["country"]
                self.assertIsInstance(country, str)

                # length of country code should be greater than 1
                self.assertTrue(len(country) > 1)
            except KeyError:
                pass

        # passing args should raise error
        for arg in (None, 1, "hello"):
            self.assertRaises(TypeError, pygame.context.get_pref_locales, arg)


if __name__ == "__main__":
    unittest.main()
