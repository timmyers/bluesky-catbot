const { BskyAgent } = require('@atproto/api')
const fs = require('node:fs/promises')

(async () => {
  console.log('Catbot starting...')
  const prompt = process.env.PROMPT

  const agent = new BskyAgent({ service: 'https://bsky.social' })

  await agent.login({
    identifier: process.env.BLUESKY_USERNAME,
    password: process.env.BLUESKY_PASSWORD,
  })

  const imgData = await fs.readFile("cat.jpg")

  console.log('Logged in, uploading...')

  const blob = await agent.api.com.atproto.repo.uploadBlob(
    imgData, {
      encoding: 'image/jpeg',
    }
  )

  console.log('Uploaded image, posting...')

  await agent.post({
    text: "",
    embed: {
      images: [{
        image: blob.data.blob,
        alt: prompt,
      }],
      $type: 'app.bsky.embed.images'
    }
  });

  console.log('Posted.')
})()