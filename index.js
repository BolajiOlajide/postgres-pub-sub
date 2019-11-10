const PGPubsub = require('pg-pubsub');
const uri = 'postgres://testuser:testuser@localhost/dump';
const pubsubInstance = new PGPubsub(uri);


const channelName = 'new_stuff';
const listener = (e) => console.log(e);

(async () => {
  try {
    pubsubInstance.addChannel(channelName, listener);
  } catch {
    pubsubInstance.close();
    console.log('Ma pa mi nau!');
  }
})();