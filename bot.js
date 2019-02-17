const Discord = require('discord.js');
const fetch = require('node-fetch');
const querystring = require('querystring');

const client = new Discord.Client();

client.once('ready', () => {
	console.log("Kido! I'm Ready!");
});

client.on('message', message => {
	if (message.content === {query}) {
		const body = fetch.get('http://api.vietbot.net/simsimi.php?key=sibendz&text=${query}').then(response => response.json());
		message.reply(body);
	}
});

client.login(process.env.BOT_TOKEN);//where BOT_TOKEN is the token of our bot
