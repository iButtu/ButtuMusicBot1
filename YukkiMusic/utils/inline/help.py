from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"source_back",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙼𝙸𝙽",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝙻𝙾𝙾𝙿",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝙰𝚄𝚃𝙷",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙿𝙻𝙰𝚈",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="𝚂𝙿𝙻-𝙲𝙼𝙳𝚂",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙿𝙸𝙽𝙶",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="𝙶𝚁𝙿-𝚂𝙴𝚃",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="𝙷𝙴𝚁𝙾𝙺𝚄",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝚂𝚄𝙳𝙾𝙴𝚁𝚂",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="𝙶-𝙱𝙰𝙽",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃",
                    callback_data="help_callback hb12",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🍏 𝙷𝙴𝙻𝙿 🍏",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
