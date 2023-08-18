# Chat Bridge

We welcome all ecosystem projects to establish a channel that is bridged between their server/telegram using [matterbridge](https://github.com/42wim/matterbridge). You can see examples of this in action on the Ergo Discord.


## Setting Up the Bridge


To set up a bridge, follow these steps:

**1.** Use [this invite link](https://discordapp.com/oauth2/authorize?&client_id=910495131646455808&scope=bot&permissions=536870912) to invite @BridgeBot#9505 to your server.

> If you prefer, you can set up [your own bot](https://github.com/42wim/matterbridge/wiki/Discord-bot-setup). However, you will need to send the `Token` ID to @Glasgow if you want it bridged to existing Ergo chats. **The bot only needs permission to see/read messages and set webhooks in the channel you want to bridge.** 

**2.** Invite [ErgoBridgeBot](https://t.me/ErgoBridgeBot) to your Telegram.

> If Shieldy is enabled, you'll need to use `/allowInvitingBots`.  

**3.** Notify @Glasgow about the channel/server you want to bridge so it can be added to the configuration. 

## Known Limitations

1. Discord does not currently allow bots to reply to messages when spoofing someone. 

      - [Allow webhooks to use reply messages#3282](https://github.com/discord/discord-api-docs/discussions/3282)

2. The [Telegram API does not report deleted messages](https://github.com/42wim/matterbridge/wiki/FAQ#matterbridge-is-not-deleting-messages-from-telegram-to-other-bridges). 
      1. This means any spam deleted on Telegram will remain visible on Discord.  
      2. **Workaround**: Restrict new Telegram users from speaking until they verify their identity. [OrgRobot](http://orgrobot.io/) is a useful tool for this, with a set of custom entry questions. This should stop most bots. (However, some spammers are real people and cannot be prevented.) 

Despite these limitations, the bridge works quite well. 

- If set, names/profile-photos will be spoofed if they are similar on both platforms. (Names can also be manually mapped). However, profile photos need to be re-cached when a new bridge is added. 
- Responses will reply to the message on Telegram platforms, triggering notifications. On Discord, the message will be quoted. 
