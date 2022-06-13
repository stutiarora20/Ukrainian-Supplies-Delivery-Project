'''Simple Travelling Salesperson Problem (TSP) on a circuit board.'''

import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


gmaps2 = {0: {0: 0, 1: 653, 2: 1143, 3: 895, 4: 1043, 5: 1307, 6: 1106, 7: 97, 8: 917, 9: 1020, 10: 1331, 11: 1400, 12: 1493, 13: 463, 14: 1340, 15: 1317, 16: 1006, 17: 795, 18: 1147, 19: 812, 20: 340, 21: 506, 22: 349, 23: 1001, 24: 1408, 25: 316, 26: 212, 27: 1026, 28: 933, 29: 791, 30: 228, 31: 259, 32: 628, 33: 1347, 34: 1237, 35: 1391, 36: 97.6, 37: 1428, 38: 227, 39: 1311, 40: 1328, 41: 1023, 42: 1308, 43: 1122, 44: 1468, 45: 905, 46: 692, 47: 373, 48: 1398, 49: 1570, 50: 242, 51: 631},
        1: {0: 648, 1: 0, 2: 486, 3: 475, 4: 496, 5: 752, 6: 559, 7: 541, 8: 421, 9: 601, 10: 784, 11: 903, 12: 837, 13: 270, 14: 785, 15: 821, 16: 349, 17: 156, 18: 650, 19: 190, 20: 348, 21: 140, 22: 531, 23: 344, 24: 751, 25: 328, 26: 605, 27: 454, 28: 331, 29: 303, 30: 463, 31: 400, 32: 86.5, 33: 690, 34: 691, 35: 734, 36: 622, 37: 831, 38: 809, 39: 764, 40: 671, 41: 543, 42: 812, 43: 568, 44: 812, 45: 251, 46: 38.6, 47: 442, 48: 741, 49: 914, 50: 771, 51: 211},
        2: {0: 1134, 1: 480, 2: 0, 3: 815, 4: 217, 5: 313, 6: 297, 7: 1027, 8: 366, 9: 678, 10: 420, 11: 767, 12: 340, 13: 737, 14: 301, 15: 684, 16: 143, 17: 592, 18: 552, 19: 381, 20: 834, 21: 627, 22: 1018, 23: 184, 24: 254, 25: 814, 26: 1091, 27: 266, 28: 250, 29: 384, 30: 949, 31: 886, 32: 561, 33: 193, 34: 417, 35: 237, 36: 1109, 37: 335, 38: 1296, 39: 490, 40: 174, 41: 345, 42: 735, 43: 245, 44: 315, 45: 327, 46: 469, 47: 928, 48: 245, 49: 417, 50: 1257, 51: 555},
        3: {0: 896, 1: 474, 2: 814, 3: 0, 4: 675, 5: 940, 6: 739, 7: 795, 8: 550, 9: 133, 10: 964, 11: 1032, 12: 1070, 13: 425, 14: 973, 15: 950, 16: 677, 17: 634, 18: 779, 19: 445, 20: 551, 21: 502, 22: 683, 23: 769, 24: 942, 25: 701, 26: 798, 27: 659, 28: 565, 29: 424, 30: 666, 31: 774, 32: 395, 33: 923, 34: 870, 35: 1001, 36: 850, 37: 1060, 38: 1018, 39: 943, 40: 936, 41: 655, 42: 941, 43: 755, 44: 1041, 45: 727, 46: 508, 47: 646, 48: 994, 49: 1138, 50: 980, 51: 271},
        4: {0: 1043, 1: 480, 2: 218, 3: 675, 4: 0, 5: 262, 6: 85.1, 7: 941, 8: 146, 9: 538, 10: 310, 11: 582, 12: 392, 13: 571, 14: 295, 15: 499, 16: 196, 17: 592, 18: 329, 19: 308, 20: 698, 21: 627, 22: 830, 23: 373, 24: 264, 25: 815, 26: 944, 27: 43.7, 28: 161, 29: 245, 30: 813, 31: 887, 32: 460, 33: 245, 34: 217, 35: 323, 36: 997, 37: 383, 38: 1165, 39: 290, 40: 258, 41: 122, 42: 491, 43: 77.2, 44: 363, 45: 459, 46: 470, 47: 792, 48: 316, 49: 460, 50: 1126, 51: 416},
        5: {0: 1377, 1: 723, 2: 301, 3: 939, 4: 261, 5: 0, 6: 229, 7: 1271, 8: 410, 9: 802, 10: 113, 11: 648, 12: 167, 13: 835, 14: 15.7, 15: 565, 16: 406, 17: 835, 18: 527, 19: 558, 20: 962, 21: 870, 22: 1094, 23: 502, 24: 48.6, 25: 1057, 26: 1208, 27: 310, 28: 430, 29: 509, 30: 1077, 31: 1130, 32: 724, 33: 119, 34: 300, 35: 148, 36: 1352, 37: 103, 38: 1429, 39: 192, 40: 133, 41: 335, 42: 616, 43: 188, 44: 124, 45: 645, 46: 712, 47: 1056, 48: 141, 49: 181, 50: 1390, 51: 680},
        6: {0: 1106, 1: 557, 2: 307, 3: 739, 4: 84.6, 5: 232, 6: 0, 7: 1005, 8: 210, 9: 602, 10: 227, 11: 483, 12: 402, 13: 635, 14: 252, 15: 400, 16: 264, 17: 669, 18: 314, 19: 372, 20: 762, 21: 704, 22: 894, 23: 463, 24: 285, 25: 892, 26: 1008, 27: 108, 28: 225, 29: 309, 30: 877, 31: 964, 32: 524, 33: 287, 34: 133, 35: 342, 36: 1061, 37: 339, 38: 1229, 39: 207, 40: 300, 41: 107, 42: 451, 43: 141, 44: 361, 45: 536, 46: 547, 47: 856, 48: 335, 49: 417, 50: 1190, 51: 480},
        7: {0: 97.2, 1: 548, 2: 1037, 3: 796, 4: 944, 5: 1208, 6: 1007, 7: 0, 8: 818, 9: 922, 10: 1232, 11: 1301, 12: 1388, 13: 364, 14: 1241, 15: 1218, 16: 900, 17: 690, 18: 1048, 19: 713, 20: 241, 21: 400, 22: 277, 23: 895, 24: 1302, 25: 211, 26: 134, 27: 927, 28: 834, 29: 692, 30: 129, 31: 151, 32: 548, 33: 1241, 34: 1139, 35: 1285, 36: 77, 37: 1329, 38: 268, 39: 1212, 40: 1222, 41: 924, 42: 1210, 43: 1024, 44: 1363, 45: 799, 46: 587, 47: 274, 48: 1293, 49: 1465, 50: 229, 51: 532},
        8: {0: 911, 1: 420, 2: 366, 3: 544, 4: 146, 5: 410, 6: 209, 7: 810, 8: 0, 9: 410, 10: 435, 11: 484, 12: 541, 13: 440, 14: 443, 15: 401, 16: 277, 17: 575, 18: 231, 19: 247, 20: 567, 21: 517, 22: 699, 23: 453, 24: 413, 25: 717, 26: 813, 27: 130, 28: 156, 29: 119, 30: 682, 31: 789, 32: 411, 33: 394, 34: 341, 35: 472, 36: 866, 37: 531, 38: 1034, 39: 414, 40: 406, 41: 107, 42: 393, 43: 226, 44: 511, 45: 460, 46: 431, 47: 661, 48: 465, 49: 609, 50: 995, 51: 285},
        9: {0: 1021, 1: 599, 2: 939, 3: 132, 4: 800, 5: 1064, 6: 863, 7: 919, 8: 675, 9: 0, 10: 1089, 11: 1157, 12: 1195, 13: 549, 14: 1097, 15: 1074, 16: 802, 17: 759, 18: 904, 19: 569, 20: 676, 21: 626, 22: 808, 23: 894, 24: 1067, 25: 826, 26: 923, 27: 784, 28: 690, 29: 549, 30: 791, 31: 898, 32: 520, 33: 1048, 34: 995, 35: 1126, 36: 975, 37: 1185, 38: 1143, 39: 1068, 40: 1060, 41: 780, 42: 1066, 43: 880, 44: 1165, 45: 852, 46: 633, 47: 770, 48: 1119, 49: 1263, 50: 1104, 51: 396},
        10: {0: 1332, 1: 783, 2: 419, 3: 965, 4: 310, 5: 113, 6: 226, 7: 1231, 8: 435, 9: 828, 10: 0, 11: 540, 12: 283, 13: 861, 14: 132, 15: 457, 16: 488, 17: 895, 18: 419, 19: 598, 20: 987, 21: 930, 22: 1119, 23: 666, 24: 166, 25: 1117, 26: 1234, 27: 333, 28: 450, 29: 534, 30: 1103, 31: 1190, 32: 750, 33: 250, 34: 192, 35: 265, 36: 1287, 37: 220, 38: 1454, 39: 84.1, 40: 250, 41: 332, 42: 508, 43: 277, 44: 242, 45: 762, 46: 773, 47: 1082, 48: 259, 49: 298, 50: 1416, 51: 705},
        11: {0: 1392, 1: 901, 2: 765, 3: 1025, 4: 581, 5: 647, 6: 480, 7: 1291, 8: 482, 9: 892, 10: 539, 11: 0, 12: 817, 13: 921, 14: 666, 15: 80.7, 16: 743, 17: 1056, 18: 354, 19: 728, 20: 1048, 21: 998, 22: 1180, 23: 921, 24: 700, 25: 1198, 26: 1294, 27: 604, 28: 645, 29: 601, 30: 1163, 31: 1270, 32: 892, 33: 742, 34: 352, 35: 799, 36: 1347, 37: 754, 38: 1515, 39: 467, 40: 754, 41: 460, 42: 123, 43: 609, 44: 776, 45: 948, 46: 912, 47: 1142, 48: 793, 49: 832, 50: 1476, 51: 766},
        12: {0: 1485, 1: 831, 2: 340, 3: 1071, 4: 393, 5: 168, 6: 401, 7: 1379, 8: 542, 9: 934, 10: 285, 11: 820, 12: 0, 13: 967, 14: 153, 15: 737, 16: 495, 17: 943, 18: 700, 19: 732, 20: 1186, 21: 978, 22: 1369, 23: 541, 24: 127, 25: 1166, 26: 1443, 27: 442, 28: 602, 29: 641, 30: 1301, 31: 1238, 32: 912, 33: 182, 34: 472, 35: 107, 36: 1460, 37: 65.9, 38: 1647, 39: 364, 40: 176, 41: 508, 42: 788, 43: 320, 44: 42.8, 45: 684, 46: 821, 47: 1280, 48: 92.1, 49: 77.5, 50: 1609, 51: 812},
        13: {0: 465, 1: 276, 2: 711, 3: 424, 4: 572, 5: 836, 6: 635, 7: 364, 8: 446, 9: 550, 10: 861, 11: 929, 12: 967, 13: 0, 14: 869, 15: 846, 16: 574, 17: 418, 18: 676, 19: 341, 20: 120, 21: 128, 22: 285, 23: 597, 24: 839, 25: 316, 26: 367, 27: 556, 28: 462, 29: 321, 30: 235, 31: 389, 32: 180, 33: 820, 34: 767, 35: 898, 36: 419, 37: 957, 38: 587, 39: 840, 40: 832, 41: 552, 42: 838, 43: 652, 44: 937, 45: 515, 46: 297, 47: 215, 48: 891, 49: 1035, 50: 549, 51: 160},
        14: {0: 1411, 1: 757, 2: 292, 3: 974, 4: 295, 5: 15.9, 6: 249, 7: 1305, 8: 444, 9: 837, 10: 133, 11: 668, 12: 152, 13: 870, 14: 0, 15: 585, 16: 440, 17: 869, 18: 548, 19: 592, 20: 996, 21: 904, 22: 1128, 23: 492, 24: 39.1, 25: 1092, 26: 1243, 27: 344, 28: 465, 29: 543, 30: 1112, 31: 1164, 32: 759, 33: 130, 34: 320, 35: 138, 36: 1386, 37: 88.9, 38: 1463, 39: 212, 40: 123, 41: 356, 42: 636, 43: 223, 44: 115, 45: 636, 46: 747, 47: 1091, 48: 132, 49: 167, 50: 1425, 51: 714},
        15: {0: 1311, 1: 820, 2: 684, 3: 944, 4: 500, 5: 566, 6: 399, 7: 1210, 8: 400, 9: 811, 10: 458, 11: 83.3, 12: 736, 13: 840, 14: 585, 15: 0, 16: 662, 17: 975, 18: 273, 19: 647, 20: 967, 21: 917, 22: 1099, 23: 839, 24: 619, 25: 1117, 26: 1213, 27: 523, 28: 564, 29: 520, 30: 1082, 31: 1189, 32: 811, 33: 661, 34: 271, 35: 718, 36: 1266, 37: 673, 38: 1434, 39: 386, 40: 673, 41: 379, 42: 72.3, 43: 527, 44: 694, 45: 867, 46: 831, 47: 1061, 48: 711, 49: 751, 50: 1395, 51: 685},
        16: {0: 996, 1: 342, 2: 143, 3: 678, 4: 197, 5: 409, 6: 261, 7: 890, 8: 275, 9: 541, 10: 491, 11: 747, 12: 494, 13: 600, 14: 442, 15: 664, 16: 0, 17: 454, 18: 499, 19: 243, 20: 697, 21: 489, 22: 880, 23: 175, 24: 408, 25: 677, 26: 954, 27: 155, 28: 113, 29: 247, 30: 812, 31: 749, 32: 423, 33: 347, 34: 397, 35: 391, 36: 971, 37: 489, 38: 1158, 39: 471, 40: 328, 41: 298, 42: 661, 43: 225, 44: 469, 45: 243, 46: 332, 47: 791, 48: 399, 49: 571, 50: 1120, 51: 418},
        17: {0: 794, 1: 157, 2: 593, 3: 633, 4: 605, 5: 859, 6: 662, 7: 687, 8: 576, 9: 759, 10: 887, 11: 1059, 12: 944, 13: 416, 14: 892, 15: 976, 16: 456, 17: 0, 18: 806, 19: 328, 20: 494, 21: 287, 22: 677, 23: 397, 24: 858, 25: 474, 26: 751, 27: 562, 28: 438, 29: 458, 30: 609, 31: 546, 32: 244, 33: 797, 34: 794, 35: 841, 36: 768, 37: 939, 38: 955, 39: 867, 40: 778, 41: 699, 42: 967, 43: 675, 44: 919, 45: 270, 46: 147, 47: 588, 48: 849, 49: 1021, 50: 917, 51: 369},
        18: {0: 1141, 1: 650, 2: 552, 3: 774, 4: 330, 5: 527, 6: 314, 7: 1040, 8: 230, 9: 641, 10: 419, 11: 355, 12: 697, 13: 670, 14: 547, 15: 272, 16: 501, 17: 805, 18: 0, 19: 477, 20: 797, 21: 747, 22: 929, 23: 708, 24: 580, 25: 947, 26: 1043, 27: 353, 28: 394, 29: 350, 30: 912, 31: 1019, 32: 641, 33: 571, 34: 231, 35: 650, 36: 1096, 37: 634, 38: 1264, 39: 348, 40: 584, 41: 209, 42: 264, 43: 404, 44: 656, 45: 697, 46: 661, 47: 891, 48: 643, 49: 712, 50: 1225, 51: 515},
        19: {0: 843, 1: 189, 2: 370, 3: 445, 4: 309, 5: 574, 6: 373, 7: 736, 8: 247, 9: 571, 10: 598, 11: 730, 12: 721, 13: 342, 14: 607, 15: 647, 16: 234, 17: 326, 18: 477, 19: 0, 20: 468, 21: 336, 22: 600, 23: 322, 24: 635, 25: 523, 26: 715, 27: 244, 28: 131, 29: 130, 30: 583, 31: 595, 32: 174, 33: 574, 34: 504, 35: 618, 36: 767, 37: 695, 38: 935, 39: 577, 40: 555, 41: 357, 42: 639, 43: 389, 44: 696, 45: 294, 46: 182, 47: 562, 48: 626, 49: 798, 50: 896, 51: 184},
        20: {0: 341, 1: 355, 2: 845, 3: 552, 4: 700, 5: 964, 6: 763, 7: 240, 8: 574, 9: 678, 10: 989, 11: 1057, 12: 1095, 13: 120, 14: 997, 15: 974, 16: 708, 17: 497, 18: 804, 19: 469, 20: 0, 21: 189, 22: 188, 23: 703, 24: 967, 25: 194, 26: 243, 27: 684, 28: 590, 29: 449, 30: 112, 31: 257, 32: 286, 33: 948, 34: 895, 35: 1026, 36: 296, 37: 1085, 38: 464, 39: 968, 40: 960, 41: 680, 42: 966, 43: 780, 44: 1065, 45: 607, 46: 394, 47: 98.9, 48: 1019, 49: 1163, 50: 425, 51: 288},
        21: {0: 508, 1: 151, 2: 641, 3: 501, 4: 602, 5: 866, 6: 665, 7: 402, 8: 524, 9: 627, 10: 890, 11: 1006, 12: 991, 13: 129, 14: 899, 15: 924, 16: 504, 17: 293, 18: 753, 19: 316, 20: 189, 21: 0, 22: 390, 23: 499, 24: 906, 25: 188, 26: 465, 27: 585, 28: 486, 29: 398, 30: 322, 31: 261, 32: 139, 33: 845, 34: 796, 35: 889, 36: 483, 37: 986, 38: 670, 39: 870, 40: 825, 41: 629, 42: 915, 43: 682, 44: 966, 45: 403, 46: 190, 47: 301, 48: 896, 49: 1068, 50: 631, 51: 237},
        22: {0: 350, 1: 539, 2: 1028, 3: 683, 4: 831, 5: 1095, 6: 894, 7: 275, 8: 705, 9: 808, 10: 1119, 11: 1188, 12: 1225, 13: 289, 14: 1128, 15: 1105, 16: 891, 17: 680, 18: 935, 19: 600, 20: 188, 21: 390, 22: 0, 23: 886, 24: 1097, 25: 322, 26: 136, 27: 814, 28: 721, 29: 579, 30: 173, 31: 336, 32: 469, 33: 1078, 34: 1025, 35: 1156, 36: 265, 37: 1216, 38: 407, 39: 1099, 40: 1091, 41: 811, 42: 1096, 43: 911, 44: 1196, 45: 790, 46: 578, 47: 90.7, 48: 1150, 49: 1294, 50: 368, 51: 419},
        23: {0: 981, 1: 366, 2: 187, 3: 836, 4: 371, 5: 511, 6: 452, 7: 875, 8: 520, 9: 962, 10: 665, 11: 922, 12: 537, 13: 604, 14: 498, 15: 839, 16: 175, 17: 319, 18: 706, 19: 325, 20: 681, 21: 474, 22: 865, 23: 0, 24: 452, 25: 662, 26: 939, 27: 329, 28: 288, 29: 422, 30: 797, 31: 734, 32: 447, 33: 391, 34: 572, 35: 435, 36: 956, 37: 532, 38: 1143, 39: 645, 40: 372, 41: 499, 42: 890, 43: 399, 44: 512, 45: 128, 46: 308, 47: 776, 48: 442, 49: 614, 50: 1104, 51: 572},
        24: {0: 1401, 1: 747, 2: 255, 3: 941, 4: 262, 5: 56.2, 6: 290, 7: 1294, 8: 411, 9: 804, 10: 173, 11: 708, 12: 123, 13: 837, 14: 40.5, 15: 626, 16: 410, 17: 858, 18: 588, 19: 559, 20: 963, 21: 894, 22: 1095, 23: 456, 24: 0, 25: 1081, 26: 1210, 27: 311, 28: 432, 29: 510, 30: 1079, 31: 1153, 32: 827, 33: 93.6, 34: 360, 35: 102, 36: 1375, 37: 84.8, 38: 1562, 39: 253, 40: 86.8, 41: 396, 42: 677, 43: 190, 44: 83.3, 45: 599, 46: 736, 47: 1058, 48: 95.1, 49: 155, 50: 1524, 51: 681},
        25: {0: 317, 1: 336, 2: 825, 3: 702, 4: 811, 5: 1091, 6: 874, 7: 211, 8: 725, 9: 828, 10: 1099, 11: 1207, 12: 1176, 13: 318, 14: 1125, 15: 1125, 16: 689, 17: 478, 18: 954, 19: 529, 20: 194, 21: 189, 22: 328, 23: 684, 24: 1091, 25: 0, 26: 275, 27: 794, 28: 671, 29: 599, 30: 159, 31: 72.6, 32: 336, 33: 1029, 34: 1005, 35: 1073, 36: 292, 37: 1171, 38: 479, 39: 1078, 40: 1010, 41: 830, 42: 1116, 43: 907, 44: 1151, 45: 588, 46: 375, 47: 293, 48: 1081, 49: 1253, 50: 440, 51: 438},
        26: {0: 213, 1: 611, 2: 1101, 3: 797, 4: 945, 5: 1209, 6: 1008, 7: 132, 8: 819, 9: 922, 10: 1233, 11: 1302, 12: 1339, 13: 365, 14: 1242, 15: 1219, 16: 964, 17: 753, 18: 1049, 19: 714, 20: 242, 21: 452, 22: 136, 23: 959, 24: 1211, 25: 275, 26: 0, 27: 928, 28: 835, 29: 693, 30: 135, 31: 259, 32: 531, 33: 1192, 34: 1139, 35: 1270, 36: 128, 37: 1330, 38: 270, 39: 1213, 40: 1205, 41: 925, 42: 1210, 43: 1025, 44: 1310, 45: 863, 46: 650, 47: 183, 48: 1264, 49: 1408, 50: 231, 51: 533},
        27: {0: 1026, 1: 451, 2: 266, 3: 659, 4: 43.9, 5: 309, 6: 107, 7: 925, 8: 129, 9: 522, 10: 332, 11: 604, 12: 440, 13: 555, 14: 343, 15: 521, 16: 157, 17: 563, 18: 351, 19: 241, 20: 681, 21: 598, 22: 813, 23: 332, 24: 312, 25: 785, 26: 928, 27: 0, 28: 122, 29: 228, 30: 796, 31: 858, 32: 443, 33: 293, 34: 239, 35: 371, 36: 980, 37: 430, 38: 1148, 39: 312, 40: 305, 41: 144, 42: 513, 43: 125, 44: 410, 45: 430, 46: 440, 47: 776, 48: 364, 49: 508, 50: 1110, 51: 399},
        28: {0: 979, 1: 325, 2: 250, 3: 566, 4: 161, 5: 414, 6: 224, 7: 873, 8: 156, 9: 429, 10: 449, 11: 647, 12: 601, 13: 462, 14: 447, 15: 564, 16: 113, 17: 437, 18: 394, 19: 128, 20: 588, 21: 472, 22: 720, 23: 288, 24: 417, 25: 659, 26: 835, 27: 121, 28: 0, 29: 135, 30: 704, 31: 732, 32: 302, 33: 454, 34: 356, 35: 498, 36: 954, 37: 535, 38: 1055, 39: 429, 40: 435, 41: 261, 42: 555, 43: 230, 44: 576, 45: 304, 46: 315, 47: 683, 48: 506, 49: 678, 50: 1017, 51: 306},
        29: {0: 792, 1: 302, 2: 384, 3: 425, 4: 245, 5: 509, 6: 308, 7: 691, 8: 120, 9: 290, 10: 533, 11: 602, 12: 639, 13: 321, 14: 542, 15: 519, 16: 247, 17: 457, 18: 349, 19: 129, 20: 448, 21: 398, 22: 580, 23: 422, 24: 511, 25: 598, 26: 694, 27: 228, 28: 135, 29: 0, 30: 563, 31: 670, 32: 292, 33: 492, 34: 439, 35: 570, 36: 747, 37: 630, 38: 915, 39: 513, 40: 505, 41: 225, 42: 511, 43: 325, 44: 610, 45: 425, 46: 313, 47: 542, 48: 564, 49: 708, 50: 876, 51: 166},
        30: {0: 229, 1: 469, 2: 959, 3: 666, 4: 814, 5: 1078, 6: 877, 7: 128, 8: 688, 9: 792, 10: 1102, 11: 1171, 12: 1208, 13: 234, 14: 1111, 15: 1088, 16: 822, 17: 611, 18: 918, 19: 583, 20: 111, 21: 321, 22: 172, 23: 817, 24: 1081, 25: 153, 26: 134, 27: 797, 28: 704, 29: 562, 30: 0, 31: 168, 32: 400, 33: 1061, 34: 1009, 35: 1140, 36: 184, 37: 1199, 38: 352, 39: 1082, 40: 1074, 41: 794, 42: 1080, 43: 894, 44: 1179, 45: 721, 46: 508, 47: 144, 48: 1133, 49: 1277, 50: 313, 51: 402},
        31: {0: 261, 1: 408, 2: 897, 3: 774, 4: 882, 5: 1163, 6: 945, 7: 151, 8: 797, 9: 900, 10: 1171, 11: 1279, 12: 1248, 13: 389, 14: 1196, 15: 1196, 16: 760, 17: 550, 18: 1026, 19: 601, 20: 257, 21: 260, 22: 337, 23: 755, 24: 1162, 25: 72.6, 26: 260, 27: 866, 28: 742, 29: 671, 30: 167, 31: 0, 32: 408, 33: 1101, 34: 1077, 35: 1145, 36: 234, 37: 1243, 38: 421, 39: 1150, 40: 1082, 41: 902, 42: 1188, 43: 979, 44: 1223, 45: 659, 46: 447, 47: 301, 48: 1153, 49: 1325, 50: 383, 51: 510},
        32: {0: 659, 1: 85.5, 2: 562, 3: 395, 4: 460, 5: 724, 6: 523, 7: 553, 8: 418, 9: 521, 10: 748, 11: 900, 12: 912, 13: 181, 14: 757, 15: 817, 16: 425, 17: 245, 18: 647, 19: 180, 20: 282, 21: 139, 22: 466, 23: 420, 24: 727, 25: 340, 26: 529, 27: 443, 28: 311, 29: 292, 30: 397, 31: 412, 32: 0, 33: 766, 34: 655, 35: 810, 36: 581, 37: 845, 38: 749, 39: 728, 40: 747, 41: 523, 42: 809, 43: 540, 44: 888, 45: 338, 46: 120, 47: 377, 48: 817, 49: 989, 50: 711, 51: 131},
        33: {0: 1340, 1: 686, 2: 194, 3: 928, 4: 249, 5: 122, 6: 284, 7: 1233, 8: 398, 9: 791, 10: 228, 11: 704, 12: 181, 13: 824, 14: 138, 15: 621, 16: 349, 17: 797, 18: 577, 19: 587, 20: 950, 21: 833, 22: 1082, 23: 395, 24: 93.7, 25: 1020, 26: 1197, 27: 298, 28: 419, 29: 497, 30: 1066, 31: 1092, 32: 766, 33: 0, 34: 354, 35: 99, 36: 1314, 37: 174, 38: 1501, 39: 308, 40: 25.8, 41: 370, 42: 672, 43: 177, 44: 154, 45: 538, 46: 675, 47: 1045, 48: 106, 49: 257, 50: 1463, 51: 668},
        34: {0: 1238, 1: 689, 2: 416, 3: 871, 4: 216, 5: 301, 6: 132, 7: 1137, 8: 341, 9: 734, 10: 192, 11: 353, 12: 471, 13: 767, 14: 320, 15: 270, 16: 394, 17: 801, 18: 231, 19: 504, 20: 893, 21: 836, 22: 1025, 23: 572, 24: 354, 25: 1023, 26: 1140, 27: 239, 28: 356, 29: 440, 30: 1009, 31: 1096, 32: 656, 33: 393, 34: 0, 35: 453, 36: 1193, 37: 408, 38: 1360, 39: 121, 40: 406, 41: 238, 42: 321, 43: 260, 44: 429, 45: 668, 46: 679, 47: 988, 48: 446, 49: 486, 50: 1322, 51: 611},
        35: {0: 1383, 1: 729, 2: 238, 3: 1001, 4: 323, 5: 175, 6: 340, 7: 1277, 8: 472, 9: 864, 10: 281, 11: 816, 12: 107, 13: 897, 14: 151, 15: 733, 16: 393, 17: 841, 18: 651, 19: 630, 20: 1083, 21: 876, 22: 1267, 23: 438, 24: 104, 25: 1064, 26: 1341, 27: 371, 28: 500, 29: 571, 30: 1199, 31: 1136, 32: 810, 33: 98.6, 34: 409, 35: 0, 36: 1358, 37: 146, 38: 1545, 39: 360, 40: 85.8, 41: 443, 42: 784, 43: 250, 44: 90.2, 45: 582, 46: 719, 47: 1178, 48: 10.9, 49: 164, 50: 1506, 51: 742},
        36: {0: 98.2, 1: 633, 2: 1123, 3: 850, 4: 998, 5: 1262, 6: 1061, 7: 77.9, 8: 872, 9: 975, 10: 1286, 11: 1354, 12: 1473, 13: 418, 14: 1295, 15: 1272, 16: 986, 17: 775, 18: 1102, 19: 767, 20: 295, 21: 486, 22: 265, 23: 981, 24: 1388, 25: 297, 26: 128, 27: 981, 28: 887, 29: 746, 30: 184, 31: 239, 32: 583, 33: 1327, 34: 1192, 35: 1371, 36: 0, 37: 1383, 38: 223, 39: 1265, 40: 1308, 41: 978, 42: 1263, 43: 1077, 44: 1449, 45: 885, 46: 672, 47: 312, 48: 1378, 49: 1550, 50: 185, 51: 586},
        37: {0: 1480, 1: 826, 2: 334, 3: 1062, 4: 383, 5: 104, 6: 337, 7: 1374, 8: 532, 9: 925, 10: 221, 11: 756, 12: 65.2, 13: 958, 14: 88.9, 15: 673, 16: 489, 17: 938, 18: 636, 19: 680, 20: 1084, 21: 973, 22: 1216, 23: 535, 24: 84.1, 25: 1160, 26: 1331, 27: 432, 28: 553, 29: 631, 30: 1200, 31: 1233, 32: 847, 33: 173, 34: 408, 35: 146, 36: 1455, 37: 0, 38: 1551, 39: 300, 40: 166, 41: 444, 42: 724, 43: 311, 44: 70.1, 45: 678, 46: 816, 47: 1179, 48: 148, 49: 75.9, 50: 1513, 51: 802},
        38: {0: 226, 1: 815, 2: 1304, 3: 1017, 4: 1165, 5: 1429, 6: 1228, 7: 268, 8: 1039, 9: 1143, 10: 1453, 11: 1522, 12: 1655, 13: 585, 14: 1462, 15: 1439, 16: 1168, 17: 957, 18: 1269, 19: 934, 20: 463, 21: 668, 22: 406, 23: 1162, 24: 1432, 25: 478, 26: 269, 27: 1149, 28: 1055, 29: 914, 30: 351, 31: 420, 32: 751, 33: 1508, 34: 1360, 35: 1552, 36: 223, 37: 1550, 38: 0, 39: 1433, 40: 1489, 41: 1145, 42: 1431, 43: 1245, 44: 1630, 45: 1066, 46: 854, 47: 453, 48: 1560, 49: 1732, 50: 40.6, 51: 753},
        39: {0: 1311, 1: 762, 2: 489, 3: 944, 4: 289, 5: 192, 6: 205, 7: 1210, 8: 415, 9: 807, 10: 84.1, 11: 469, 12: 362, 13: 840, 14: 212, 15: 386, 16: 467, 17: 874, 18: 348, 19: 577, 20: 967, 21: 909, 22: 1099, 23: 645, 24: 245, 25: 1097, 26: 1213, 27: 312, 28: 430, 29: 514, 30: 1082, 31: 1169, 32: 729, 33: 330, 34: 120, 35: 345, 36: 1266, 37: 299, 38: 1434, 39: 0, 40: 330, 41: 312, 42: 437, 43: 333, 44: 321, 45: 741, 46: 752, 47: 1061, 48: 338, 49: 377, 50: 1395, 51: 685},
        40: {0: 1320, 1: 666, 2: 174, 3: 941, 4: 263, 5: 145, 6: 298, 7: 1214, 8: 412, 9: 804, 10: 252, 11: 717, 12: 174, 13: 837, 14: 133, 15: 634, 16: 329, 17: 778, 18: 591, 19: 567, 20: 1020, 21: 813, 22: 1204, 23: 375, 24: 86.3, 25: 1000, 26: 1278, 27: 312, 28: 436, 29: 511, 30: 1135, 31: 1073, 32: 747, 33: 25.2, 34: 367, 35: 85.6, 36: 1295, 37: 167, 38: 1482, 39: 331, 40: 0, 41: 383, 42: 685, 43: 190, 44: 147, 45: 518, 46: 656, 47: 1114, 48: 77.9, 49: 250, 50: 1443, 51: 682},
        41: {0: 1017, 1: 595, 2: 345, 3: 650, 4: 122, 5: 336, 6: 107, 7: 916, 8: 106, 9: 516, 10: 332, 11: 462, 12: 506, 13: 546, 14: 355, 15: 379, 16: 301, 17: 707, 18: 209, 19: 353, 20: 672, 21: 623, 22: 804, 23: 501, 24: 389, 25: 822, 26: 919, 27: 145, 28: 262, 29: 225, 30: 787, 31: 895, 32: 516, 33: 364, 34: 238, 35: 442, 36: 971, 37: 443, 38: 1139, 39: 311, 40: 377, 41: 0, 42: 370, 43: 196, 44: 464, 45: 574, 46: 585, 47: 766, 48: 435, 49: 520, 50: 1101, 51: 390},
        42: {0: 1301, 1: 810, 2: 727, 3: 934, 4: 490, 5: 610, 6: 443, 7: 1200, 8: 390, 9: 801, 10: 501, 11: 117, 12: 780, 13: 830, 14: 629, 15: 77.3, 16: 661, 17: 965, 18: 263, 19: 637, 20: 957, 21: 907, 22: 1089, 23: 883, 24: 663, 25: 1107, 26: 1203, 27: 513, 28: 554, 29: 510, 30: 1072, 31: 1179, 32: 801, 33: 704, 34: 314, 35: 762, 36: 1256, 37: 717, 38: 1424, 39: 430, 40: 717, 41: 369, 42: 0, 43: 571, 44: 738, 45: 857, 46: 821, 47: 1051, 48: 755, 49: 794, 50: 1385, 51: 675},
        43: {0: 1193, 1: 539, 2: 243, 3: 755, 4: 76.8, 5: 189, 6: 141, 7: 1087, 8: 226, 9: 618, 10: 277, 11: 610, 12: 319, 13: 651, 14: 222, 15: 528, 16: 222, 17: 651, 18: 405, 19: 373, 20: 778, 21: 686, 22: 910, 23: 399, 24: 191, 25: 873, 26: 1024, 27: 126, 28: 246, 29: 325, 30: 893, 31: 946, 32: 540, 33: 172, 34: 261, 35: 250, 36: 1168, 37: 310, 38: 1245, 39: 334, 40: 185, 41: 197, 42: 579, 43: 0, 44: 290, 45: 542, 46: 528, 47: 872, 48: 244, 49: 387, 50: 1206, 51: 496},
        44: {0: 1463, 1: 809, 2: 317, 3: 1045, 4: 366, 5: 135, 6: 368, 7: 1357, 8: 515, 9: 908, 10: 252, 11: 787, 12: 42.2, 13: 941, 14: 120, 15: 704, 16: 472, 17: 921, 18: 667, 19: 710, 20: 1163, 21: 956, 22: 1347, 23: 518, 24: 88, 25: 1143, 26: 1420, 27: 415, 28: 579, 29: 614, 30: 1278, 31: 1216, 32: 890, 33: 156, 34: 439, 35: 90.3, 36: 1438, 37: 48.3, 38: 1625, 39: 331, 40: 149, 41: 487, 42: 755, 43: 294, 44: 0, 45: 661, 46: 798, 47: 1257, 48: 79.5, 49: 118, 50: 1586, 51: 785},
        45: {0: 904, 1: 261, 2: 330, 3: 733, 4: 514, 5: 654, 6: 528, 7: 798, 8: 460, 9: 859, 10: 808, 11: 950, 12: 680, 13: 526, 14: 642, 15: 867, 16: 244, 17: 192, 18: 697, 19: 296, 20: 604, 21: 397, 22: 788, 23: 128, 24: 595, 25: 584, 26: 861, 27: 427, 28: 304, 29: 426, 30: 719, 31: 657, 32: 345, 33: 534, 34: 715, 35: 578, 36: 879, 37: 675, 38: 1066, 39: 788, 40: 515, 41: 565, 42: 859, 43: 542, 44: 656, 45: 0, 46: 233, 47: 698, 48: 585, 49: 757, 50: 1027, 51: 469},
        46: {0: 672, 1: 29.3, 2: 476, 3: 502, 4: 489, 5: 742, 6: 569, 7: 566, 8: 431, 9: 627, 10: 795, 11: 914, 12: 827, 13: 294, 14: 775, 15: 831, 16: 340, 17: 147, 18: 661, 19: 183, 20: 372, 21: 165, 22: 556, 23: 308, 24: 741, 25: 352, 26: 629, 27: 445, 28: 321, 29: 313, 30: 487, 31: 425, 32: 113, 33: 680, 34: 701, 35: 724, 36: 647, 37: 822, 38: 834, 39: 774, 40: 661, 41: 554, 42: 823, 43: 558, 44: 802, 45: 221, 46: 0, 47: 466, 48: 732, 49: 904, 50: 795, 51: 238},
        47: {0: 374, 1: 449, 2: 938, 3: 613, 4: 761, 5: 1025, 6: 824, 7: 273, 8: 636, 9: 739, 10: 1050, 11: 1118, 12: 1156, 13: 183, 14: 1058, 15: 1035, 16: 801, 17: 591, 18: 865, 19: 530, 20: 98.7, 21: 301, 22: 89.8, 23: 796, 24: 1028, 25: 287, 26: 185, 27: 745, 28: 651, 29: 510, 30: 144, 31: 301, 32: 379, 33: 1009, 34: 956, 35: 1087, 36: 313, 37: 1146, 38: 454, 39: 1029, 40: 1021, 41: 741, 42: 1027, 43: 841, 44: 1126, 45: 700, 46: 488, 47: 0, 48: 1080, 49: 1224, 50: 416, 51: 349},
        48: {0: 1391, 1: 737, 2: 245, 3: 994, 4: 316, 5: 168, 6: 333, 7: 1285, 8: 465, 9: 857, 10: 275, 11: 810, 12: 90.6, 13: 891, 14: 144, 15: 727, 16: 400, 17: 849, 18: 644, 19: 638, 20: 1091, 21: 884, 22: 1275, 23: 446, 24: 97.1, 25: 1071, 26: 1348, 27: 365, 28: 507, 29: 564, 30: 1206, 31: 1144, 32: 818, 33: 106, 34: 403, 35: 11, 36: 1366, 37: 148, 38: 1553, 39: 354, 40: 78.1, 41: 437, 42: 778, 43: 244, 44: 79.4, 45: 589, 46: 726, 47: 1185, 48: 0, 49: 166, 50: 1514, 51: 735},
        49: {0: 1562, 1: 908, 2: 417, 3: 1145, 4: 467, 5: 182, 6: 416, 7: 1456, 8: 616, 9: 1008, 10: 299, 11: 834, 12: 77.1, 13: 1041, 14: 167, 15: 751, 16: 572, 17: 1020, 18: 714, 19: 809, 20: 1263, 21: 1055, 22: 1446, 23: 618, 24: 154, 25: 1243, 26: 1520, 27: 515, 28: 679, 29: 715, 30: 1378, 31: 1315, 32: 989, 33: 256, 34: 486, 35: 164, 36: 1537, 37: 75.9, 38: 1724, 39: 378, 40: 249, 41: 522, 42: 802, 43: 394, 44: 118, 45: 761, 46: 898, 47: 1357, 48: 166, 49: 0, 50: 1686, 51: 886},
        50: {0: 242, 1: 776, 2: 1265, 3: 978, 4: 1126, 5: 1390, 6: 1189, 7: 229, 8: 1000, 9: 1104, 10: 1414, 11: 1483, 12: 1616, 13: 546, 14: 1423, 15: 1400, 16: 1129, 17: 918, 18: 1230, 19: 895, 20: 424, 21: 629, 22: 367, 23: 1123, 24: 1393, 25: 439, 26: 230, 27: 1110, 28: 1016, 29: 875, 30: 312, 31: 381, 32: 712, 33: 1469, 34: 1321, 35: 1513, 36: 184, 37: 1511, 38: 41.1, 39: 1394, 40: 1450, 41: 1106, 42: 1392, 43: 1206, 44: 1591, 45: 1027, 46: 815, 47: 414, 48: 1521, 49: 1693, 50: 0, 51: 714},
        51: {0: 631, 1: 211, 2: 558, 3: 271, 4: 419, 5: 683, 6: 482, 7: 530, 8: 294, 9: 397, 10: 708, 11: 776, 12: 814, 13: 160, 14: 717, 15: 693, 16: 421, 17: 371, 18: 523, 19: 184, 20: 287, 21: 238, 22: 419, 23: 509, 24: 686, 25: 438, 26: 533, 27: 403, 28: 309, 29: 168, 30: 402, 31: 510, 32: 132, 33: 667, 34: 614, 35: 745, 36: 586, 37: 804, 38: 754, 39: 687, 40: 679, 41: 399, 42: 685, 43: 499, 44: 784, 45: 464, 46: 245, 47: 381, 48: 738, 49: 882, 50: 715, 51: 0}}

location_list = ['Przemysl', 'Kyiv', 'Kharkiv', 'Odesa', 'Dnipro', 
'Donetsk', 'Zaporizhzhia', 'Lviv', 'Kryvyi Rih', 'Mykolaiv', 
'Mariupol', 'Sevastopol', 'Luhansk', 'Vinnytsia', 'Makiivka', 
'Simferopol', 'Poltava', 'Chernihiv', 'Kherson', 'Cherkasy', 
'Khmelnytskyi', 'Zhytomyr', 'Chernivtsi', 'Sumy', 'Horlivka', 
'Rivne', 'Ivano-Frankivsk', 'Kamianske', 'Kremenchuk', 
'Kropyvnytskyi', 'Ternopil', 'Lutsk', 'Bila Tserkva', 'Kramatorsk', 
'Melitopol', 'Sievierodonetsk', 'Drohobych', 'Khrustalnyi', 'Uzhhorod', 
'Berdiansk', 'Sloviansk', 'Nikopol', 'Yevpatoriia', 'Pavlohrad', 
'Alchevsk', 'Konotop', 'Brovary', 'Kamianets-Podilskyi', 'Lysychansk', 
'Dovzhansk', 'Mukacheve', 'Uman']

def create_data_model():
    '''Stores the data for the problem.'''
    data = {}
    data['coord_locations'] = [
        (30.5236,50.45), (36.2292,50), (30.7326,46.4775), (34.9833,48.45), 
        (37.8042,48.0089), (35.1383,47.8378), (24.0315,49.8419), (33.3433,47.9086), 
        (32,46.9667), (37.5639,47.1306), (33.5333,44.6), (39.3333,48.5833), 
        (28.4672,49.2372), (37.9611,48.0556), (34.1,44.9484), (34.5686,49.5744), 
        (31.2947,51.4939), (32.6,46.6333), (32.0597,49.4444), (27,49.42), 
        (28.6578,50.2544), (25.9344,48.2908), (34.7992,50.9068), (38.0925,48.3336), 
        (26.2514,50.6197), (24.7106,48.9228), (34.6132,48.5076), (33.4239,49.0775), 
        (32.2667,48.5103), (25.6,49.5667), (25.3244,50.7478), (30.1167,49.7956), 
        (37.5556,48.7208), (35.3667,46.8333), (38.4833,48.95), (23.5,49.35), 
        (38.9453,48.1214), (22.295,48.6239), (36.7845,46.7598), (37.625,48.87), 
        (34.3575,47.5772), (33.3583,45.2), (35.87,48.52), (38.7983,48.4672), 
        (33.2027,51.2369), (30.7903,50.5114), (26.5806,48.6806), (38.4306,48.9169), 
        (39.6516,48.0846), (22.7136,48.4414)]
     # yapf: disable

    data['num_cities'] = 50
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def compute_distance_from_coord(lon1, lat1, lon2, lat2):
    R = 6371e3 # metres
    phi_1 = lat1 * math.pi/180 # φ, λ in radians
    phi_2 = lat2 * math.pi/180
    delt_phi = (lat2-lat1) * math.pi/180
    delt_lambda = (lon2-lon1) * math.pi/180

    a = math.sin(delt_phi/2) * math.sin(delt_phi/2) + math.cos(phi_1) * math.cos(phi_2) * math.sin(delt_lambda/2) * math.sin(delt_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = R * c # in metres

    return d


def create_distance_matrix_gmaps():
    '''Returns the pre-created dictionary of the Google Maps created on Google Sheets'''
    return gmaps2


def create_distance_matrix_euclidean(locations):
    '''Creates callback to return distance between points.'''
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                dist_between = compute_distance_from_coord(from_node[0], from_node[1], to_node[0], to_node[1])
                distances[from_counter][to_counter] = dist_between
    return distances


def print_solution(manager, routing, solution, names):
    '''Prints solution on console.'''
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(names[manager.IndexToNode(index)])
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(names[manager.IndexToNode(index)])
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def print_csv(manager, routing, solution, names):
    '''Prints solution on console.'''
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += '{}\n'.format(names[manager.IndexToNode(index)])
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(location_list),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # OLD: distance_matrix = create_distance_matrix_euclidean(data['coord_locations'])
    distance_matrix = create_distance_matrix_gmaps()

    def distance_callback(from_index, to_index):
        '''Returns the distance between the two nodes.'''
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    #EXPERIMENT - DEFAULT ROUTING SEARCH 

    #search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    #EXPERIMENT #1: default strategy, using path_cheapest_arc
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)'''
    #EXPERIMENT #2: using Clarke & Wright Savings algorithm
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.SAVINGS)'''
    #EXPERIMENT #3: using local search insertion
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.LOCAL_CHEAPEST_INSERTION)'''
    #EXPERIMENT #4: using all unperformed algorithm which makes all nodes inactive. 
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.ALL_UNPERFORMED)'''
    #EXPERIMENT #5: using automatic
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.AUTOMATIC)'''

    #EXPERIMENTs - LOCAL SEARCH
    
    #search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    #EXPERIMENT #6: local search algorithm with guided heuristic 
    '''search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.seconds = 30
    search_parameters.log_search = True'''

    #EXPERIMENT #7: local search algorithm witth simulated annealing
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.SIMULATED_ANNEALING)
    search_parameters.time_limit.seconds = 30
    search_parameters.log_search = True
    '''search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)'''

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution, location_list)

        # print_csv(manager, routing, solution, data['city_names'])


if __name__ == '__main__':
    main()