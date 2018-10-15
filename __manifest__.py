# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2018 NEOGESTIO.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'DurbWine module',
    'version': '11.0.1.0.0',
    'summary': 'DurbWine customization',
    'sequence': '1',
    'description': """
Wine cellar management
======================
    """,
    'category': 'Sales',
    'author': 'NeoGestio',
    'depends': [
        'NEOGESTIO_wine',
        'point_of_sale',
        ],
    'data': [

    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
