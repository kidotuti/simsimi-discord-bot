const Discord = require('discord.js');

const client = new Discord.Client();

 

client.on('ready', () => {

    console.log('I am ready! Kido');

});


client.on('ready', () => {
    client.user.setStatus('dnd')
    client.user.setPresence({
        game: {
            name: 'Simsimi BOT, developed by Kido#9203. Have a great time!',
            type: "STREAMING",
            url: "https://www.twitch.tv/kidoooooooooooo"
        }
    });
});

 

client.on('message', message => {

    if (message.content === 'kido') {

       message.reply('Bạn cần Kido giúp gì nào? Cứ ibox đừng ngại nhé!')

       }

});


client.login(process.env.BOT_TOKEN);//where BOT_TOKEN is the token of our bot
