const path = require('path')
const ghPages = require('gh-pages')

ghPages.publish(path.join(__dirname, '../_book'), err => {
  console.error(err)
})
