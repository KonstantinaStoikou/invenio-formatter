# -*- coding: utf-8 -*-
## $Id$

## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005 CERN.
##
## The CDSware is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## The CDSware is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDSware; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

def format(bfo, separator="; ", print_link="yes"):
    """
    Prints a list of addresses linked to this report
    
    @param separator the separator between addresses.
    @param print_link Link the addresses to search engine (HTML links) if 'yes'
    """
    from urllib import quote
    from invenio.config import weburl

    addresses = bfo.fields('270')
    list_addresses = []
    for address in addresses:
        list_addresses.append('<a href="'+weburl+'/search.py?f=author&p='+ quote(address.get('p', "")) +'">'+address.get('p', "")+'</a>')
        list_addresses.append(address.get('g', ""))

    return separator.join(list_addresses)