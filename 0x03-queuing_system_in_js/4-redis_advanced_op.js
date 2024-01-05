import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const asyncHSet = promisify(client.hset).bind(client);

async function setHolbertonSchools() {
  try {
    await hsetAsync('HolbertonSchools', 'Portland', 50, redis.print);
    await hsetAsync('HolbertonSchools', 'Seattle', 80, redis.print);
    await hsetAsync('HolbertonSchools', 'New York', 20, redis.print);
    await hsetAsync('HolbertonSchools', 'Bogota', 20, redis.print);
    await hsetAsync('HolbertonSchools', 'Cali', 40, redis.print);
    await hsetAsync('HolbertonSchools', 'Paris', 2, redis.print);
  } catch (error) {
    console.log(error);
  }
}
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.log(err);
  }
  console.log(result);
})
