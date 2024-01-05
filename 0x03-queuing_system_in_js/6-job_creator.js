const kue = require('kue');
const queue = kue.createQueue()

const jobData = {
  phoneNumber: '07057387314',
  message: 'Howdy',
}

const notificationJob = queue.create('push_notification_code', jobData);
notificationJob.on('enqueue', function (id, type) {
  console.log(`Notification job created: ${notificationJob.id}`);
})

notificationJob.on('complete', () => {
  console.log('Notification job completed');
  notificationJob.remove();
})

notificationJob.on('failed', (err) => {
  console.log('Notification job failed');
})

notificationJob.save();
