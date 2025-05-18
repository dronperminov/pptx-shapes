import colorsys
import re


def cm_to_emu(cm: float) -> str:
    return str(round(cm * 360000))


def pt_to_emu(pt: float) -> str:
    return str(round(pt * 12700))


def pt_to_font(pt: float) -> str:
    return str(round(pt * 100))


def scale_to_unit(scale: float) -> str:
    return str(round(scale * 100000))


def fraction_to_unit(fraction: float) -> str:
    return scale_to_unit(max(0.0, min(1.0, fraction)))


def angle_to_unit(angle: float) -> str:
    return str(round(angle * 60000))


def parse_color(color: str) -> str:
    color = color.strip().lstrip("#").lower()

    name2color = {
        "black": "000000",
        "white": "ffffff",
        "red": "ff0000",
        "green": "00ff00",
        "blue": "0000ff",
        "yellow": "ffff00",
        "magenta": "ff00ff",
        "cyan": "00ffff"
    }

    if color in name2color:
        return name2color[color]

    if re.fullmatch(r"[\da-f]{3}", color):
        r, g, b = color
        return f"{r}{r}{g}{g}{b}{b}"

    if re.fullmatch(r"[\da-f]{6}", color):
        return color

    color = re.sub(r"\s+", "", color)

    match = re.fullmatch(r"rgb\((?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3})\)", color)
    if match:
        r, g, b = min(int(match.group("r")), 255), min(int(match.group("g")), 255), min(int(match.group("b")), 255)
        return f"{r:02X}{g:02X}{b:02X}"

    match = re.fullmatch(r"hsl\((?P<h>\d{1,3}),(?P<s>\d{1,3})%,(?P<l>\d{1,3})%\)", color)
    if match:
        hsl = min(int(match.group("h")), 360) / 360, min(int(match.group("s")), 100) / 100, min(int(match.group("l")), 100) / 100
        r, g, b = colorsys.hls_to_rgb(h=hsl[0], s=hsl[1], l=hsl[2])
        return f"{int(r * 255):02X}{int(g * 255):02X}{int(b * 255):02X}"

    raise ValueError(f'Invalid color format "{color}"')
