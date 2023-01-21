
# Bridge

All ecosystem projects are welcome to a channel that is bridged between their server/telegram using [matterbridge](https://github.com/42wim/matterbridge). See the Ergo Discord for examples of this in action.


## Getting Setup


Follow these simple steps to get bridged;

**1.** Invite @BridgeBot#9505 to your server using [this invite link](https://discordapp.com/oauth2/authorize?&client_id=910495131646455808&scope=bot&permissions=536870912)

> You can set up your [your own bot](https://github.com/42wim/matterbridge/wiki/Discord-bot-setup) but will need to send @Glasgow the `Token` ID if you want it bridged to existing ergo chats. **You only need to grant the bot the ability to see/read messages and set webhooks in the channel you want to bridge.** 

**2.** Invite [ErgoBridgeBot](https://t.me/ErgoBridgeBot) to your Telegram

> You'll need to use `/allowInvitingBots` if Shieldy is enabled.  

**3.** Tag @Glasgow and let him know what channel/server you want to be bridged so it can be added to the configuration. 

## Limitations

1. Discord does currently not allow bots to reply to messages when spoofing someone. 

      - [Allow webhooks to use reply messages#3282](https://github.com/discord/discord-api-docs/discussions/3282)

2. [Telegram API doesn't report deleted messages](https://github.com/42wim/matterbridge/wiki/FAQ#matterbridge-is-not-deleting-messages-from-telegram-to-other-bridges). 
      1. This means any spam deleted on Telegram will remain on Discord.  
      2. **Workaround**: New Telegram users should be restricted from speaking until verifying. [OrgRobot](http://orgrobot.io/) works best here with a set of custom entry questions. This should stop every bot in their tracks. (However sometimes spammers are real people and unpreventable.) 

Other than that, it works pretty well. 

- Names/profile-photos will be spoofed if they are set and the names on both platforms are similar. (names can also be mapped manually). But the profile photos need to be re-cached when a new bridge is added. 
- Responses will reply to the message on Telegram platforms so people will see notifications. On Discord it'll quote the message. 