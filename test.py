"""
Run Tests from Here. Do not run the test files in the Test Folder.
"""

import unittest
from Tests import map_tests
from Tests.edge_tests import EdgeTests
from Tests.item_tests import ItemTests
from Tests.character_tests import CharacterTests, PlayerTests, EnemyTests
from Tests.room_tests import RoomTests
from Tests.shop_room_tests import ShopRoomTests
from Tests.chest_room_tests import ChestRoomTests
from Tests.combat_room_tests import CombatRoomTests
from Tests.start_room_tests import StartRoomTests
from Tests.boss_room_tests import BossRoomTests


test_suite = unittest.TestSuite()

# Add to suite for each method in test class
# Map Tests
test_suite.addTests([map_tests.MapTests('test1'), map_tests.MapTests('test2')])
# Edge Tests
test_suite.addTests([EdgeTests('test1'), EdgeTests('test2'), EdgeTests('test3')])
# Item Tests
test_suite.addTests([ItemTests('test_1load_items1'), ItemTests('test_2load_items2'),
                     ItemTests('test_3load_items3'), ItemTests('test_4load_items4'),
                     ItemTests('test_5make_item1'), ItemTests('test_6item_stats1'),
                     ItemTests('test_7item_assign_stats'), ItemTests('test_8item_get_damage'),
                     ItemTests('test_9item_notitem')])
# Character Tests
test_suite.addTests([CharacterTests('test_1make_character'),
                     CharacterTests('test_2character_stats'),
                     CharacterTests('test_3set_living'), CharacterTests('test_4add_item'),
                     CharacterTests('test_5drop_item'), CharacterTests('test_6lv_up'),
                     CharacterTests('test_7update_max_health'),
                     CharacterTests('test_8update_health'), CharacterTests('test_9get_defense'),
                     CharacterTests('test_10get_attack'), CharacterTests('test_11defend_action')])
# Player Tests
test_suite.addTests([PlayerTests('test_1make_player'), PlayerTests('test_2player_stats'),
                     PlayerTests('test3_equip_item_real'),
                     PlayerTests('test4_equip_item_none_item'),
                     PlayerTests('test_5unequip_item_real'), PlayerTests('test_6unequip_item_none'),
                     PlayerTests('test_7use_medkits'), PlayerTests('test_8get_medkits'),
                     PlayerTests('test_9set_medkits'), PlayerTests('test_10change_name'),
                     PlayerTests('test_11update_defense'), PlayerTests('test_12update_attack'),
                     PlayerTests('test_13take_damage')])
# Enemy Tests
test_suite.addTests([EnemyTests('test_1make_enemy'), EnemyTests('test_2enemy_stats'),
                     EnemyTests('test_3take_damage'), EnemyTests('test_4update_defense'),
                     EnemyTests('test_5update_attack'), EnemyTests('test_6update_stats')])
# Room Tests
test_suite.addTests([RoomTests('test_1make_room'), RoomTests('test_2room_stats'),
                     RoomTests('test_3set_coordinates'), RoomTests('test_4get_coordinates'),
                     RoomTests('test_5clear_room'), RoomTests('test_6get_cleared'),
                     RoomTests('test_7create_adjacency'),
                     RoomTests('test_8create_adjacency_alreadyadjacent'),
                     RoomTests('test_9add_adjacent_room'), RoomTests('test_10get_adjacent_rooms'),
                     RoomTests('test_11generate_name'), RoomTests('test_12__repr__'),
                     RoomTests('test_13__eq__')])
# ChestRoom Tests
test_suite.addTests([ChestRoomTests('test_1make_chestroom'),
                     ChestRoomTests('test_2chestroom_stats')])
# CombatRoom Tests
test_suite.addTests([CombatRoomTests('test_1make_combatroom'),
                     CombatRoomTests('test_2combatroom_stats'),
                     CombatRoomTests('test_3generate_enemies'),
                     CombatRoomTests('test_4lv_enemies')])
# ShopRoom Tests
test_suite.addTests([ShopRoomTests('test_1make_shoproom'), ShopRoomTests('test_2shoproom_stats')])
# StartRoom Tests
test_suite.addTests([StartRoomTests('test_1make_startroom'),
                     StartRoomTests('test_2startroom_stats')])
# BossRoom Tests
test_suite.addTests([BossRoomTests('test_1make_bossroom'), BossRoomTests('test_2bossroom_stats')])
# ...

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
