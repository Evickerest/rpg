"""Module containing the unittests for BossRoom.
"""

import unittest
from Classes.Rooms.boss_room import BossRoom


class BossRoomTests(unittest.TestCase):
    """Testcase for the BossRoom.
    """

    def test_1bossroom_init(self):
        """Check that the BossRoom initializes.
        """
        x = BossRoom()
        self.assertEqual(x.room_type, "Boss")
        self.assertTrue(x.name)
        self.assertTrue(x.is_boss_room)
        self.assertEqual(x.enemies_killed, 0)
        self.assertTrue(x.enemies)
        self.assertEqual(x.enemies[0].name, "BOSS")
