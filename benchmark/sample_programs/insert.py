class Node!1():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_right(self, v):
        if self.right == None:
            self.right = Node!1(v)
        else:
            self.right.insert(v)

    def insert_left(self, v):    
        if self.left == None:
            self.left = Node!1(v)
        else:
            self.left.insert(v)
        
    def insert(self, v):
        if(self.value <= v):
            self.insert_right(v)
        else:
            self.insert_left(v)
    
    def prity_print(self):
        result = ""
        if self.left != None:
            result = result + self.left.prity_print()
        result = result + str(self.value) + ", "
        if self.right != None:
            result = result + self.right.prity_print()
        return result


root = Node!1(5)
a = [8841, 1092, 5647, 4210, 7658, 5154, 3837, 1459, 1270, 3302, 1916, 5117, 4075, 4622, 9340, 599, 4271, 547, 4260, 2024, 2213, 378, 7940, 4064, 3650, 192, 5659, 4464, 5590, 1143, 1859, 6036, 5466, 1525, 7500, 1634, 7405, 2816, 5270, 3360, 1349, 9372, 5458, 3392, 8978, 9347, 7261, 5595, 1569, 1241, 7071, 997, 8822, 5605, 911, 9657, 8927, 5375, 2819, 4348, 2729, 6603, 906, 3730, 2576, 3375, 2011, 9622, 62, 5749, 2654, 2554, 4752, 246, 5504, 1127, 7625, 8636, 6802, 7050, 4238, 1852, 9765, 3040, 2555, 1427, 1085, 1676, 9232, 906, 8232, 5467, 5743, 9339, 9224, 3962, 3305, 6808, 2225, 1016, 7092, 631, 2082, 3612, 2544, 3318, 224, 6603, 8252, 2429, 8004, 8230, 1189, 8561, 6294, 9286, 6697, 3935, 4236, 5966, 6757, 1690, 8136, 3816, 5321, 6624, 5772, 425, 9292, 1247, 9699, 6005, 3379, 9101, 3501, 416, 7221, 3169, 7420, 5634, 4233, 7121, 4415, 9032, 6440, 1288, 9157, 3641, 2563, 8657, 5680, 1678, 7897, 9064, 1073, 2569, 448, 4079, 8407, 7610, 1786, 938, 8827, 8113, 9821, 5342, 4324, 4437, 1612, 252, 8278, 4307, 1316, 8943, 4034, 6060, 3110, 8743, 9541, 3387, 7129, 8443, 4743, 9205, 4694, 3947, 958, 7033, 8691, 8249, 6654, 5555, 6870, 1761, 4279, 6196, 3686, 2358, 9250, 4005, 1830, 6366, 928, 6361, 3511, 3910, 7553, 9693, 746, 2883, 6818, 8568, 8837, 5100, 7823, 1639, 5554, 4374, 3621, 8624, 5383, 8582, 9118, 816, 5656, 7580, 6418, 6719, 9496, 310, 5128, 123, 2082, 2252, 1564, 8070, 7499, 5128, 1812, 4327, 7658, 6802, 3645, 6072, 2204, 1307, 3621, 5940, 4760, 9008, 2125, 7138, 9170, 5162, 7378, 9912, 7859, 981, 6346, 3659, 3639, 1563, 9206, 1753, 7121, 8136, 9544, 7055, 2302, 9647, 4313, 8047, 7096, 7868, 3550, 1156, 1140, 8368, 8226, 6465, 4708, 8309, 6894, 1074, 5928, 4363, 1307, 537, 7894, 7039, 4977, 8821, 9637, 7594, 7069, 9013, 8734, 6495, 6214, 9665, 6908, 7497, 5617, 7186, 3550, 5379, 8882, 2733, 1669, 2364, 654, 4039, 2964, 5183, 7602, 3083, 475, 5724, 6933, 6250, 8012, 680, 6185, 760, 2910, 6717, 1890, 9204, 9767, 8821, 5927, 4314, 8963, 7120, 7390, 2859, 6697, 2469, 1869, 908, 1024, 3836, 7300, 4057, 5511, 851, 1306, 7824, 4366, 9738, 5905, 7568, 8827, 1725, 4973, 5947, 5822, 9962, 3490, 9441, 8677, 1517, 4114, 3591, 8305, 302, 2976, 9392, 3818, 949, 7859, 8035, 7745, 105, 6601, 6332, 9744, 9849, 9304, 3584, 9712, 894, 6824, 7562, 6972, 1003, 9572, 5654, 9796, 9739, 1247, 7412, 220, 2477, 1900, 2221, 7654, 7051, 7014, 7584, 861, 3124, 3866, 1543, 1615, 2988, 4315, 1624, 7560, 2892, 6411, 3183, 4526, 4112, 5652, 8184, 5617, 7176, 4577, 5229, 5201, 6292, 7751, 8980, 4528, 137, 7820, 9777, 1018, 9134, 1371, 7693, 1482, 3536, 1068, 8984, 3131, 6816, 9777, 7071, 9600, 253, 9282, 208, 3472, 7714, 1565, 610, 582, 1028, 4819, 5580, 7516, 5329, 775, 8822, 2328, 4865, 8212, 4770, 1100, 4935, 7108, 1224, 7725, 8920, 813, 746, 1773, 5813, 7639, 8549, 2950, 1980, 2420, 7757, 8290, 6746, 335, 2988, 6732, 1680, 5974, 5725, 5793, 4446, 4331, 6674, 2114, 9192, 1167, 2831, 1691, 5771, 4339, 5063, 8188, 7605, 8294, 1473, 273, 8206, 8559, 4836, 1950, 2045, 2905, 231, 2959, 9309, 4266, 8517, 68, 4714, 2869, 3778, 4368, 3703, 5001, 9515, 2498, 3802, 9515, 5758, 8008, 4327, 409, 3108, 9793, 2968, 7849, 4186, 463, 5662, 3494, 1618, 8297, 5362, 2338, 464, 2011, 8924, 9157, 1077, 5496, 2871, 3521, 8412, 8215, 9019, 2140, 5688, 2345, 8772, 9069, 5670, 352, 4309, 5341, 232, 5768, 3318, 4873, 2218, 1395, 5736, 9131, 9547, 3584, 4651, 6696, 8445, 8431, 7751, 1734, 3632, 5331, 9901, 4935, 7548, 909, 1637, 1095, 3257, 1474, 1792, 3735, 2909, 3393, 679, 7857, 7101, 3973, 7006, 861, 3954, 3784, 174, 7030, 8771, 8972, 9959, 1065, 5108, 5550, 9192, 8352, 8708, 4395, 4231, 3114, 8713, 2545, 877, 1004, 8214, 9390, 1717, 9617, 3557, 4597, 1521, 6898, 5845, 3642, 2208, 4904, 6499, 5326, 2805, 3028, 3531, 5330, 3679, 6770, 1508, 1865, 6801, 8600, 5651, 9103, 2911, 8008, 3593, 8624, 8080, 1929, 6638, 2291, 7645, 5062, 9368, 5627, 9741, 9588, 1346, 1130, 491, 9690, 5495, 7360, 6815, 1314, 5745, 2728, 2935, 8800, 5993, 6688, 2410, 5591, 4855, 2508, 2275, 9424, 215, 8171, 5969, 6202, 6657, 3482, 1755, 7087, 5904, 9960, 5227, 9450, 5454, 7697, 3853, 3600, 3342, 3770, 9789, 6893, 3691, 3044, 915, 4430, 5361, 1340, 542, 5147, 5035, 1943, 2422, 9553, 2998, 7153, 3591, 2408, 1480, 4172, 4131, 8761, 731, 7777, 4589, 7522, 2253, 6475, 4880, 6803, 7312, 2222, 7715, 3112, 3309, 8457, 9186, 1325, 7499, 5565, 8455, 1839, 9439, 7067, 7261, 5619, 1591, 8204, 8935, 6621, 7775, 6229, 8199, 2342, 8141, 2024, 3020, 8283, 5894, 2829, 6754, 5799, 8867, 938, 35, 1287, 7305, 3561, 5601, 6758, 1173, 9862, 5067, 4785, 4232, 9478, 9964, 2106, 3996, 9692, 9475, 8321, 8339, 8439, 255, 8452, 3703, 131, 722, 5527, 318, 1155, 1366, 8089, 436, 910, 6537, 246, 2958, 219, 540, 2114, 2643, 5326, 5403, 8705, 7114, 2500, 4770, 4419, 3560, 1723, 589, 1544, 6981, 695, 3183, 6021, 2597, 7535, 1463, 2442, 2915, 6965, 9010, 5303, 2467, 2639, 9214, 8277, 1481, 5839, 3831, 9907, 1514, 5412, 4911, 3988, 6131, 8942, 4965, 7758, 7457, 925, 9648, 2707, 8525, 6321, 3985, 6890, 9149, 3379, 2416, 9296, 5144, 2461, 2590, 1307, 5149, 4709, 8599, 8278, 2060, 5093, 5207, 8343, 834, 2109, 7237, 9958, 7158, 9878, 8313, 5555, 9256, 652, 9037, 9241, 6364, 2588, 5508, 7956, 4331, 7137, 6963, 125, 8719, 7427, 1035, 9079, 1091, 3418, 6541, 8079, 9808, 9654, 6147, 8243, 768, 3066, 5849, 2767, 5906, 4865, 7336, 6724, 8478, 3056, 9904, 9609, 7671, 1509, 8598, 1348, 8121, 5507, 8822, 8709, 6196, 715, 1380, 7420, 3042, 575, 8183, 4423, 1889, 2493, 412, 9297, 304, 9873, 1354, 8834, 2100, 9079, 7180, 2156, 6072, 2306, 5733, 2979, 870, 9795, 3354, 8566, 7544, 1321, 1046, 5529, 8172, 5042, 359, 2477, 9324, 9862, 1693, 6152, 9920, 8216, 3692, 981, 4758, 1825, 3459, 1083, 9499, 7727, 1198, 2574, 8445, 279, 1148, 7462, 8838, 8414, 2175, 6934, 4404, 6618, 7314, 316, 5982, 4297, 5596, 9128, 8997, 2566, 8244, 6124, 5823, 5652, 2790, 3774, 4898, 6086, 8643, 6682, 2792, 3885, 7557, 1994, 4750, 9419, 3067, 7132, 977]
for i in a:
    root.insert(i)
