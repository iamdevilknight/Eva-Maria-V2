class script(object):
    START_TXT = """<b>Hey {} !</b>

<b><i>I'm An Advanced Group Managing bot Created For @MovieJunction 🔥

Hit /Help To Know More...! 🙊</b></i>"""
    HELP_TXT = """Hey {}
Here Is A Brief Details About Some of the Features Of Mine..."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: @MasterOfTG
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: N/A
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: N/A
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.0 [ Stable ]"""
    SOURCE_TXT = """✯ Kanged And Modified By @MasterOfTG 🙂

✯ Special Courtesy To :
   ● Team Eva Maria
   ● Team TrojanzHex
   ● Team CrazyBotsz
   ● Team InFoTel 

✯ Bot Managed By :
   ● @DoubleAgent2
   ● @Mr_WarLord
   ● @Jeffrey_morgan2

- <a href=https://t.me/MovieJunction>Team Movie Junction ⚡</a>"""
    MANUELFILTER_TXT = """Feature: <b>Filter</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Diana can only used at @MovieJunction Group 😊.
2. only admins can add filters in diana.
3. So Ultimately You're Just Wasting Your Time 🤐.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Feature: <b>Filter Buttons</b>

- Diana Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Diana supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieJunction)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Feature: <b>Auto Filter</b>

<b>NOTE:</b>
1.<code> Make Me The Admin Of Your Channel and And Add The Channel In Auth List.</code>
2.<code> That's It,Now I Will Index The Channel Files In</code> @MovieJunctionGrp ⚡.
3.<code> And Obviously Won't Work Anywhere Else 🙃</code>"""
    CONNECTION_TXT = """Feature: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Feature: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of diana

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
• <code>There Are A Bunch Of Extra Modules Kanged From @BanhammerMarie_bot And Still Not Added In This Essay 😪(മടി 🙃),Gud Luck Finding Them Yourself 😅</code>"""
    ADMIN_TXT = """Feature: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""

## Pattishow Starts Here

GREETINGS_TEXT = """Feature: <b>Greetings</b>

<b>NOTE:</b>
This Module Only Works In Groups

<b>Commands and Usage:</b>

★ Ban Commands :
• /ban - <code>Ban A User From Group By Replying Or Mentioning [If You Have Any Reasons,Type That After A Space.]</code>
• /kick - <code>Kick Out A User.</code>
• /tban - <code>Ban A User For Some Period Of Time (1m/1h/1d/1w/).</code>
• /unban - <code>Un Ban A User.</code>

★ Mute Commands :
• /mute - <code>Mute A User (By Mentioning Or Replying).</code>
• /tmute - <code>Mute An User For A Period Of Time (1m/1h/1d/1w)</code>
• /unmute  - <code>Un Mute A User.</code>

★ Warn Commands :
• /warn  -  <code>Warn A User By Mentioning Or Replying [eg: /warn @mention reason.]</code>
• /resetwarn - <code>Reset Warns Of A User.</code>
• /warns - <code>Get A User's Number, And Reason Of Warnings,Can Be Used By Mentioning Or Replying</code>
• /addwarn  - <code>Set Automated Warn Filter For Some Words.[eg: /setwarn ""wtf"" No Abusive Words Allowed Here 😠.]</code>
• /nowarn - <code>Stop A Warning Filter.</code>
• /warnlist - <code>List Of All Current Warn Filters.</code>
• /warnlimit  - <code>Set A Limit For Warn,After Exceeding This Limit User Will Be Banned From Chat.</code>
• /strongwarn True/False - <code>If True User Will Be Banned After Warning,Else Will be just kicked.</code>"""

RESTRICTION_TEXT = """Feature: <b>Restrictions</b>

<b>NOTE:</b>
This Module Only Works In Groups

<b>Commands and Usage:</b>

● Welcome Commands :
• /welcome on/off - <code>Enable/Disable Welcome Message.</code>
• /setwelcome - <code>Set A Custom Message.</code>
• /cleanwelcome on/off - <code>If On Then Deletes Previous Welcome Messages When A New Member Joins.</code>
• /resetwelcome - <code>Reset The Welcome Message.</code>

● Goodbye Commands :
• /goodbye - <code>Same Usage And Args as Welcome Commands [Replace welcome with goodbye in above mentioned command]</code>"""

## Pattishow Ends Here
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
