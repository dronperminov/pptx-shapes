from enum import Enum


class LineDash(Enum):
    SOLID = "solid"
    DASHED = "dash"
    DOTTED = "sysDot"
    SHORT_DASHED = "sysDash"
    DASH_DOTTED = "dashDot"
    LONG_DASH = "lgDash"
    LONG_DASH_DOTTED = "lgDashDot"
    LONG_DASH_DOT_DOTTED = "lgDashDotDot"
