const Discord = require('discord.js');
const fetch = require('node-fetch');
const querystring = require('querystring');

const client = new Discord.Client();
const prefix = ',';

client.once('ready', () => {
	console.log("Kido! I'm Ready!");
});

client.on('message', async message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;

	const args = message.content.slice(prefix.length).split(/ +/);
	const command = args.shift().toLowerCase();

	if (command === 'sim') {
		if (!args.length) {
			return message.channel.send('Gọi gì bố?');
		}

		const query = querystring.stringify({ term: args.join(' ') });

		const { body } = await fetch(`http://api.vietbot.net/simsimi.php?key=sibendz&text=${query}`).then(response => response.json());

		const embed = new Discord.RichEmbed()
			.setColor('#00ffff')
			.setTitle('Simsimi BOT, created by Kido')

		message.channel.send(embed);
	}
});

client.login(process.env.BOT_TOKEN);//where BOT_TOKEN is the token of our bot
