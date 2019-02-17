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

	if (command === 'simsimi') {
		if (!args.length) {
			return message.channel.send('Gọi gì bố?');
		}

		const query = querystring.stringify({ term: args.join(' ') });

		const { body } = await fetch.get(`http://api.vietbot.net/simsimi.php?key=sibendz&text=${query}`).then(response => response.json());

		if (!body.list.length) {
			return message.channel.send(`Deoco từ này **${args.join(' ')}**, dạy bố đi!`);
		}

		const [answer] = body.list;

		message.channel.send(body.list[0].definition);
	}
});

client.login(process.env.BOT_TOKEN);//where BOT_TOKEN is the token of our bot
