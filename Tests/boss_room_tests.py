"""Module containing the unittests for BossRoom.
"""

import unittest
from Classes.Rooms.boss_room import BossRoom


class BossRoomTests(unittest.TestCase):
    """Testcase for the BossRoom.
    """

    def test_1make_bossroom(self):
        """Check that the BossRoom initializes.
        """
        x = BossRoom()
        self.assertTrue(isinstance(x, BossRoom))

    def test_2bossroom_stats(self):
        """Check the BossRoom's instance attributes.
        """
        x = BossRoom()
        self.assertEqual(x.room_type, "Boss")
        self.assertTrue(x.name)
        self.assertTrue(x.is_boss_room)
        self.assertTrue(x.enemies)
        self.assertEqual(x.enemies[0].name, "BOSS")
