Overview
=========

tzbuddy is a simple script to visualize times in different timezones.
It displays the current hour as well past and future values.

```bash
$ tzbuddy --tz 'US/Pacific' --tz 'Asia/Tokyo' --tz 'Europe/Rome' --tz 'Europe/Dublin' --tz 'US/Eastern'
Asia/Tokyo      Sat 12:56 am 29/03/14 · 13- 14- 15- 16- 17- 18- 19- 20- 21- 22- 23-| 00 | 01  02  03  04  05  06  07  08  09  10  11  12
Europe/Rome     Fri 04:56 pm 28/03/14 · 05  06  07  08  09  10  11  12  13  14  15 | 16 | 17  18  19  20  21  22  23  00+ 01+ 02+ 03+ 04+
Local           Fri 03:56 pm 28/03/14 · 04  05  06  07  08  09  10  11  12  13  14 | 15 | 16  17  18  19  20  21  22  23  00+ 01+ 02+ 03+
Us/Eastern      Fri 11:56 am 28/03/14 · 00  01  02  03  04  05  06  07  08  09  10 | 11 | 12  13  14  15  16  17  18  19  20  21  22  23
Us/Pacific      Fri 08:56 am 28/03/14 · 21- 22- 23- 00  01  02  03  04  05  06  07 | 08 | 09  10  11  12  13  14  15  16  17  18  19  20
```

Install
========
Clone the repository, then install inside the virtualenv
```bash
pip install ./
```

It is not currently pushed to pypi, but it will be soon.


Usage
=======

See `tzbuddy --help` for all available options. There is no configuration, so you probably want to create an alias.

