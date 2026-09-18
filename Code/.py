from pywebio.platform import start_server
from pywebio.input import  *
from pywebio.output import *
from pywebio.session import *

import asyncio

chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100

async def main():
    global chat_msgs

    put_markdown("## Welcome to PyWebIO Chat Room! (Max messages: %d)")

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    nickname = await input("Enter your nickname", required=True, placeholder="Your nickname", validate=lambda n: "This nickname is already taken" if n in online_users else None)
    online_users.add(nickname)

    chat_msgs.append(('System', f'**{nickname}** joined the chat'))
    msg_box.append(put_markdown(f'**{nickname}** joined the chat'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:
        data = await input_group(
            "Send a message",
            [
                input(placeholder="Type your message here...", name="msg"),
                actions(name="cmd", buttons=["Send", {"label": "Exit", "type": "cancel"}]),
            ],
            validate=lambda m: "Message cannot be empty" if not m["msg"] else None,

        )

        if data is None:
            break


        msg_box.append(put_markdown(f'**{nickname}**: {data["msg"]}'))
        chat_msgs.append((nickname, data["msg"]))

    # exit chat
    refresh_task.close()
    online_users.remove(nickname)

    toast("You have left the chat", color="info")
    msg_box.append(put_markdown(f'**{nickname}** left the chat'))

    chat_msgs.append(('System', f'**{nickname}** left the chat'))

    put_buttons(["refresh"], onclick=lambda _: run_js("window.location.reload()"))


async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)
    while True:
        await asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:
                msg_box.append(put_markdown(f'**{m[0]}**: {m[1]}'))

        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

        last_idx = len(chat_msgs)

if __name__ == '__main__':
    start_server(main, debug=True, port=8080, cdn=False)
