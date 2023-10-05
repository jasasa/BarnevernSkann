# Copyright (C) 2023 Bergen Kommune
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--name', 'BKModulusScan',
    '--onefile',
    '--clean',
    '--console'
])

PyInstaller.__main__.run([
    'generatekey.py',
    '--name', 'generatekey',
    '--onefile',
    '--clean',
    '--console'
])
