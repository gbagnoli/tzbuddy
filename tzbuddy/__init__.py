#!/usr/bin/env python
# coding: utf-8

import argparse
import arrow
from operator import itemgetter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tz", "-z", help="Timezone to show", action="append")
    parser.add_argument("--no-order", "-O", help="Do not sort timezones",
                        action="store_true", default=False)
    parser.add_argument("--inverse-order", "-I", help="Sort TZ west to east",
                        action="store_true", default=False)
    parser.add_argument("--no-local", "-L", help="Do not add local timezone",
                        action="store_true", default=False)
    parser.add_argument("--no-header", "-H", help="Do not print TZ header",
                        action="store_true", default=False)
    parser.add_argument("date", nargs="?", default=None,
                        help="Calculate times from a specific date")
    parser.add_argument("--vertical", "-v", default=False, action="store_true",
                        help="Vertical output")
    parser.add_argument("--span", "-s", default=24, type=int, dest="span",
                        help="How many hours to print. defaults to 24")
    parser.add_argument("--am-pm-hours", "-a", help="Use 12h (am/pm) for hours",
                        action="store_true", default=False)
    args = parser.parse_args()

    if not args.date:
        args.date = arrow.utcnow()

    else:
        try:
            args.date = arrow.get(args.date)
        except arrow.parser.ParserError as e:
            parser.error(e)

    if not args.tz:
        args.tz = ["local"]
    elif not args.no_local:
        args.tz.insert(0, "local")

    args.tz = ((x, int(arrow.utcnow().to(x).format("Z"))) for x in args.tz)
    try:
        args.tz = set(args.tz)
    except arrow.parser.ParserError as e:
        parser.error(e[0].format(e[1]))

    return args


def reordered(tzs, inverse):
    """ Order timezones so that the eastern countries come first """
    st = sorted(tzs, key=itemgetter(1))
    if inverse:
        return [x[0] for x in st]

    return reversed([x[0] for x in st])


def calculate_tz(date, tz, hour_format_12, span=24, header=True, sep=True):
    local = date.to(tz)
    today = local.day
    hours = []
    if header:
        hours.append("{0:16}".format(tz.title()))
        hours.append(local.format("(Z) ddd hh:mm a DD/MM/YY"))
        if sep:
            hours.append(u" ·")

    span_half = int(span / 2.0) - 1
    for h in (x - span_half for x in range(span)):
        hr = local.replace(hours=h)
        if hr.day < today:
            mod = "-"
        elif hr.day > today:
            mod = "+"
        else:
            mod = " "

        if hour_format_12:
            hr = hr.format("hha")
        else:
        hr = hr.format("HH")

        if h == 0:
            hours.append("| %s%s|" % (hr, mod))
        else:
            hours.append(" %s%s" % (hr, mod))

    return hours


def main():
    args = parse_args()
    res = []
    if args.no_order:
        for tz in (x[0] for x in args.tz):
            res.append(calculate_tz(args.date, tz, args.am_pm_hours, args.span,
                                    not args.no_header,
                                    not args.vertical))
    else:
        for tz in reordered(args.tz, args.inverse_order):
            res.append(calculate_tz(args.date, tz, args.am_pm_hours, args.span,
                                    not args.no_header,
                                    not args.vertical))

    if not args.vertical:
        for r in res:
            print("".join(r))

    else:
        res = list(zip(*res[::-1]))
        if args.no_header:
            w = max((len(x) for x in res[0])) + 2
        else:
            w = len(res[1][0]) + 2

        for r in res:
            print(".".join(x.center(w, " ") for x in r))

if __name__ == '__main__':
    main()
