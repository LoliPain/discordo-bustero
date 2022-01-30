# Headers
> 
> -H `authorization: ***token***`
> 
> -H `user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36` 
> 
> -H `content-type: application/json`


# API send message 

> BaseURL
> > https://discord.com/api/v9/channels/338400013367377932/messages
> 
> > POST /channels/{channel.id}/messages

> Request
> 
> > curl
> >
> > -H `:method: POST` 
> >
> > -H `:authority: discord.com` 
> >
> > -H `:scheme: https` 
> >
> > -H `:path: /api/v9/channels/338400013367377932/messages`

> JSON Content
>
> > --data-binary `{"content":"123","nonce":"930065521649385472","tts":false}`

---------

> JSON research 

> {
	"content": "123",
	"nonce": "930065521649385472",
	"tts": false
}

> "content" `REQUIRED`
> > - Plain text
> > - Emoji:
> > - - Default Unicode emoji: 😫 (converted to http entities)
> > - - Custom server emoji: <:1163512:811709376540049459> || <:**emoji_ID**:**server_ID**>

> "nonce"
> > - String:
> > - - Unique randomID for event that preventing double intercations *(??)*

> "tts" `REQUIRED`
> > - Bool
> > - - Enables/Disables text to speech feature reading "content" text


# API send reaction

> BaseURL
>
> > https://discord.com/api/v9/channels/661365069006897154/messages/908665404858183761/reactions/heart_ghost%3A878987844104892488/%40me
> 
> > PUT /channels/{channel.id}/messages/{message.id}/reactions/{emoji}/@me

> Request
>
> > curl 
> >
> > -H `:method: PUT` 
> >
> > -H `:authority: discord.com` 
> >
> > -H `:scheme: https` 
> >
> > -H `:path: /api/v9/channels/661365069006897154/messages/908665404858183761/reactions/heart_ghost%3A878987844104892488/%40me` 

---------

> Request research

> `{channel.id} `
> > Server setting Channel ID
> 
> `{message.id}`
> > Server setting message ID
> 
> `{emoji}`
> > Server setting SymID


# Confirmation research

> BaseURL
>
> #### Get the confirmation body terms
>
> > https://discord.com/api/v9/guilds/848996376896602163/member-verification?with_guild=false&invite_code=masafinance 
> > > GET /guilds/{guild}/member-verification?with_guild=false&invite_code={code}


> #### Send the confirmation
> 
> > https://discord.com/api/v9/guilds/848996376896602163/requests/@me
> > > PUT /guilds/{guild}/requests/@me

---------

> Researching requests
>

> #### Get content
> > {
	"version": "2021-11-08T12:21:16.941000+00:00",
	"form_fields": [{
		"field_type": "TERMS",
		"label": "Read and agree to the server rules",
		"description": null,
		"automations": null,
		"required": true,
		"values": [""]
	}],
	"description": "" **(!!!)**
}

> #### Send content
> > {
	"version": "2021-11-08T12:21:16.941000+00:00",
	"form_fields": [{
		"field_type": "TERMS",
		"label": "Read and agree to the server rules",
		"description": null,
		"automations": null,
		"required": true,
		"values": [""],
		"response": true **(!!!)**
	}]
}

