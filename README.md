Overview
=========

tzbuddy is a simple script to visualize times in different timezones.
It displays the current hour as well past and future values.

```bash
$ tzbuddy --tz 'US/Pacific' --tz 'Asia/Tokyo' --tz 'Europe/Rome' -s 18
Asia/Tokyo      Sat 01:11 am 29/03/14 · 17- 18- 19- 20- 21- 22- 23- 00 | 01 | 02  03  04  05  06  07  08  09  10
Europe/Rome     Fri 05:11 pm 28/03/14 · 09  10  11  12  13  14  15  16 | 17 | 18  19  20  21  22  23  00+ 01+ 02+
Local           Fri 04:11 pm 28/03/14 · 08  09  10  11  12  13  14  15 | 16 | 17  18  19  20  21  22  23  00+ 01+
Us/Pacific      Fri 09:11 am 28/03/14 · 01  02  03  04  05  06  07  08 | 09 | 10  11  12  13  14  15  16  17  18
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

