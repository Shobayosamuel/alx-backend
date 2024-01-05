const kue = require('kue');
const queue = kue.createQueue();

queue.process('push_notification_code', function (job, done) {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
