import unittest
from Tests import Map_tests
from Tests.Edge_tests import *
from Tests.Item_tests import *
from Tests.Character_tests import *
from Tests.Room_tests import *
from Tests.ShopRoom_tests import *
from Tests.ChestRoom_tests import *
from Tests.CombatRoom_tests import *
from Classes.Item import *


test_suite = unittest.TestSuite()

# Add to suite for each method in test class

# Map Tests
test_suite.addTests([Map_tests.Map_tests('test1'), Map_tests.Map_tests('test2')])

# Edge Tests
test_suite.addTests([Edge_tests('test1'), Edge_tests('test2'), Edge_tests('test3')])

# Item Tests
test_suite.addTests([ItemTests('test_1load_items1'), ItemTests('test_2load_items2'),
                     ItemTests('test_3load_items3'), ItemTests('test_4load_items4'),
                     ItemTests('test_5make_item1'), ItemTests('test_6item_stats1'),
                     ItemTests('test_7item_assign_stats'), ItemTests('test_8item_getDamage'),
                     ItemTests('test_9item_notitem')])

# Character Tests
test_suite.addTests([CharacterTests('test_1make_character'), CharacterTests('test_2character_stats'),
                     CharacterTests('test_3set_living'), CharacterTests('test_4addItem'),
                     CharacterTests('test_5dropItem'), CharacterTests('test_6lv_up'),
                     CharacterTests('test_7updateMaxHealth'), CharacterTests('test_8updateHealth'),
                     CharacterTests('test_9getDefense'), CharacterTests('test_10getAttack'),
                     CharacterTests('test_11defend_action')])
# Player Tests
test_suite.addTests([PlayerTests('test_1make_player'), PlayerTests('test_2player_stats'),
                     PlayerTests('test3_equip_item_Real'), PlayerTests('test4_equip_item_NoneItem'),
                     PlayerTests('test_5unequipItem_Real'), PlayerTests('test_6unequipItem_None'),
                     PlayerTests('test_7use_medkits'), PlayerTests('test_8get_medkits'),
                     PlayerTests('test_9set_medkits'), PlayerTests('test_10changeName'),
                     PlayerTests('test_11updateDefense'), PlayerTests('test_12updateAttack'),
                     PlayerTests('test_13takeDamage')])
# Enemy Tests
test_suite.addTests([EnemyTests('test_1make_enemy'), EnemyTests('test_2enemy_stats'),
                     EnemyTests('test_3take_damage'), EnemyTests('test_4updateDefense'),
                     EnemyTests('test_5updateAttack'), EnemyTests('test_6updateStats')])
# Room Tests
test_suite.addTests([RoomTests('test_1make_room'), RoomTests('test_2room_stats'),
                     RoomTests('test_3setCoordinates'), RoomTests('test_4getCoordinates'),
                     RoomTests('test_5clearRoom'), RoomTests('test_6getCleared'),
                     RoomTests('test_7createAdjacency'), RoomTests('test_8createAdjacency_AlreadyAdjacent'),
                     RoomTests('test_9AddAdjacentRoom'), RoomTests('test_10getAdjacentRooms'),
                     RoomTests('test_11generateName'), RoomTests('test_12__repr__'),
                     RoomTests('test_13__eq__')])
# ChestRoom Tests
test_suite.addTests([ChestRoomTests('test_1make_chestroom'), ChestRoomTests('test_2chestroom_stats')])
# CombatRoom Tests
test_suite.addTests([CombatRoomTests('test_1make_combatroom'),
                     CombatRoomTests('test_2combatroom_stats'),
                     CombatRoomTests('test_3generate_enemies'),
                     CombatRoomTests('test_4lv_enemies')])
# ShopRoom Tests
test_suite.addTests([ShopRoomTests('test_1make_shoproom'), ShopRoomTests('test_2shoproom_stats')])
# ...

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
