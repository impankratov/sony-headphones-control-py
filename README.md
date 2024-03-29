Sony Headphones Control
=======

Allows changing the noise-cancelling mode of Sony Bluetooth headsets.
Inspired by [sony-headphones-control](https://github.com/ClusterM/sony-headphones-control) Tasker plugin.

Usage
--------

```
sony-headphones-control <bt_addr> <mode>
```

`bt_addr` - MAC address of Bluetooth headset

`mode` - one of following:
- noise-cancelling
- wind-cancelling
- ambient-sound
- disable

Examples
--------

```
sony-headphones-control 00:00:00:00:00:00 noise-cancelling
```

Installation
------------

Clone repository and run:

```
poetry install
poetry build
```

License
-------

> sony-headphones-control-py is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

> sony-headphones-control-py is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

> You should have received a copy of the GNU General Public License along with
sony-headphones-control-py; if not, write to the Free Software Foundation, Inc., 51 Franklin St,
Fifth Floor, Boston, MA 02110-1301 USA
