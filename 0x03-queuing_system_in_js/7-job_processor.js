const kue = require('kue');

const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
      done();
    }, 2000);
  }
}

const queue = kue.createQueue({
  concurrency: 2,
});

queue.process('push_notification_code_2', 2, function (job, done) {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, done);
});

queue.on('job complete', function (id, result) {
  kue.Job.get(id, function (err, job) {
    if (err) return;
    job.remove(function (err) {
      if (err) throw err;
      console.log(`Removed completed job #${job.id} from queue`);
    });
  });
});

queue.on('job failed', function (id, result) {
  kue.Job.get(id, function (err, job) {
    if (err) return;
    console.log(`Job #${job.id} failed with error: ${result.message}`);
  });
});

