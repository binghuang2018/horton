# -*- coding: utf-8 -*-
# HORTON: Helpful Open-source Research TOol for N-fermion systems.
# Copyright (C) 2011-2019 The HORTON Development Team
#
# This file is part of HORTON.
#
# HORTON is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# HORTON is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --


import numpy as np
from nose.tools import assert_raises

from horton import *  # pylint: disable=wildcard-import,unused-wildcard-import


def test_boys_functions():
    # reference data computed with sympy.mpmath arbitrary precision libraray
    result = np.array([
        boys_function(0,0.0e+00), boys_function(0,1.0e-20),
        boys_function(0,1.0e-10), boys_function(0,1.0e-07),
        boys_function(0,1.0e-05), boys_function(0,1.0e-02),
        boys_function(0,1.0e-01), boys_function(0,5.0e-01),
        boys_function(0,1.0e+00), boys_function(0,1.5e+00),
        boys_function(0,2.0e+00), boys_function(0,1.0e+01),
        boys_function(0,1.0e+02), boys_function(0,1.0e+05),
        boys_function(0,1.0e+10), boys_function(0,1.0e+20),
        boys_function(1,0.0e+00), boys_function(1,1.0e-20),
        boys_function(1,1.0e-10), boys_function(1,1.0e-07),
        boys_function(1,1.0e-05), boys_function(1,1.0e-02),
        boys_function(1,1.0e-01), boys_function(1,5.0e-01),
        boys_function(1,1.0e+00), boys_function(1,1.5e+00),
        boys_function(1,2.0e+00), boys_function(1,1.0e+01),
        boys_function(1,1.0e+02), boys_function(1,1.0e+05),
        boys_function(1,1.0e+10), boys_function(1,1.0e+20),
        boys_function(2,0.0e+00), boys_function(2,1.0e-20),
        boys_function(2,1.0e-10), boys_function(2,1.0e-07),
        boys_function(2,1.0e-05), boys_function(2,1.0e-02),
        boys_function(2,1.0e-01), boys_function(2,5.0e-01),
        boys_function(2,1.0e+00), boys_function(2,1.5e+00),
        boys_function(2,2.0e+00), boys_function(2,1.0e+01),
        boys_function(2,1.0e+02), boys_function(2,1.0e+05),
        boys_function(2,1.0e+10), boys_function(2,1.0e+20),
        boys_function(3,0.0e+00), boys_function(3,1.0e-20),
        boys_function(3,1.0e-10), boys_function(3,1.0e-07),
        boys_function(3,1.0e-05), boys_function(3,1.0e-02),
        boys_function(3,1.0e-01), boys_function(3,5.0e-01),
        boys_function(3,1.0e+00), boys_function(3,1.5e+00),
        boys_function(3,2.0e+00), boys_function(3,1.0e+01),
        boys_function(3,1.0e+02), boys_function(3,1.0e+05),
        boys_function(3,1.0e+10), boys_function(3,1.0e+20),
        boys_function(4,0.0e+00), boys_function(4,1.0e-20),
        boys_function(4,1.0e-10), boys_function(4,1.0e-07),
        boys_function(4,1.0e-05), boys_function(4,1.0e-02),
        boys_function(4,1.0e-01), boys_function(4,5.0e-01),
        boys_function(4,1.0e+00), boys_function(4,1.5e+00),
        boys_function(4,2.0e+00), boys_function(4,1.0e+01),
        boys_function(4,1.0e+02), boys_function(4,1.0e+05),
        boys_function(4,1.0e+10), boys_function(4,1.0e+20),
        boys_function(5,0.0e+00), boys_function(5,1.0e-20),
        boys_function(5,1.0e-10), boys_function(5,1.0e-07),
        boys_function(5,1.0e-05), boys_function(5,1.0e-02),
        boys_function(5,1.0e-01), boys_function(5,5.0e-01),
        boys_function(5,1.0e+00), boys_function(5,1.5e+00),
        boys_function(5,2.0e+00), boys_function(5,1.0e+01),
        boys_function(5,1.0e+02), boys_function(5,1.0e+05),
        boys_function(5,1.0e+10), boys_function(5,1.0e+20),
        boys_function(6,0.0e+00), boys_function(6,1.0e-20),
        boys_function(6,1.0e-10), boys_function(6,1.0e-07),
        boys_function(6,1.0e-05), boys_function(6,1.0e-02),
        boys_function(6,1.0e-01), boys_function(6,5.0e-01),
        boys_function(6,1.0e+00), boys_function(6,1.5e+00),
        boys_function(6,2.0e+00), boys_function(6,1.0e+01),
        boys_function(6,1.0e+02), boys_function(6,1.0e+05),
        boys_function(6,1.0e+10), boys_function(6,1.0e+20),
        boys_function(7,0.0e+00), boys_function(7,1.0e-20),
        boys_function(7,1.0e-10), boys_function(7,1.0e-07),
        boys_function(7,1.0e-05), boys_function(7,1.0e-02),
        boys_function(7,1.0e-01), boys_function(7,5.0e-01),
        boys_function(7,1.0e+00), boys_function(7,1.5e+00),
        boys_function(7,2.0e+00), boys_function(7,1.0e+01),
        boys_function(7,1.0e+02), boys_function(7,1.0e+05),
        boys_function(7,1.0e+10), boys_function(7,1.0e+20),
        boys_function(8,0.0e+00), boys_function(8,1.0e-20),
        boys_function(8,1.0e-10), boys_function(8,1.0e-07),
        boys_function(8,1.0e-05), boys_function(8,1.0e-02),
        boys_function(8,1.0e-01), boys_function(8,5.0e-01),
        boys_function(8,1.0e+00), boys_function(8,1.5e+00),
        boys_function(8,2.0e+00), boys_function(8,1.0e+01),
        boys_function(8,1.0e+02), boys_function(8,1.0e+05),
        boys_function(8,1.0e+10), boys_function(8,1.0e+20),
        boys_function(9,0.0e+00), boys_function(9,1.0e-20),
        boys_function(9,1.0e-10), boys_function(9,1.0e-07),
        boys_function(9,1.0e-05), boys_function(9,1.0e-02),
        boys_function(9,1.0e-01), boys_function(9,5.0e-01),
        boys_function(9,1.0e+00), boys_function(9,1.5e+00),
        boys_function(9,2.0e+00), boys_function(9,1.0e+01),
        boys_function(9,1.0e+02), boys_function(9,1.0e+05),
        boys_function(9,1.0e+10), boys_function(9,1.0e+20),
        boys_function(10,0.0e+00), boys_function(10,1.0e-20),
        boys_function(10,1.0e-10), boys_function(10,1.0e-07),
        boys_function(10,1.0e-05), boys_function(10,1.0e-02),
        boys_function(10,1.0e-01), boys_function(10,5.0e-01),
        boys_function(10,1.0e+00), boys_function(10,1.5e+00),
        boys_function(10,2.0e+00), boys_function(10,1.0e+01),
        boys_function(10,1.0e+02), boys_function(10,1.0e+05),
        boys_function(10,1.0e+10), boys_function(10,1.0e+20),
        boys_function(11,0.0e+00), boys_function(11,1.0e-20),
        boys_function(11,1.0e-10), boys_function(11,1.0e-07),
        boys_function(11,1.0e-05), boys_function(11,1.0e-02),
        boys_function(11,1.0e-01), boys_function(11,5.0e-01),
        boys_function(11,1.0e+00), boys_function(11,1.5e+00),
        boys_function(11,2.0e+00), boys_function(11,1.0e+01),
        boys_function(11,1.0e+02), boys_function(11,1.0e+05),
        boys_function(11,1.0e+10), boys_function(11,1.0e+20),
        boys_function(12,0.0e+00), boys_function(12,1.0e-20),
        boys_function(12,1.0e-10), boys_function(12,1.0e-07),
        boys_function(12,1.0e-05), boys_function(12,1.0e-02),
        boys_function(12,1.0e-01), boys_function(12,5.0e-01),
        boys_function(12,1.0e+00), boys_function(12,1.5e+00),
        boys_function(12,2.0e+00), boys_function(12,1.0e+01),
        boys_function(12,1.0e+02), boys_function(12,1.0e+05),
        boys_function(12,1.0e+10), boys_function(12,1.0e+20),
        boys_function(13,0.0e+00), boys_function(13,1.0e-20),
        boys_function(13,1.0e-10), boys_function(13,1.0e-07),
        boys_function(13,1.0e-05), boys_function(13,1.0e-02),
        boys_function(13,1.0e-01), boys_function(13,5.0e-01),
        boys_function(13,1.0e+00), boys_function(13,1.5e+00),
        boys_function(13,2.0e+00), boys_function(13,1.0e+01),
        boys_function(13,1.0e+02), boys_function(13,1.0e+05),
        boys_function(13,1.0e+10), boys_function(13,1.0e+20),
        boys_function(14,0.0e+00), boys_function(14,1.0e-20),
        boys_function(14,1.0e-10), boys_function(14,1.0e-07),
        boys_function(14,1.0e-05), boys_function(14,1.0e-02),
        boys_function(14,1.0e-01), boys_function(14,5.0e-01),
        boys_function(14,1.0e+00), boys_function(14,1.5e+00),
        boys_function(14,2.0e+00), boys_function(14,1.0e+01),
        boys_function(14,1.0e+02), boys_function(14,1.0e+05),
        boys_function(14,1.0e+10), boys_function(14,1.0e+20),
        boys_function(15,0.0e+00), boys_function(15,1.0e-20),
        boys_function(15,1.0e-10), boys_function(15,1.0e-07),
        boys_function(15,1.0e-05), boys_function(15,1.0e-02),
        boys_function(15,1.0e-01), boys_function(15,5.0e-01),
        boys_function(15,1.0e+00), boys_function(15,1.5e+00),
        boys_function(15,2.0e+00), boys_function(15,1.0e+01),
        boys_function(15,1.0e+02), boys_function(15,1.0e+05),
        boys_function(15,1.0e+10), boys_function(15,1.0e+20),
        boys_function(16,0.0e+00), boys_function(16,1.0e-20),
        boys_function(16,1.0e-10), boys_function(16,1.0e-07),
        boys_function(16,1.0e-05), boys_function(16,1.0e-02),
        boys_function(16,1.0e-01), boys_function(16,5.0e-01),
        boys_function(16,1.0e+00), boys_function(16,1.5e+00),
        boys_function(16,2.0e+00), boys_function(16,1.0e+01),
        boys_function(16,1.0e+02), boys_function(16,1.0e+05),
        boys_function(16,1.0e+10), boys_function(16,1.0e+20),
        boys_function(17,0.0e+00), boys_function(17,1.0e-20),
        boys_function(17,1.0e-10), boys_function(17,1.0e-07),
        boys_function(17,1.0e-05), boys_function(17,1.0e-02),
        boys_function(17,1.0e-01), boys_function(17,5.0e-01),
        boys_function(17,1.0e+00), boys_function(17,1.5e+00),
        boys_function(17,2.0e+00), boys_function(17,1.0e+01),
        boys_function(17,1.0e+02), boys_function(17,1.0e+05),
        boys_function(17,1.0e+10), boys_function(17,1.0e+20),
        boys_function(18,0.0e+00), boys_function(18,1.0e-20),
        boys_function(18,1.0e-10), boys_function(18,1.0e-07),
        boys_function(18,1.0e-05), boys_function(18,1.0e-02),
        boys_function(18,1.0e-01), boys_function(18,5.0e-01),
        boys_function(18,1.0e+00), boys_function(18,1.5e+00),
        boys_function(18,2.0e+00), boys_function(18,1.0e+01),
        boys_function(18,1.0e+02), boys_function(18,1.0e+05),
        boys_function(18,1.0e+10), boys_function(18,1.0e+20),
        boys_function(19,0.0e+00), boys_function(19,1.0e-20),
        boys_function(19,1.0e-10), boys_function(19,1.0e-07),
        boys_function(19,1.0e-05), boys_function(19,1.0e-02),
        boys_function(19,1.0e-01), boys_function(19,5.0e-01),
        boys_function(19,1.0e+00), boys_function(19,1.5e+00),
        boys_function(19,2.0e+00), boys_function(19,1.0e+01),
        boys_function(19,1.0e+02), boys_function(19,1.0e+05),
        boys_function(19,1.0e+10), boys_function(19,1.0e+20),
        boys_function(20,0.0e+00), boys_function(20,1.0e-20),
        boys_function(20,1.0e-10), boys_function(20,1.0e-07),
        boys_function(20,1.0e-05), boys_function(20,1.0e-02),
        boys_function(20,1.0e-01), boys_function(20,5.0e-01),
        boys_function(20,1.0e+00), boys_function(20,1.5e+00),
        boys_function(20,2.0e+00), boys_function(20,1.0e+01),
        boys_function(20,1.0e+02), boys_function(20,1.0e+05),
        boys_function(20,1.0e+10), boys_function(20,1.0e+20),
        boys_function(21,0.0e+00), boys_function(21,1.0e-20),
        boys_function(21,1.0e-10), boys_function(21,1.0e-07),
        boys_function(21,1.0e-05), boys_function(21,1.0e-02),
        boys_function(21,1.0e-01), boys_function(21,5.0e-01),
        boys_function(21,1.0e+00), boys_function(21,1.5e+00),
        boys_function(21,2.0e+00), boys_function(21,1.0e+01),
        boys_function(21,1.0e+02), boys_function(21,1.0e+05),
        boys_function(21,1.0e+10), boys_function(21,1.0e+20),
        boys_function(22,0.0e+00), boys_function(22,1.0e-20),
        boys_function(22,1.0e-10), boys_function(22,1.0e-07),
        boys_function(22,1.0e-05), boys_function(22,1.0e-02),
        boys_function(22,1.0e-01), boys_function(22,5.0e-01),
        boys_function(22,1.0e+00), boys_function(22,1.5e+00),
        boys_function(22,2.0e+00), boys_function(22,1.0e+01),
        boys_function(22,1.0e+02), boys_function(22,1.0e+05),
        boys_function(22,1.0e+10), boys_function(22,1.0e+20),
        boys_function(23,0.0e+00), boys_function(23,1.0e-20),
        boys_function(23,1.0e-10), boys_function(23,1.0e-07),
        boys_function(23,1.0e-05), boys_function(23,1.0e-02),
        boys_function(23,1.0e-01), boys_function(23,5.0e-01),
        boys_function(23,1.0e+00), boys_function(23,1.5e+00),
        boys_function(23,2.0e+00), boys_function(23,1.0e+01),
        boys_function(23,1.0e+02), boys_function(23,1.0e+05),
        boys_function(23,1.0e+10), boys_function(23,1.0e+20),
        boys_function(24,0.0e+00), boys_function(24,1.0e-20),
        boys_function(24,1.0e-10), boys_function(24,1.0e-07),
        boys_function(24,1.0e-05), boys_function(24,1.0e-02),
        boys_function(24,1.0e-01), boys_function(24,5.0e-01),
        boys_function(24,1.0e+00), boys_function(24,1.5e+00),
        boys_function(24,2.0e+00), boys_function(24,1.0e+01),
        boys_function(24,1.0e+02), boys_function(24,1.0e+05),
        boys_function(24,1.0e+10), boys_function(24,1.0e+20),
        boys_function(25,0.0e+00), boys_function(25,1.0e-20),
        boys_function(25,1.0e-10), boys_function(25,1.0e-07),
        boys_function(25,1.0e-05), boys_function(25,1.0e-02),
        boys_function(25,1.0e-01), boys_function(25,5.0e-01),
        boys_function(25,1.0e+00), boys_function(25,1.5e+00),
        boys_function(25,2.0e+00), boys_function(25,1.0e+01),
        boys_function(25,1.0e+02), boys_function(25,1.0e+05),
        boys_function(25,1.0e+10), boys_function(25,1.0e+20),
        boys_function(26,0.0e+00), boys_function(26,1.0e-20),
        boys_function(26,1.0e-10), boys_function(26,1.0e-07),
        boys_function(26,1.0e-05), boys_function(26,1.0e-02),
        boys_function(26,1.0e-01), boys_function(26,5.0e-01),
        boys_function(26,1.0e+00), boys_function(26,1.5e+00),
        boys_function(26,2.0e+00), boys_function(26,1.0e+01),
        boys_function(26,1.0e+02), boys_function(26,1.0e+05),
        boys_function(26,1.0e+10), boys_function(26,1.0e+20),
        boys_function(27,0.0e+00), boys_function(27,1.0e-20),
        boys_function(27,1.0e-10), boys_function(27,1.0e-07),
        boys_function(27,1.0e-05), boys_function(27,1.0e-02),
        boys_function(27,1.0e-01), boys_function(27,5.0e-01),
        boys_function(27,1.0e+00), boys_function(27,1.5e+00),
        boys_function(27,2.0e+00), boys_function(27,1.0e+01),
        boys_function(27,1.0e+02), boys_function(27,1.0e+05),
        boys_function(27,1.0e+10), boys_function(27,1.0e+20),
        boys_function(28,0.0e+00), boys_function(28,1.0e-20),
        boys_function(28,1.0e-10), boys_function(28,1.0e-07),
        boys_function(28,1.0e-05), boys_function(28,1.0e-02),
        boys_function(28,1.0e-01), boys_function(28,5.0e-01),
        boys_function(28,1.0e+00), boys_function(28,1.5e+00),
        boys_function(28,2.0e+00), boys_function(28,1.0e+01),
        boys_function(28,1.0e+02), boys_function(28,1.0e+05),
        boys_function(28,1.0e+10), boys_function(28,1.0e+20)])
    check = np.array([
        1.0000000000000000000, 1.0000000000000000000, 9.9999999996666666667e-1,
        9.9999996666666766667e-1, 9.9999666667666664286e-1,
        9.9667664290336350257e-1, 9.6764331263559183101e-1,
        8.5562439189214880317e-1, 7.4682413281242702540e-1,
        6.6335094584033480566e-1, 5.9814400666130410147e-1,
        2.8024739050664274064e-1, 8.8622692545275801365e-2,
        2.8024956081989643497e-3, 8.8622692545275801365e-6,
        8.8622692545275801365e-11, 3.3333333333333333333e-1,
        3.3333333333333333333e-1, 3.3333333331333333333e-1,
        3.3333331333333404762e-1, 3.3333133334047617196e-1,
        3.3134045770977244975e-1, 3.1402947299816128923e-1,
        2.4909373217951537957e-1, 1.8947234582049235190e-1,
        1.4674026189730165891e-1, 1.1570218085617285239e-1,
        1.4010099528844012789e-2, 4.4311346272637900682e-4,
        1.4012478040994821748e-8, 4.4311346272637900682e-16,
        4.4311346272637900682e-31, 2.0000000000000000000e-1,
        2.0000000000000000000e-1, 1.9999999998571428571e-1,
        1.9999998571428626984e-1, 1.9999857143412696898e-1,
        1.9857696900746478356e-1, 1.8625500479262147256e-1,
        1.4075053682591271510e-1, 1.0026879814501736706e-1,
        7.2363541847825049265e-2, 5.2942814832976466321e-2,
        2.0992449328384776758e-3, 6.6467019408956851024e-6,
        2.1018717061492232622e-13, 6.6467019408956851024e-26,
        6.6467019408956851024e-51, 1.4285714285714285714e-1,
        1.4285714285714285714e-1, 1.4285714284603174603e-1,
        1.4285713174603220058e-1, 1.4285603175057718776e-1,
        1.4175056440779321124e-1, 1.3218802963573894813e-1,
        9.7222024416930151920e-2, 6.6732274776822256840e-2,
        4.6229183030231805798e-2, 3.2344697732067409928e-2,
        5.2254123672149517637e-4, 1.6616754852239212756e-7,
        5.2546792653730581556e-18, 1.6616754852239212756e-35,
        1.6616754852239212756e-70, 1.1111111111111111111e-1,
        1.1111111111111111111e-1, 1.1111111110202020202e-1,
        1.1111110202020240482e-1, 1.1111020202404816294e-1,
        1.1020585526922125508e-1, 1.0239394707106531886e-1,
        7.4023511205877639835e-2, 4.9623241133156738143e-2,
        3.3491373687730937217e-2, 2.2769400221964794400e-2,
        1.8061943636439906915e-4, 5.8158641982837244646e-9,
        1.8391377428805703545e-22, 5.8158641982837244646e-45,
        5.8158641982837244646e-90, 9.0909090909090909091e-2,
        9.0909090909090909090e-2, 9.0909090901398601399e-2,
        9.0909083216783550117e-2, 9.0908321681655001851e-2,
        9.0143183691162106895e-2, 8.3540528018141482712e-2,
        5.9680941140265334908e-2, 3.9364864513484160846e-2,
        2.6097401013716202008e-2, 1.7397329690267614428e-2,
        7.9008749875855338543e-5, 2.6171388892276760091e-10,
        8.2761198429625665951e-27, 2.6171388892276760091e-54,
        2.6171388892276760091e-109, 7.6923076923076923077e-2,
        7.6923076923076923076e-2, 7.6923076916410256411e-2,
        7.6923070256410550528e-2, 7.6922410259351424109e-2,
        7.6259342680756113524e-2, 7.0541950817983683352e-2,
        4.9959692830285260385e-2, 3.2567034238441723855e-2,
        2.1313750334149464385e-2, 1.4008835839082766702e-2,
        4.1184815943596193622e-5, 1.4394263890752218050e-11,
        4.5518659136294116273e-31, 1.4394263890752218050e-63,
        1.4394263890752218050e-128, 6.6666666666666666667e-2,
        6.6666666666666666666e-2, 6.6666666660784313726e-2,
        6.6666660784313988648e-2, 6.6666078434004120030e-2,
        6.6081055033071111589e-2, 6.1039712989141552054e-2,
        4.2945347081074961403e-2, 2.7746001964150044258e-2,
        1.7982864731837736023e-2, 1.1694895667865818809e-2,
        2.4500133875213283277e-5, 9.3562715289889417324e-13,
        2.9587128438591175577e-35, 9.3562715289889417324e-73,
        9.3562715289889417324e-148, 5.8823529411764705882e-2,
        5.8823529411764705882e-2, 5.8823529406501547988e-2,
        5.8823524148607049241e-2, 5.8823003098356177333e-2,
        5.8299587344931012757e-2, 5.3791384005818538229e-2,
        3.7649546503490997443e-2, 2.4155294145404171134e-2,
        1.5537603609712070468e-2, 1.0022037945343647562e-2,
        1.6105103918285719881e-5, 7.0172036467417062993e-14,
        2.2190346328943381683e-39, 7.0172036467417062993e-82,
        7.0172036467417062993e-167, 5.2631578947368421053e-2,
        5.2631578947368421052e-2, 5.2631578942606516291e-2,
        5.2631574185463876539e-2, 5.2631102759066136953e-2,
        5.2157555732958164332e-2, 4.8080550314777883670e-2,
        3.3511630846713532924e-2, 2.1380279650214293844e-2,
        1.3669700405558456342e-2, 8.7598404585573291634e-3,
        1.1419341842418619322e-5, 5.9646230997304503544e-15,
        1.8861794379601874431e-43, 5.9646230997304503544e-91,
        5.9646230997304503544e-186, 4.7619047619047619048e-2,
        4.7619047619047619047e-2, 4.7619047614699792961e-2,
        4.7619043271221732091e-2, 4.7618612838438917223e-2,
        4.7186258851853437103e-2, 4.3465189724101082800e-2,
        3.0190326374923701953e-2, 1.9172936091314630718e-2,
        1.2198049185726947187e-2, 7.7754213689941405525e-3,
        8.5783782621734457793e-6, 5.6663919447439278367e-16,
        1.7918704660621780709e-47, 5.6663919447439278367e-100,
        5.6663919447439278367e-205, 4.3478260869565217391e-2,
        4.3478260869565217391e-2, 4.3478260865565217391e-2,
        4.3478256869565402576e-2, 4.3477860871417063496e-2,
        4.3080106987706279780e-2, 3.9657830850815828202e-2,
        2.7466194160764317408e-2, 1.7376108373082461737e-2,
        1.1009624250612020668e-2, 6.9871413780660649274e-3,
        6.7373006871578754915e-6, 5.9497115419811242285e-17,
        1.8814639893652869745e-51, 5.9497115419811242285e-109,
        5.9497115419811242285e-224, 4.0000000000000000000e-2,
        4.0000000000000000000e-2, 3.9999999996296296296e-2,
        3.9999996296296468710e-2, 3.9999629631353762184e-2,
        3.9631348403819068680e-2, 3.6463457664022377457e-2,
        2.5191805984945876777e-2, 1.5885525704727149183e-2,
        1.0030399205215548810e-2, 6.3422421147267003590e-3,
        5.4778993021073142385e-6, 6.8421682732782928628e-18,
        2.1636835877700800206e-55, 6.8421682732782928628e-118,
        6.8421682732782928628e-243, 3.7037037037037037037e-2,
        3.7037037037037037037e-2, 3.7037037033588761175e-2,
        3.7037033588761336258e-2, 3.7036692211063728316e-2,
        3.6693817315433171378e-2, 3.3745117822999316353e-2,
        2.3264489911013495831e-2, 1.4629350723368203987e-2,
        9.2099399939862971041e-3, 5.8051924078887042700e-3,
        4.5773776395099002213e-6, 8.5527103415978660785e-19,
        2.7046044847126000258e-59, 8.5527103415978660785e-127,
        8.5527103415978660785e-262, 3.4482758620689655172e-2,
        3.4482758620689655172e-2, 3.4482758617463848721e-2,
        3.4482755394883355075e-2, 3.4482436041559640635e-2,
        3.4161688376378682029e-2, 3.1403815925109841822e-2,
        2.1610567884730963843e-2, 1.3556514179749593031e-2,
        8.5127398964000642924e-3, 5.3512279440955808488e-3,
        3.9094633252141227220e-6, 1.1546158961157119206e-19,
        3.6512160543620100348e-63, 1.1546158961157119206e-135,
        1.1546158961157119206e-280, 3.2258064516129032258e-2,
        3.2258064516129032258e-2, 3.2258064513098729228e-2,
        3.2258061485826144812e-2, 3.2257761487254568879e-2,
        3.1956458290686263888e-2, 2.9366218961129198435e-2,
        2.0175808944564527830e-2, 1.2629735020647938149e-2,
        7.9130989490573451819e-3, 4.9625817855397881807e-3,
        3.3987253334362353701e-6, 1.6741930493677822849e-20,
        5.2942632788249145505e-67, 1.6741930493677822849e-144,
        1.6741930493677822849e-299, 3.0303030303030303030e-2,
        3.0303030303030303030e-2, 3.0303030300173160173e-2,
        3.0303027445887581023e-2, 3.0302744590095935822e-2,
        3.0018663105306347766e-2, 2.7576848795227891671e-2,
        1.8919417568866939139e-2, 1.1821172234321880515e-2,
        7.3919690907826239024e-3, 4.6261880287801854266e-3,
        2.9980277787019222468e-6, 2.5949992265200625415e-21,
        8.2061080821786175532e-71, 2.5949992265200625415e-153,
        2.5949992265200625415e-318, 2.8571428571428571429e-2,
        2.8571428571428571428e-2, 2.8571428568725868726e-2,
        2.8571425868725996931e-2, 2.8571158302440348375e-2,
        2.8302436297071135506e-2, 2.5992961032804259884e-2,
        1.7810120059975567988e-2, 1.1109621280589867692e-2,
        6.9349399491322532817e-3, 4.3322304282833567961e-3,
        2.6767493467339291305e-6, 4.2817487237581031935e-22,
        1.3540078335594718963e-74, 4.2817487237581031935e-162,
        4.2817487237581031935e-337, 2.7027027027027027027e-2,
        2.7027027027027027027e-2, 2.7027027024462924463e-2,
        2.7027024462924584876e-2, 2.7026770617990125090e-2,
        2.6771832416084457389e-2, 2.4581090560947613802e-2,
        1.6823542386511455959e-2, 1.0478651824601523812e-2,
        6.5309126903996786420e-3, 4.0731954383261989926e-3,
        2.4143148686601334016e-6, 7.4930602665766805887e-23,
        2.3695137087290758185e-78, 7.4930602665766805887e-171,
        7.4930602665766805887e-356, 2.5641025641025641026e-2,
        2.5641025641025641025e-2, 2.5641025638586616636e-2,
        2.5641023202001367061e-2, 2.5640781739749403629e-2,
        2.5398282297843490117e-2, 2.3314663595510687521e-2,
        1.5940408588290446897e-2, 9.9153381694070297198e-3,
        6.1712031321194269398e-3, 3.8432369953641677081e-3,
        2.1964860188970042161e-6, 1.3862161493166859089e-23,
        4.3836003611487902642e-82, 1.3862161493166859089e-179,
        1.3862161493166859089e-374, 2.4390243902439024390e-2,
        2.4390243902439024390e-2, 2.4390243900113442995e-2,
        2.4390241576857740153e-2, 2.4390011345410597072e-2,
        2.4158793336403048661e-2, 2.2172310944786200757e-2,
        1.5145275230694005365e-2, 9.4093737177159187385e-3,
        5.8489206680759405733e-3, 3.6377398956474621805e-3,
        2.0131512487249156447e-6, 2.7031214911675375224e-24,
        8.5480207042401410152e-86, 2.7031214911675375224e-188,
        2.7031214911675375224e-393, 2.3255813953488372093e-2,
        2.3255813953488372093e-2, 2.3255813951266149871e-2,
        2.3255811731266256254e-2, 2.3255591732329976257e-2,
        2.3034652167847076284e-2, 2.1136653501373289358e-2,
        1.4425624745820796361e-2, 8.9524406274551733420e-3,
        5.5585290808945781911e-3, 3.4530131212333143763e-3,
        1.8569635717618344948e-6, 5.5413990568934519209e-25,
        1.7523442443692289081e-89, 5.5413990568934519209e-197,
        5.5413990568934519209e-412, 2.2222222222222222222e-2,
        2.2222222222222222222e-2, 2.2222222220094562648e-2,
        2.2222220094562749795e-2, 2.2222009457285180309e-2,
        2.2010473412811330846e-2, 2.0193412615459346222e-2,
        1.3771204357660819926e-2, 8.5377529045650660557e-3,
        5.2955301100123444283e-3, 3.2860702441049565713e-3,
        1.7224751911637015871e-6, 1.1914007972320921630e-25,
        3.7675401253938421524e-93, 1.1914007972320921630e-205,
        1.1914007972320921630e-430, 2.1276595744680851064e-2,
        2.1276595744680851064e-2, 2.1276595742640034737e-2,
        2.1276593703864622572e-2, 2.1276391664028587015e-2,
        2.1073491367091725735e-2, 1.9330748298555034192e-2,
        1.3173536382103473062e-2, 8.1597197669928254560e-3,
        5.0562316007085567799e-3, 3.1344694370275884539e-3,
        1.6055726919940859941e-6, 2.6806517937722073667e-26,
        8.4769652821361448430e-97, 2.6806517937722073667e-214,
        2.6806517937722073667e-449, 2.0408163265306122449e-2,
        2.0408163265306122449e-2, 2.0408163263345338135e-2,
        2.0408161304521903063e-2, 2.0407967187818143096e-2,
        2.0213025207152798185e-2, 1.8538759980635169217e-2,
        1.2625550246229810319e-2, 7.8136939386102374180e-3,
        4.8375750282907799067e-3, 2.9961950759209913599e-3,
        1.5030993380618595094e-6, 6.2995317153646873115e-27,
        1.9920868413019940381e-100, 6.2995317153646873118e-223,
        6.2995317153646873118e-468, 1.9607843137254901961e-2,
        1.9607843137254901961e-2, 1.9607843135368109508e-2,
        1.9607841250462540040e-2, 1.9607654458918706927e-2,
        1.9420070065952873521e-2, 1.7809105075818592281e-2,
        1.2121302352627282037e-2, 7.4957809102296559431e-3,
        4.6370054126061288324e-3, 2.8695688708789711856e-3,
        1.4125968901273132212e-6, 1.5433852702643483911e-27,
        4.8806127611898853934e-104, 1.5433852702643483914e-231,
        1.5433852702643483914e-486, 1.8867924528301886792e-2,
        1.8867924528301886792e-2, 1.8867924526483704974e-2,
        1.8867922710120156330e-2, 1.8867742710997258768e-2,
        1.8686980721424798970e-2, 1.7134704153943165715e-2,
        1.1655760271357960264e-2, 7.2026926251350657504e-3,
        4.4523719648275805070e-3, 2.7531822945537096434e-3,
        1.3321255817004061373e-6, 3.9356324391740883955e-28,
        1.2445562541034207753e-107, 3.9356324391740883980e-240,
        3.9356324391740883980e-505, 1.8181818181818181818e-2,
        1.8181818181818181818e-2, 1.8181818180063795853e-2,
        1.8181816427432301652e-2, 1.8181642744069145485e-2,
        1.8007224317314592036e-2, 1.6509510615141048637e-2,
        1.1224634669338470378e-2, 6.9316339803580815877e-3,
        4.2818513291439793121e-3, 2.6458445936834798010e-3,
        1.2601363033818336872e-6, 1.0429425963811334230e-28,
        3.2980740733740650546e-111, 1.0429425963811334255e-248,
        1.0429425963811334255e-523, 1.7543859649122807018e-2,
        1.7543859649122807017e-2, 1.7543859647427891763e-2,
        1.7543857954207634747e-2, 1.7543690158417052774e-2,
        1.7375185156725418943e-2, 1.5928328983990509433e-2,
        1.0824247100982447194e-2, 6.6802138741260828643e-3,
        4.1238876514963444098e-3, 2.5465423539946742906e-3,
        1.1953783461758000630e-6, 2.8680921400481168945e-29,
        9.0697037017786789000e-115, 2.8680921400481169201e-257,
        2.8680921400481169201e-542])

    # relative errors for the bigger ones
    big_mask = abs(check) > 1e-10
    errors = (result[big_mask] - check[big_mask])/check[big_mask]
    max_error = abs(errors).max()
    rms_error = np.sqrt((errors**2).mean())
    assert max_error < 1e-15
    assert rms_error < 1e-15

    # absolute errors for the smaller ones
    small_mask = abs(check) > 1e-10
    errors = result[small_mask] - check[small_mask]
    max_error = abs(errors).max()
    rms_error = np.sqrt((errors**2).mean())
    assert max_error < 1e-16
    assert rms_error < 1e-16


def test_boys_domain_error():
    for m, t in (-1, 0.0), (get_max_shell_type()*4+1, 0.0), (5, -1):
        with assert_raises(ValueError):
            boys_function(m, t)


def test_boys_array():
    for mmax in range(get_max_shell_type()*4+1):
        for t in np.random.uniform(0, 200, 500):
            output = boys_function_array(mmax, t)
            for m in range(mmax+1):
                assert output[m] == boys_function(m, t)
