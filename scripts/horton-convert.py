#!/usr/bin/env python
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


import sys, argparse, os, numpy as np

from horton import __version__, IOData


# All, except underflows, is *not* fine.
np.seterr(divide='raise', over='raise', invalid='raise')


def parse_args():
    parser = argparse.ArgumentParser(prog='horton-convert.py',
        description='Convert between file formats supported in HORTON. This '
                    'only works of the input contains sufficient data for the '
                    'output')
    parser.add_argument('-V', '--version', action='version',
        version="%%(prog)s (HORTON version %s)" % __version__)

    parser.add_argument('input',
        help='The input file. Supported file types are: '
             '*.h5 (HORTON\'s native format), '
             '*.cif (Crystallographic Information File), '
             '*.cp2k.out (Output from a CP2K atom computation), '
             '*.cube (Gaussian cube file), '
             '*.log (Gaussian log file), '
             '*.fchk (Gaussian formatted checkpoint file), '
             '*.molden.input (Molden wavefunction file), '
             '*.mkl (Molekel wavefunction file), '
             '*.wfn (Gaussian/GAMESS wavefunction file), '
             'CHGCAR, LOCPOT or POSCAR (VASP files), '
             '*.xyz (The XYZ format).')
    parser.add_argument('output',
        help='The output file. Supported file types are: '
             '*.h5 (HORTON\'s native format), '
             '*.cif (Crystallographic Information File), '
             '*.cube (Gaussian cube file), '
             '*.molden.input (Molden wavefunction file), '
             'POSCAR (VASP files), '
             '*.xyz (The XYZ format).')

    return parser.parse_args()


def main():
    args = parse_args()
    mol = IOData.from_file(args.input)
    mol.to_file(args.output)


if __name__ == '__main__':
    main()
