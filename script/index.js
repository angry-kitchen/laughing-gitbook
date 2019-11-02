const path = require('path')
const { publish } = require('gh-pages')

publish(path.join(__dirname, '../_book'), err => {
  console.error("发布出错 ", err)
})
